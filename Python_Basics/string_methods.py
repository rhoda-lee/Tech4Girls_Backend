'''

Create a Python file named `string_methods.py`. Write a script that demonstrates the following string methods:
`upper()`
`lower()`
`replace()`
`join()`
 For each method, provide an example and print the result. Save your script and push it to the `Python_Basics` directory.


'''
my_string = "I am a cute programmer and these are my hobbies:"
hobbies = ['Reading,', 'Writing,', 'Coding and', 'Sleeping']

print(my_string)

to_upper = my_string.upper()
print(to_upper)

to_lower = my_string.lower()
print(to_lower)

text_replace = my_string.replace('I am', 'You are')
print(text_replace)

my_hobbies = ' '.join(hobbies)
print(my_hobbies)

