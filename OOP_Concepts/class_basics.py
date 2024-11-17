class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        return f'The {self.make} {self.model} was released in the year {self.year}'
    
new_car = Car('Toyota', 'Camry', '2020')
print(new_car.display_info())