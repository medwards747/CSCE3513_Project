import select
import socket
import multiprocessing


class NetworkSender:
    def __init__(self, remote_address='127.0.0.1', remote_port=7500):
        self.remote_address = remote_address
        self.remote_port = remote_port

        # Create a UDP socket at client side
        self.s = socket.socket(
            family=socket.AF_INET, type=socket.SOCK_DGRAM)

    def send_data(self, data: str):
        # Send data (a string) to multicast UDP on the transmitter port

        # Send to server using created UDP socket and encode the data to bytes
        self.s.sendto(data.encode(), (self.remote_address, self.remote_port))

    def __del__(self):
        # Close the socket
        self.s.close()


class NetworkReceiver:
    max_buffer_size = 128

    def __init__(self, listen_address='0.0.0.0', listen_port=7501):
        self.listen_address = listen_address
        self.listen_port = listen_port
        self._run = True
        self._manager = multiprocessing.Manager()
        self._stop_flag = self._manager.Value("B", 0)
        self._result_queue = self._manager.Queue()

    def _rx(self):
        # Start the receiver that listens on the receiver port (UDP) and call the callback function with the received data (a string)
        self._s = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        self._s.bind((self.listen_address, self.listen_port))

        while not self._stop_flag.value:
            ready_to_read, _, _ = select.select([self._s], [], [], 0.5)
            if ready_to_read:
                data, client_address = self._s.recvfrom(1024)
                # perform desired processing
                self._result_queue.put(data.decode())

        self._s.close()

    def start_rx(self):
        self._t = multiprocessing.Process(target=self._rx)

        self._t.start()

    def stop_rx(self):
        # Stop the receiver
        self._stop_flag.value = 1
        self._t.join()

    def poll_result(self, block=True, timeout=None):
        # Poll the result queue for new results. Only returns one result.
        if not self._result_queue.empty():
            return self._result_queue.get(block=block, timeout=timeout)
        else:
            return None

    def __del__(self):
        # Stop the receiver when the object is destroyed
        if self._t.is_alive():
            self.stop_rx()
