import logging
import socket
import multiprocessing
import select
from queue import Empty
from typing import Union


class NetworkSender:
    """Class that handles sending data over the network. Uses UDP.
    """

    def __init__(self, remote_address: str = '127.0.0.1', remote_port: int = 7500) -> None:
        """Create a new NetworkSender object.

        Keyword Arguments:
            remote_address -- IP address or hostname to send to. (default: {'127.0.0.1'})
            remote_port -- Server's port to connect to. (default: {7500})
        """
        self._remote_address = remote_address
        self._remote_port = remote_port
        self._logger = logging.getLogger()

        self._logger.debug(
            f"Opening a connection to {self._remote_address}:{self._remote_port}")
        # Create a UDP socket at client side
        self._s = socket.socket(
            family=socket.AF_INET, type=socket.SOCK_DGRAM)

    def _send_data(self, data: bytes) -> None:
        """Sends a string to the remote host.

        Arguments:
            data -- Bytes to send.
        """
        self._logger.debug(
            f"Sending {data} to {self._remote_address}:{self._remote_port}")
        self._s.sendto(
            data, (self._remote_address, self._remote_port))

    def send_hit_player(self, player_id: int) -> None:
        """Sends the player's ID to the remote host to broadcast who got hit.

        Arguments:
            player_id -- The player's ID that got hit.
        """
        self._send_data(str(player_id).encode())

    def __del__(self) -> None:
        """Close the socket when the object is destroyed.
        """
        self._s.close()


class NetworkReceiver:
    """A class that handles receiving data from the network. Runs a UDP server in a separate process.
    Has methods to poll for new results and process them.
    """
    max_buffer_size = 128

    def __init__(self, listen_address: str = '0.0.0.0', listen_port: int = 7501) -> None:
        """Create a new NetworkReceiver object. Automatically starts the receiver.

        Keyword Arguments:
            listen_address -- IP address or hostname to listen on. (default: {'0.0.0.0'})
            listen_port -- Port to listen on. (default: {7501})
        """
        self._listen_address = listen_address
        self._listen_port = listen_port
        self._run = True
        self._manager = multiprocessing.Manager()
        self._stop_flag = self._manager.Value("B", 0)
        self._result_queue = self._manager.Queue()
        self._logger = logging.getLogger()

        # Start the server when object is created
        self._start_rx()

    def _rx(self) -> None:
        """Run the receiver that listens on the receiver port (UDP).
        Receives data and puts it in the result queue as bytes.
        Runs until the stop flag is set then closes the socket.
        """
        self._s = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        self._s.bind((self._listen_address, self._listen_port))

        while not self._stop_flag.value:
            ready_to_read, _, _ = select.select([self._s], [], [], 0.5)
            if ready_to_read:
                data, client_address = self._s.recvfrom(1024)
                self._logger.debug(
                    f"Network receiver got {data} from {client_address}")
                self._result_queue.put(data)

        self._s.close()

    def _start_rx(self) -> None:
        """Start the receiver in a separate process.
        """
        self._logger.debug(
            f"Network receiver starting on {self._listen_address}:{self._listen_port}")
        self._t = multiprocessing.Process(target=self._rx)

        self._t.start()

        self._logger.debug(
            f"Network receiver started on {self._listen_address}:{self._listen_port}")

    def stop_rx(self) -> None:
        """Stop the receiver process. Blocks until the receiver is stopped.
        """
        self._logger.debug(
            f"Network receiver stopping on {self._listen_address}:{self._listen_port}")
        self._stop_flag.value = 1
        self._t.join()
        self._logger.debug(
            f"Network receiver stopped on {self._listen_address}:{self._listen_port}")

    def process_result(self, block: bool = False, timeout: Union[float, None] = None) -> Union[tuple[int, int], None]:
        """Process a single result in the result queue. Returns a tuple with IDs.

        Keyword Arguments:
            block -- Whether the function should wait for a message to return or not. (default: {False})
            timeout -- How long the function should wait for a message before returning None. None will wait indefinitely. (default: {None})

        Returns:
            A tuple with IDs or None if no result is available or invalid data is received.
            Tuple format: (ID of player transmitting, ID of player hit)
        """
        if not self._result_queue.empty():
            # Incoming message format: "ID of player transmitting:ID of player hit"
            try:
                result = self._result_queue.get(block=block, timeout=timeout)
                result = result.decode()
                result = result.split(":")
                id_transmit = int(result[0])
                id_hit = int(result[1])
            except Empty:
                return None
            except ValueError:
                self._logger.error(
                    "Could not convert incoming data to an integer")
                return None
            except IndexError:
                self._logger.error(
                    "Incoming data is not in the correct format")
                return None

            return (id_transmit, id_hit)

    def process_results(self, block: bool = False, timeout: Union[float, None] = None) -> list[tuple[int, int]]:
        """Process all results in the result queue. Returns a list of tuples with IDs.

        Keyword Arguments:
            block -- Whether the function should wait for a message to return or not. (default: {False})
            timeout -- How long the function should wait for a message before returning None. None will wait indefinitely. (default: {None})

        Returns:
            An array filled with integer tuples. Empty if no valid data is received.
            Tuple format: (ID of player transmitting, ID of player hit)
        """
        results = []
        result = self.process_result(block=block, timeout=timeout)
        while result:
            results.append(result)
            result = self.process_result()

        return results

    def __del__(self) -> None:
        """Stop the receiver when the object is destroyed
        """
        if self._t.is_alive():
            self.stop_rx()
