from gamepad import Gamepad
from sender import Sender


def main():
    """
    Orquestra Gamepad e Sender conectando os dois via callback
    """

    data_sender = Sender("192.168.100.54", 5005)

    # Recebe gamepad_output de Gamepad e repassa para Sender
    def callback(data):
    
        data_sender.send(data)

    deck_gamepad = Gamepad("/dev/input/event10", callback)

    deck_gamepad.run()

if __name__ == "__main__":
    main()