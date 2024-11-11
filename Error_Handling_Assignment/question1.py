# Question 1: Division Calculator
numerator = int(input("Enter the numerator: "))
denominator = int(input("Enter the denominator: "))
try:
    result = numerator / denominator
    print("The result is:", result)
except ZeroDivisionError:
    print('Cannot divide by 0')
except ValueError:
    print('Enter a number instead')





