from gamepad import Gamepad
from sender import Sender
from dotenv import load_dotenv
import os


def main():
    """
    Orquestra Gamepad e Sender conectando os dois via callback
    """

    load_dotenv()

    ip = os.getenv("PC_IP")
    port = int(os.getenv("PORT"))
    device = os.getenv("DEVICE_PATH")

    data_sender = Sender(ip, port)

    # Recebe gamepad_output de Gamepad e repassa para Sender
    def callback(data):
    
        data_sender.send(data)

    deck_gamepad = Gamepad(device, callback)

    deck_gamepad.run()

if __name__ == "__main__":
    main()