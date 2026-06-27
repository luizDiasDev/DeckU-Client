import socket
import json

class Sender:
    """
    Envia dados via UDP para um endereço IP e porta especificados
    """

    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        #UDP em vez de TCP pois a perda ocasional de pacotes é aceitavel para input de controle
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def send(self, data):
        """
        Envia informações para o caminho especificado
        """

        self.sock.sendto(json.dumps(data).encode("utf-8"), (self.ip, self.port))

    def close(self):
        """
        Fecha o socket e libera o recurso
        """

        self.sock.close()

        self.sock = None

    def __del__(self):
        # Para evitar double-close caso close() já tenha sido chamado manualmente
        if self.sock is not None:
            self.sock.close()
