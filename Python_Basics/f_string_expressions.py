#!/usr/bin/python3

'''

 Create a Python file named `f_string_expressions.py`.
 Write a script that defines two variables, `a = 10` and `b = 20`.
 Use an fstring to print a message showing the sum, difference, and product of `a` and `b`.
 Save your script and push it to the `Python_Basics` directory.

'''

a = 10
b = 20

sum = a + b
difference = a - b
product = a * b

arithmetic = f'The sum, difference and product of a and b are: {sum}, {difference} and {product} respectively.'
print(arithmetic)