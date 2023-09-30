


from abc import ABC, abstractmethod

# Abstract class (Shape)
class Shape(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

# Concrete class (Circle) implementing the abstract class
class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14159 * self.radius

# Concrete class (Rectangle) implementing the abstract class
class Rectangle(Shape):
    def __init__(self, name, width, height):
        super().__init__(name)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

# Create instances of concrete classes
circle = Circle("Circle", 5)
rectangle = Rectangle("Rectangle", 4, 6)

# Use the abstract interface to calculate area and perimeter
print(f"{circle.name} - Area: {circle.area()}, Perimeter: {circle.perimeter()}")
print(f"{rectangle.name} - Area: {rectangle.area()}, Perimeter: {rectangle.perimeter()}")
