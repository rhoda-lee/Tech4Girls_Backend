#!/bin/bash

read -p "Enter firt number: " number1
read -p "Enter second number: " number2

if [ $number1 == $number2 ]
then
    echo "Both numbers are equal"
elif [ $number1 -gt $number2 ]
then
    echo "Between $number1 and $number2, $number1 is greater"
else
    echo "Between $number1 and $number2, $number2 is greater"
fi