#!/usr/bin/python3

'''
Write a script that asks the user for their age and:
Prints "You are a minor." if the age is less than 18.
Prints "You are an adult." if the age is between 18 and 64.
Prints "You are a senior." if the age is 65 or older.
'''

# Take user input
age = int(input('Enter your age: '))

if age < 18:
    print('You are a minor.')
elif age >= 18 and age <= 64:
    print('You are an adult.')
else:
    print('You are a senior.')