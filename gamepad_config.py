from evdev import InputDevice, categorize, ecodes
import os
import time


#-----------Constants-----------------

DEAD_ZONE_RANGE = 1500

DEAD_ZONE_INPUTS = {0,1,3,4}

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

#----------Functions------------------

# Controle da Zona morta dos analogicos
def config_dead_zone(dead_zone_range, dead_zone_inputs, event):

    state = event.value

    if event.code in dead_zone_inputs:
        if abs(event.value) <= dead_zone_range: state = 0

    return state

#Leitura e mapeamento dos botẽos baseado nos codigos
def read_event(gamepad_map, event):

    if event.code in gamepad_map:

        if event.type == ecodes.EV_ABS:

            state = config_dead_zone(DEAD_ZONE_RANGE, DEAD_ZONE_INPUTS, event)

        elif event.type == ecodes.EV_KEY:

            state = event.value

        else:

            state = None

        button = gamepad_map.get(event.code, "")

        return button, state
    else:
        return None, None


#----------Exec----------------

def main():

    gamepad_output = {}

    gamepad = InputDevice("/dev/input/event10")

    print(gamepad.capabilities())

    for event in gamepad.read_loop():
        
        #os.system("clear")

        button, state = read_event(GAMEPAD_MAP, event)

        if button is None or state is None: continue

        gamepad_output[button] = state

        print(gamepad_output)

main()

