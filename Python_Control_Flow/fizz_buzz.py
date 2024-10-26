#!/usr/bin/python3

'''
Write a script that:
Loops through the numbers from 1 to 50.
Prints "Fizz" if the number is divisible by 3.
Prints "Buzz" if the number is divisible by 5.
Prints "FizzBuzz" if the number is divisible by both 3 and 5.
Otherwise, prints the number itself.
'''

for number in range(1, 51):
    if number % 3 == 0 and number % 5 == 0:
        print('FizzBuzz')
    elif number % 3 == 0:
        print('Fizz')
    elif number % 5 == 0:
        print('Buzz')
    else:
        print(number)