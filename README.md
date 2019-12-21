# Fun stuff for Raspberry Pi

## Installation

Here are the commands to install fun stuff on your Raspberry Pi:
* cd /home/pi
* git clone https://github.com/groovymarty/raspberry-fun.git

## Christmas Tree

Sample programs for https://thepihut.com/products/christmas-tree-programmable-kit
* sparkle.py - Randomly toggles all LEDs on tree
* glow.py - Uses PWM to glow LEDs on and off, filling tree from bottom to top

Based on sample code found at https://github.com/modmypi/Programmable-Xmas-Tree, especially
class ChristmasTree that lays out all the I/O devices on the board.  I copied this module
to my repo, and wrote similar ones for Snowman and Fish Dish.

Here are the commmands to install Programmable-Xmas-Tree (optional):
* cd /home/pi
* git clone https://github.com/modmypi/Programmable-Xmas-Tree.git

## Snowman

Sample programs for https://thepihut.com/products/ryanteck-snowpi-the-gpio-snowman-for-raspberry-pi
* snowtest.py - Test program from https://thepihut.com/blogs/raspberry-pi-tutorials/ryanteck-snowpi-test-program
* wiggle.py - Rapidly alternates left and right sides, and blinks eyes even faster
* spin.py - Spins body LEDs while toggling eyes and nose

Class Snowman lays out all the I/O devices on the board.

## Fish Dish

Sample programs for https://thepihut.com/products/fish-dish-gpio-led-buzzer-board
* fishtest.py - Test program from https://pastebin.com/8cnxXRNT
* fishbump.py - Binks LEDs in a pattern that changes when you push the button

## Services to run Christmas Tree and Snowman sample programs

You can install services to run the Christmas tree and Snowman programs automatically at startup.

Here are the commands to install the services:
* cd /home/pi/raspberry-fun
* sudo cp *.service /etc/systemd/system
* sudo systemctl daemon-reload

To enable the Christmas Tree demo at startup, type these commands:
* sudo systemctl enable run_tree_all
* sudo systemctl disable run_man_all

To enable the Snowman demo at startup, type these commands:
* sudo systemctl enable run_man_all
* sudo systemctl disable run_tree_all

You can do work on your Pi while the services are running in the background, but if you want
to use the GPIO for something else you'll probably want to step them.  Here are the commands:
* sudo systemctl stop run_man_all
* sudo systemctl stop run_tree_all
