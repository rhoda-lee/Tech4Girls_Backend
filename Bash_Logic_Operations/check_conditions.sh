#!/bin/bash

number1=$1
number2=$2

if [ $number1 -gt 10 ] && [ $number2 -gt 10 ]
then
    echo "Both numbers are greater than 10"
elif [ $number1 -gt 10 ] || [ $number2 -gt 10 ] 
then
    echo "At least one number is greater than 10"
else
    echo "Neither of the numbers is greater than 10"
fi