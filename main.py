from gamepad import Gamepad
from sender import Sender

class Main:

    deck_gamepad = Gamepad("/dev/input/event10")

    deck_gamepad.run()

    #data_sender = Sender("", 0)

    #data_sender.send(b"")
