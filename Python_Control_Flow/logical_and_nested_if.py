#!/usr/bin/python3

'''
Write a script that defines two boolean variables: is_student and is_employed.
Use and, or, and not to print messages based on the conditions:
If is_student and is_employed are both True, print "You are a working student."
If is_student is True but is_employed is False, print "You are a student."
If not is_student and is_employed, print "You are employed but not a student."
'''

is_student = True
is_employed = True

if is_student:

    if is_employed:
        print('You are a working student')
    else:
        print('You are a student')

elif not is_student and is_employed:
    print('You are employed but not a student')

else:
    print('You are neither a student nor employed')




'''
Write a nested if statement that:
Asks the user for their age.
Checks if the age is greater than or equal to 18.
If it is, ask if they have a driver's license.
Print "You are allowed to drive." if they do.
Print "You need a driver's license to drive." if they don’t.
If the age is less than 18, print "You are not old enough to drive."
'''

age = int(input('Enter your age: '))

if age >= 18:

    print('Select the option (A or B) associated with your answer.')
    print('A. Yes')
    print('B. No')

    license_status = input('Do you have a driver\'s licence? ')

    if license_status == 'A'.lower():
        print('You are allowed to drive.')
    else:
        print('You need a driver\'s licence to drive.')

else:
    print('You are not old enough to drive.')
