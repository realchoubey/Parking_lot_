#!/bin/bash

if [ $# -eq 0 ]
  then
    python ../src/ParkingController.py
else
    if [ -e $1 ]
    then
        python ../src/ParkingController.py $1
    else
        echo "Please give correct file path."
    fi
fi