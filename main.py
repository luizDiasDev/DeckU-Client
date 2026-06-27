from gamepad import Gamepad
from sender import Sender


def main():

    data_sender = Sender("192.168.100.54", 5005)

    def callback(data):
    
        data_sender.send(data)

    deck_gamepad = Gamepad("/dev/input/event10", callback)

    deck_gamepad.run()

if __name__ == "__main__":
    main()