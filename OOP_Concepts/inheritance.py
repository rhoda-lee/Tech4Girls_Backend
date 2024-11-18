

class Employee:
    ''' Model an employee'''
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_details(self):
        return f'{self.name} holds the position of {self.position} at our company.\n'



# creating an instance of the cllass Employee
employee1 = Employee('Paul Nii Armah', 'Senior Software Engineer')
print(employee1.get_details())



class Manager(Employee):
    ''' Model of a child class, Manager that inherits from parent class, Employee'''
    def __init__(self, name, position, department):
        super().__init__(name, position)
        self.department = department

    def get_details(self):
        return f'{self.name} holds the position of {self.position} at the {self.department} department.\n'


# creating an instance of the cllass Manager
manager1 = Manager('Mark Attah Mensah', 'IT Officer', 'Finance')
print(manager1.get_details())