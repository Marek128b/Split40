print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC 
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers #adding layers to kmk 

keyboard = KMKKeyboard() #making a KMKeyboard object

keyboard.modules.append(Layers())

keyboard.col_pins = (board.GP3, board.GP4, board.GP5, board.GP6, board.GP7, board.GP8, board.GP9, board.GP10, board.GP11, board.GP12, board.GP13, board.GP14)  # 12 Columns
keyboard.row_pins = (board.GP15, board.GP26, board.GP27, board.GP28) # 4 Rows
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [[
    #main layer
     KC.A, KC.S,  	#GP10.GP8 | GP10.GP7
     KC.D, KC.TG(1)	#GP11.GP8 | GP11.GP7
    ]
]

if __name__ == '__main__':
    keyboard.go()