import math

class Shape:
    def calculate_area(self):
        pass
    
    def calculate_perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.__radius = radius
    
    def calculate_area(self):
        if self.__radius > 0:
            return math.pi * (self.__radius ** 2)
        else:
            return 0
    
    def calculate_perimeter(self):
        if self.__radius > 0:
            return 2 * math.pi * self.__radius
        else:
            return 0

class Rectangle(Shape):
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
    
    def calculate_area(self):
        if self.__width > 0 and self.__height > 0:
            return self.__width * self.__height
        else:
            return 0
    
    def calculate_perimeter(self):
        if self.__width > 0 and self.__height > 0:
            return 2 * (self.__width + self.__height)
        else:
            return 0

circle = Circle(5)
print(circle.calculate_area())
print(circle.calculate_perimeter())

rectangle = Rectangle(10, 20)
print(rectangle.calculate_area())
print(rectangle.calculate_perimeter())