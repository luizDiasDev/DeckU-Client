import socket
import json

class Sender:

    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def send(self, data):
        self.sock.sendto(json.dumps(data).encode("utf-8"), (self.ip, self.port))

    def close(self):
        self.sock.close()

        self.sock = None

    def __del__(self):
        if self.sock is not None:
            self.sock.close()
