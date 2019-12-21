#!/bin/bash

while true; do
    timeout --foreground 18 python snowtest.py
    if [ $? -ne 124 ]; then break; fi
    timeout --foreground 30 python wiggle.py
    if [ $? -ne 124 ]; then break; fi
    timeout --foreground 30 python spin.py
    if [ $? -ne 124 ]; then break; fi
done

