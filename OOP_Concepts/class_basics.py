class Car:
    '''modeling a representation of a car'''
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        '''Method to display car information'''
        return f'The {self.make} {self.model} was released in the year {self.year}'


# Creating an instance of the class Car
new_car = Car('Toyota', 'Camry', '2020')

# calling diplay_info() method on instance
print(new_car.display_info())