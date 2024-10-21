#!/bin/bash

number1=$1
number2=$2
number3=$3

#Sum first two numbers
sum=$((number1 + number2))

product=$((sum * number3))

echo "The sum of $number1 and $number2 is: $sum"
echo "The product of $sum and $number3 is: $product"



