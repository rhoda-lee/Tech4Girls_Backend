class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    

    def area(self):
        '''method to calculate the area of the rectangle'''
        rect_area = self.length * self.width
        return f'The area of the rectangle is: {rect_area}'
    

    def perimeter(self):
        '''method to calculate the perimeter of the rectangle'''
        rect_perimeter = (2 * (self.length)) + (2 * (self.width))
        return f'The perimeter of the rectangle is: {rect_perimeter}\n'
    

    def __str__(self):
        '''Unofficial representation'''
        return f'Rectangle has a length of {self.length} and a width of {self.width}\n'
    

    def __eq__(self, instance):
        '''method to compare rectangles'''
        if isinstance(instance, Rectangle):
            return self.area() == instance.area()
        return False
    

# rectangle instance 1
rectangle1 = Rectangle(10, 6)
print(rectangle1.area())
print(rectangle1.perimeter())
print(rectangle1)

# rectangle instance 2
rectangle2 = Rectangle(20, 5)
print(rectangle2.area())
print(rectangle2.perimeter())
print(rectangle2)

# rectangle instance 3
rectangle3 = Rectangle(12, 5)
print(rectangle3.area())
print(rectangle3.perimeter())
print(rectangle3)


# Comparing rectangle areas that are unequal using __eq__
if rectangle1 == rectangle2:
    print(f'Rectangle1 and Rectangle2 have the same area')
else:
    print(f'Rectangle1 and Rectangle2 have different areas')


# Comparing rectangle areas that are equal using
if rectangle1 == rectangle3:
    print(f'Rectangle1 and Rectangle3 have the same area')
else:
    print(f'Rectangle1 and Rectangle3 have different areas')


