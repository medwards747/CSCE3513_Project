import unittest
import socket
import multiprocessing
import time
from itertools import product
from csce3513_project.Network import NetworkReceiver, NetworkSender


class TestNetworkSender(unittest.TestCase):
    """Tests the NetworkSender class.

    Arguments:
        unittest -- Inherits from unittest.TestCase for unit testing.
    """

    def run_server(self, test_string: int, address: str, port: int) -> None:
        """Runs a UDP server that receives data and verifies it.
        Blocks until data is received.

        Arguments:
            test_string -- String to verify the data against.
            address -- Address to bind to.
            port -- Port to bind to.

        Exceptions:
            AssertionError -- If the data received does not match the test string.
        """
        s = socket.socket(
            family=socket.AF_INET, type=socket.SOCK_DGRAM)
        s.bind((address, port))

        data = None
        while data is None:
            data, remote_address = s.recvfrom(NetworkReceiver.max_buffer_size)

        s.close()

        # Verify the data
        self.assertEqual(int(data), int(test_string))

    def test_send_hit_player(self) -> None:
        """Tests the send_hit_player method.
        """
        ids = [0, 1, 1234567890, -1]
        remote_addresses = ['127.0.0.1', '0.0.0.0']
        remote_ports = [7500, 60000]

        for id, remote_address, remote_port in product(ids, remote_addresses, remote_ports):
            t = multiprocessing.Process(target=self.run_server,
                                        args=(id, remote_address, remote_port))
            t.start()

            # Wait for the server to start
            time.sleep(0.1)

            n = NetworkSender(remote_address=remote_address,
                              remote_port=remote_port)
            n.send_hit_player(id)

            t.join()


class TestNetworkReceiver(unittest.TestCase):
    """Tests the NetworkReceiver class.

    Arguments:
        unittest -- Inherits from unittest.TestCase for unit testing.
    """

    def send_data(self, remote_address: tuple[str, int], bytes_to_send: bytes) -> None:
        """Send the test data

        Arguments:
            remote_address -- Address or hostname and port to send to.
            bytes_to_send -- Data to send.
        """
        s = socket.socket(
            family=socket.AF_INET, type=socket.SOCK_DGRAM)
        s.sendto(bytes_to_send, remote_address)
        s.close()
        time.sleep(0.05)  # Wait for the data to be received

    def test_receive(self) -> None:
        """Test the UDP server and related methods.
        """
        test_tuples = [(0, 0), (1, 2), (1234567890, 123456790),
                       (-1, -1)]  # Valid
        test_strings = [str(t[1]) for t in test_tuples] + \
            ["0", "aB", ""]  # Invalid
        test_bytes = [bytes(s, 'utf-8')
                      for s in test_strings] + [b'\x00', b'\xFF', b'']  # Invalid
        listen_addresses = ['0.0.0.0', '127.0.0.1']
        listen_ports = [7501, 60001]

        for listen_address, listen_port in product(listen_addresses, listen_ports):
            # Start the receiver
            n = NetworkReceiver(listen_address=listen_address,
                                listen_port=listen_port)

            # Wait for the server to start
            time.sleep(0.05)

            # Test valid data
            for tuple_to_send in test_tuples:
                # Convert the tuple to bytes
                bytes_to_send = bytes(
                    str(tuple_to_send[0]) + ":" + str(tuple_to_send[1]), 'utf-8')

                # Test with process_result
                self.send_data((listen_address, listen_port), bytes_to_send)
                data_received = n.process_result()
                self.assertEqual(data_received, tuple_to_send)

                # Do the same with process_results, but with multiple results
                self.send_data((listen_address, listen_port), bytes_to_send)
                self.send_data((listen_address, listen_port), bytes_to_send)
                data_received = n.process_results()
                self.assertListEqual(
                    data_received, [tuple_to_send, tuple_to_send])

            # Test invalid data
            for bytes_to_send in test_bytes:
                # Test with process_result
                self.send_data((listen_address, listen_port), bytes_to_send)
                data_received = n.process_result()
                self.assertIsNone(data_received)

                # Test with process_results
                self.send_data((listen_address, listen_port), bytes_to_send)
                self.send_data((listen_address, listen_port), bytes_to_send)
                data_received = n.process_results()
                self.assertListEqual(data_received, [])

            # Test with empty results
            data_received = n.process_result()
            self.assertIsNone(data_received)
            data_received = n.process_results()
            self.assertListEqual(data_received, [])


# Run the unit tests
if __name__ == '__main__':
    unittest.main()
