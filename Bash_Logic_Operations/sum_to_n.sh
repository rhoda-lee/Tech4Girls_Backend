#!/bin/bash

read -p "Enter a number to sum all numbers from 1 to that number: " n

sum=0
i=1

while [ $i -le $n ]
do
    sum=$((sum + i))
    i=$((i + 1))
done

echo "The sum of numbers from 1 to $n is: $sum"