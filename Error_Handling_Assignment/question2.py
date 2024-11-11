# Question 2: Dictionary Lookup
data = {"name": "Alice", "age": 25, "country": "Wonderland"}
key = input("Enter the key you want to look up: ")
try:
    print("Value:", data[key])
except KeyError:
    print('This key does not exist')
