from evdev import InputDevice, categorize, ecodes
import os
import time


class Gamepad:
    """
    Lê e interpreta eventos de um controle físico 
    """

    DEAD_ZONE_RANGE = 2000 # Valor calibrado manualmente para o Steam Deck, pode variar entre unidades

    DEAD_ZONE_INPUTS = {0,1,3,4} # Códigos referentes aos eixos analógicos do controle

    GAMEPAD_MAP = {
            # Botões Clicáveis
            304: "A",
            307: "X",
            308: "Y",
            305: "B",
            310: "L1",
            311: "R1",
            314: "Select",
            315: "Start",
            317: "L6",
            318: "R6",

            # Gatilhos
            2: "L2",
            5: "R2",

            # Analógicos
            0: "LAX",
            1: "LAY",
            3: "RAX",
            4: "RAY",

            #D-pad
            16: "DPX",
            17: "DPY"
        }


    def __init__(self, device_path, callback):
        self.device_path = device_path
        self.gamepad_output = {}
        self.gamepad = InputDevice(self.device_path)
        self.callback = callback # Função chamada a cada mudança de estado do controle  recebendo gamepad_output como argumento

    def run(self):
        """
        Executa a leitura do Controle
        """

        for event in self.gamepad.read_loop():

            button, state = self._read_event(event)

            if button is None or state is None: continue

            self.gamepad_output[button] = state

            self.callback(self.gamepad_output)


    def _read_event(self, event):
        """
        Leitura e mapeamento dos botẽos baseado nos codigos
        """

        if event.code in self.GAMEPAD_MAP:

            if event.type == ecodes.EV_ABS:

                state = self._config_dead_zone(event)

            elif event.type == ecodes.EV_KEY:

                state = event.value

            else:

                state = None

            button = self.GAMEPAD_MAP.get(event.code, "")

            return button, state
        else:
            return None, None

    def _config_dead_zone(self, event):
        """
        Controle da Zona morta dos analogicos
        """

        state = event.value

        if event.code in self.DEAD_ZONE_INPUTS:
            if abs(event.value) <= self.DEAD_ZONE_RANGE: state = 0

        return state