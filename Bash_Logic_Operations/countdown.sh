#!/bin/bash

read -p "Enter a number to start countdown: " number

while [ $number -ge 1 ]
do
    echo $number
    number=$((number - 1))
done

echo "Countdown complete!"
