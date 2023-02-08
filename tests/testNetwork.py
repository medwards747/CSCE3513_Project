import unittest
import socket
import multiprocessing
import time
from itertools import product
from csce3513_project.Network import NetworkReceiver, NetworkSender


class TestNetworkSender(unittest.TestCase):
    def run_server(self, test_string, address='127.0.0.1', port=7500):
        s = socket.socket(
            family=socket.AF_INET, type=socket.SOCK_DGRAM)
        s.bind((address, port))

        data = None
        while data is None:
            data, addr = s.recvfrom(NetworkReceiver.max_buffer_size)
            print(
                f"Received data: {data.decode()} from {str(addr[0])}:{str(addr[1])}")

        s.close()

        # Verify the data
        self.assertEqual(data.decode(), test_string)

    def test_send(self):
        strings = ["1234567890:123456790", "1:2"]
        remote_addresses = ['127.0.0.1', '0.0.0.0']
        remote_ports = [7500, 60000]

        for string, remote_address, remote_port in product(strings, remote_addresses, remote_ports):
            print(
                f"Testing {string} {remote_address} {remote_port}")
            t = multiprocessing.Process(target=self.run_server,
                                        args=(string, remote_address, remote_port))
            t.start()

            # Wait for the server to start
            time.sleep(0.1)

            n = NetworkSender(remote_address=remote_address,
                              remote_port=remote_port)
            n.send_data(string)

            t.join()


class TestNetworkReceiver(unittest.TestCase):
    def test_receive(self):
        strings = ["1234567890:123456790", "1:2"]
        listen_addresses = ['0.0.0.0', '127.0.0.1']
        listen_ports = [7501, 60001]

        for string, listen_address, listen_port in product(strings, listen_addresses, listen_ports):
            # Start the receiver
            n = NetworkReceiver(listen_address=listen_address,
                                listen_port=listen_port)
            n.start_rx()

            # Wait for the server to start
            time.sleep(0.1)

            # Send the test data
            s = socket.socket(
                family=socket.AF_INET, type=socket.SOCK_DGRAM)
            s.sendto(
                string.encode(), (listen_address, listen_port))
            s.close()

            n.stop_rx()

            # Verify the data
            string_received = n.poll_result()
            print(f"Received data: {string_received}")
            self.assertEqual(string, string_received)


if __name__ == '__main__':
    unittest.main()
