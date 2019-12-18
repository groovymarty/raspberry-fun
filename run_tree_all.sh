#!/bin/bash

while true; do
    timeout 15 python ../Programmable-Xmas-Tree/ants.py
    timeout 15 python ../Programmable-Xmas-Tree/alt.py
    timeout 15 python ../Programmable-Xmas-Tree/random_leds.py
    timeout 60 python sparkle.py
    timeout 60 python glow.py
done

