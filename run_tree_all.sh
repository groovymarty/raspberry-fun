#!/bin/bash

while true; do
    timeout --foreground 15 python ../Programmable-Xmas-Tree/ants.py
    if [ $? -ne 124 ]; then break; fi
    timeout --foreground 15 python ../Programmable-Xmas-Tree/alt.py
    if [ $? -ne 124 ]; then break; fi
    timeout --foreground 15 python ../Programmable-Xmas-Tree/random_leds.py
    if [ $? -ne 124 ]; then break; fi
    timeout --foreground 60 python sparkle.py
    if [ $? -ne 124 ]; then break; fi
    timeout --foreground 60 python glow.py
    if [ $? -ne 124 ]; then break; fi
done

