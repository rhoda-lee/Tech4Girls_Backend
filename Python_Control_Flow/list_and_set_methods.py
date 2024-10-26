#!/usr/bin/python3

'''
Write a script that demonstrates the following list methods: 
append(), remove(), pop(), sort(), reverse(), and extend().

Write a script demonstrating the use of the following set methods: 
add(), remove(), union(), intersection(), difference().

Use lists and sets with at least 5 and 4 elements respectively.
'''

# Created a list for the task
my_list = ['This', 'is', 'a', 'random', 'list']

# .append()
my_list.append('data type')
print(my_list)


# .remove()
my_list.remove('list')
print(my_list)


# .pop()
my_list.pop()
print(my_list)


# .sort()
my_second_list = [23, 19, 17, 13, 11, 7, 5, 3]
my_second_list.sort()
print(my_second_list)


# .reverse()
my_second_list.reverse()
print(my_second_list)


# .extend()
my_list.extend(my_second_list)
print(my_list)




# Set Methods
my_set1 = {'Rhoda', 'Joan', 'Danielle', 'Dede', 'Nabi'}
my_set2 = {'Dede', 'Michaela', 'Nabi', 'Nana Akua'}


# .add()
my_set1.add('Adwoa')
print(my_set1)


# .remove()
my_set1.remove('Danielle')
print(my_set1)


# .union()
union_set = my_set1.union(my_set2)
print(union_set)


# .intersection()
inter_set = my_set1.intersection(my_set2)
print(inter_set)


# .difference()
diff_set = my_set1.difference(my_set2)
print(diff_set)
