#!/bin/bash

while true; do
    timeout 18 python snowtest.py
    timeout 30 python wiggle.py
    timeout 30 python spin.py
done

