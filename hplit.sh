#!/bin/bash
echo >/tmp/getpower
./get_power.sh &
./run_16 &
./hpl_logger.py
rm /tmp/getpower
wait 
./ensemble.py

