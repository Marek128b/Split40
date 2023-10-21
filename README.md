# ErgoSplit50

** table of content **
- [ErgoSplit50](#ergosplit50)
  - [Description](#description)
  - [Price](#price)
  - [Firmware](#firmware)
    - [Keyboards RGB](#keyboards-rgb)

## Description 

The ErgoSplit50 is a 50% split keyboard which means that the keyboard is in two half's which is better for ergonomics than a "normal" keyboard. A 50% Keyboard is smaller compared to a normal 100% keyboard with function and number keys as well as a num keys.
The Keyboard has a ortho linear key layout which is more ergonomic than the staggered key layout (normal layout).

___
Here you can see both half of the keyboard built using [Keyboard Layout Editor](http://www.keyboard-layout-editor.com/#/gists/dc776eb6e80d4ed39cddeabd265ff729) <br>
<img src="hardware/keyboard 2d Files/ergosplit-50-1.png"> <br> 
___
This keyboard layout is better for ergonomics as it accommodates the different sizes of your fingers. 


## Price

| AMOUNT 	| ITEM                  	| SUPPLIER  	| PRICE  	| SHIPPING 	| PRICE  	| PRICE TOTAL 	    |
|--------	|-----------------------	|-----------	|--------	|----------	|--------	|------------------ |
| 2x     	| RP2040-USB-C          	| Barrybase 	| €5,55  	| €3,33    	| €11,10 	|             	    |
| 1x     	| USB-C 2.0 1m Kabel    	| Barrybase 	| €2,92  	| €5,95    	| €2,90  	|             	    |
| 1x     	| 110 Gateron G PRO RED 	| Keychron  	| €19,-  	| €15,-    	| €34,-  	|             	    |
|        	|                       	|           	| TOTAL: 	| €24,28   	| €48,-  	| **€72,28**      	|


Product links: 
1. [RP2040-uC](https://www.berrybase.at/en/waveshare-rp2040-zero-ohne-header)
2. [USB-C cable](https://www.berrybase.at/en/usb-c-2.0-sync-ladekabel-a-stecker-c-stecker-schwarz?number=45735)
3. [Gateron red Switches](https://www.keychron.com/collections/all-switches/products/gateron-switch-set?variant=40119134355545)

<br>
Building firmware:

https://www.tablesgenerator.com/markdown_tables <br>
http://builder.swillkb.com/

## Firmware 
The firmware i used is called [QMK](https://docs.qmk.fm/#/) which is a popular keyboard firmware for wired Keyboards. The reason i am using this firmware is that it works more reliable and doesn't have the problems i faced when i was trying to use [KMK](http://kmkfw.io).

### Keyboards RGB
This keyboard uses a [RP2040](https://docs.qmk.fm/#/platformdev_rp2040?id=raspberry-pi-rp2040) microcontroller that has a on-board [ws2812-2020](https://docs.qmk.fm/#/ws2812_driver)
 rgb led that is used for signaling on which layer you are, if caps lock is enabled, if num lock is enabled and if scroll lock is enabled. <br>

