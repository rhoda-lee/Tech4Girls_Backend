#!/usr/bin/python3

'''
Write a script that:
Defines a tuple containing 5 different elements.
Uses indexing to print the first and last elements of the tuple.
Demonstrates the use of the count() and index() methods on the tuple.
Converts an integer to a float, a float to an integer, and a string representing a number to an integer.
Joins a list of strings into a single string using join().
Print the result of each example.
'''

my_tuple = ('Dede', 22, 'Antwiwaa', 20, 'Nabi', 22)

# print first element
first_element = my_tuple[0]
print(first_element)

# print last element
last_element = my_tuple[-1]
print(first_element)

# use .count()
count_element = my_tuple.count(22)
print(count_element)

# use .index
element_index = my_tuple.index('Nabi')
print(element_index)


# convert integer to float
number1 = 4
to_float = float(number1)
print(to_float)
print(type(to_float))


# convert float to integer
number2 = 3.5
to_int = int(number2)
print(to_int)
print(type(to_int))


# convert string to integer
number3 = '20'
str_to_int = int(number3)
print(str_to_int)
print(type(str_to_int))


# using .join()
my_list = ['I', 'am', 'a', 'cute', 'programmer']
my_string = " ".join(my_list)
print(my_string)
