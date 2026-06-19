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


#---------Variables-------------------

gamepad_output = {
        # Botões Clicaveis
        "A": 0,
        "X": 0,
        "Y": 0,
        "B": 0,
        "L1": 0,
        "R1": 0,
        "Select": 0,
        "Start": 0,
        "L6": 0,
        "R6": 0,

        # Gatilhos
        "L2": 0,
        "R2": 0,

        # Analogicos
        "LAX": 0,
        "LAY": 0,
        "RAX": 0,
        "RAY": 0,

        "DPX": 0,
        "DPY": 0
    }

gamepad = InputDevice("/dev/input/event10")

#print(gamepad.capabilities())

#----------Functions------------------

# Controle da Zona morta dos analogicos
def config_dead_Zone(dead_zone_range, dead_zone_inputs, event_code, state):

    if event_code in dead_zone_inputs:
        if abs(state) <= dead_zone_range: state = 0

    return state

#Leitura e mapeamento dos botẽos baseado nos codigos
def read_event(gamepad_map, event_code, state):

    if event_code in gamepad_map:

        new_state = config_dead_Zone(DEAD_ZONE_RANGE, DEAD_ZONE_INPUTS, event_code, state)

        button = gamepad_map.get(event_code, "")

        return button, new_state
    else:
        return None, None


#----------Exec----------------

def main():

    for event in gamepad.read_loop():
        
        #os.system("clear")

        button, state = read_event(GAMEPAD_MAP, event.code, event.value)

        if button is None or state is None: continue

        gamepad_output[button] = state

        print(gamepad_output)

main()

