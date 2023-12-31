# Software

** table of content **
- [Software](#software)
  - [QMK Basics](#qmk-basics)
  - [Keymap and Matrix](#keymap-and-matrix)
  - [RGB WS2812 LEDs](#rgb-ws2812-leds)
  - [Via/Vial support](#viavial-support)

## QMK Basics 
Note: ALL the code parts shown below are located in `./ergosplit44/info.json`

This part of the json document defines the keyboard name, bootloader, manufacturer and the amount of dynamic layers as well as the features of the Keyboard.

``` JSON
"manufacturer": "Marek128b",
"keyboard_name": "ergosplit44",
"maintainer": "Marek128b",
"bootloader": "rp2040",
"diode_direction": "COL2ROW",
"dynamic_keymap": {
    "layer_count": 5
},
"features": {
    "bootmagic": true,
    "command": false,
    "console": false,
    "extrakey": true,
    "mousekey": true,
    "nkro": true,
    "rgb_matrix": true
},
```

## Keymap and Matrix

Here you can see how to define the column Pins and row Pins:
``` JSON
"matrix_pins": {
  "cols": ["GP6", "GP7", "GP8", "GP9", "GP10", "GP11", "GP12", "GP13", "GP14", "GP15", "GP17", "GP18"],
  "rows": ["GP2", "GP3", "GP4", "GP5"]
},
```

---
You define the layout of your Keyboard using this JSON format:

``` JSON
"layouts": {
    "LAYOUT": {
        "layout": [
            {"label":"tab", "matrix": [0, 0],"x":0, "y":1.25}, 
            {"label":"Q", "matrix": [0, 1],"x":1, "y":1.25}, 
            {"label":"W", "matrix": [0, 2],"x":2, "y":0.75}, 
            {"label":"E", "matrix": [0, 3],"x":3, "y":0.5}, 
            {"label":"R", "matrix": [0, 4],"x":4, "y":0.75}, 
            {"label":"T", "matrix": [0, 5],"x":5, "y":1},    
            {"label":"Y", "matrix": [0, 6],"x":9.75, "y":1}, 
            {"label":"U", "matrix": [0, 7],"x":10.75, "y":0.75}, 
            {"label":"I", "matrix": [0, 8],"x":11.75, "y":0.5}, 
            {"label":"O", "matrix": [0, 9],"x":12.75, "y":0.75}, 
            {"label":"P", "matrix": [0, 10],"x":13.75, "y":1.25}, 
            {"label":"\u00dc", "matrix": [0, 11],"x":14.75, "y":1.25}, 
            {"label":"back-space", "matrix": [1, 0],"x":0, "y":2.25}, 
            {"label":"A", "matrix": [1, 1],"x":1, "y":2.25},
            {"label":"S", "matrix": [1, 2],"x":2, "y":1.75},  
            {"label":"D", "matrix": [1, 3],"x":3, "y":1.5}, 
            {"label":"F", "matrix": [1, 4],"x":4, "y":1.75}, 
            {"label":"G", "matrix": [1, 5],"x":5, "y":2}, 
            {"label":"H", "matrix": [1, 6],"x":9.75, "y":2}, 
            {"label":"J", "matrix": [1, 7],"x":10.75, "y":1.75}, 
            {"label":"K", "matrix": [1, 8],"x":11.75, "y":1.5}, 
            {"label":"L", "matrix": [1, 9],"x":12.75, "y":1.75}, 
            {"label":"\u00d6", "matrix": [1, 10],"x":13.75, "y":2.25}, 
            {"label":"\u00c4", "matrix": [1, 11],"x":14.75, "y":2.25}, 
            {"label":"shift", "matrix": [2, 0],"x":0, "y":3.25}, 
            {"label":"Z", "matrix": [2, 1],"x":1, "y":3.25}, 
            {"label":"X", "matrix": [2, 2],"x":2, "y":2.75}, 
            {"label":"C", "matrix": [2, 3],"x":3, "y":2.5}, 
            {"label":"V", "matrix": [2, 4],"x":4, "y":2.75}, 
            {"label":"B", "matrix": [2, 5],"x":5, "y":3}, 
            {"label":"N", "matrix": [2, 6],"x":9.75, "y":3}, 
            {"label":"M", "matrix": [2, 7],"x":10.75, "y":2.75}, 
            {"label":"<", "matrix": [2, 8],"x":11.75, "y":2.5}, 
            {"label":":", "matrix": [2, 9],"x":12.75, "y":2.75}, 
            {"label":"_", "matrix": [2, 10],"x":13.75, "y":3.25}, 
            {"label":"Shift", "matrix": [2, 11],"x":14.75, "y":3.25}, 
            {"label":"L2", "matrix": [3, 2],"x":-3.5, "y":4.5}, 
            {"label":"Alt", "matrix": [3, 3],"x":-2.25, "y":7.25},
            {"label":"Strg", "matrix": [3, 4],"x":-1.0, "y":7.25}, 
            {"label":"Space", "matrix": [3, 5],"x":0, "y":7}, 
            {"label":"Space", "matrix": [3, 6],"x":-1.0, "y":8.5}, 
            {"label":"Strg", "matrix": [3, 7],"x":0, "y":8.75}, 
            {"label":"AltGr", "matrix": [3, 8],"x":1.25, "y":8.75},
            {"label":"L1", "matrix": [3, 9],"x":2.5, "y":5.75}
        ]
    }
}
```

This part of the JSON format defines the X, Y `"x":0, "y":1.25` Position of the key as well as the x and y position of the key in the matrix `"matrix": [0, 0]`.
```JSON
{"label":"tab", "matrix": [0, 0],"x":0, "y":1.25}, 
```


## RGB WS2812 LEDs

This defines the Pin and Driver of your WS2812 LEDs.

``` JSON
"ws2812": {
    "driver": "vendor",
    "pin": "GP26"
},
```

## Via/Vial support
