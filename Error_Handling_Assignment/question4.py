# Question 4: List Index Access
items = ["apple", "banana", "cherry"]
try:
    index = int(input("Enter the index of the item you want to access: "))
    print("You selected:", items[index])
except IndexError:
    print('Index out of range. Enter a number from 0-2')
except ValueError:
    print('Enter a number from 0-2')
