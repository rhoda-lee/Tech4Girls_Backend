#!/usr/bin/python3

'''
Write a script that defines two variables, x and y, with any values.
Use +, -, *, /, //, **, and % to perform calculations between x and y.
Compare x and y using ==, !=, <, >, <=, and >=.
Print the result of each calculation and comparison using f-strings.
'''

# declaring variables
x = 10
y = 4


# Arithmetics

# addition
sum = x + y
print(f'The sum of {x} and {y} is {sum}')

# subtractio
diff = x - y
print(f'The difference of {x} and {y} is {diff}')

# multiplication
product = x * y
print(f'The product of {x} and {y} is {product}')

# division
division = x / y
print(f'The division of {x} by {y} is {division}')

# floor division
floor_division = x // y
print(f'The floor division of {x} by {y} is {floor_division}')

# exponent
exp = x ** y
print(f'{x} exponent {y} is {exp}')

# modulos
mod = x % y
print(f'The modulos of {x} by {y} is {mod}')



# Comparison

# using equality operator '=='
result1 = x == 4
print(f'{x} == {y} is {result1}')

# using inequality operator '!='
result2 = x != 4
print(f'{x} != {y} is {result2}')

# using less than operator '<'
result3 = x < 4
print(f'{x} < {y} is {result3}')

# using greater than operator '>'
result4 = x > 4
print(f'{x} > {y} is {result4}')

# using less than or equal operator '<='
result5 = x <= 4
print(f'{x} <= {y} is {result5}')

# using greater than or equal operator '>='
result6 = x >= 4
print(f'{x} >= {y} is {result6}')



