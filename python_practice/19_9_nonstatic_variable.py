



class Circle:
    pi = 3.14159  # Static variable shared by all instances

    def __init__(self, radius):
        self.radius = radius  # Instance variable specific to each instance

    def calculate_area(self):
        return self.pi * (self.radius ** 2)

# Create instances of the Circle class
circle1 = Circle(5)
circle2 = Circle(3)

# Access the static variable (class variable) using the class name
print(Circle.pi)  # Output: 3.14159

# Access the instance variable using instances
print(circle1.radius)  # Output: 5
print(circle2.radius)  # Output: 3

# Calculate the area using the instance method
area1 = circle1.calculate_area()
area2 = circle2.calculate_area()
print(area1)  # Output: 78.53975
print(area2)  # Output: 28.27431

"""In this example, pi is a static variable (class variable) that is shared among all instances of the Circle class. It's accessed using the class name (Circle.pi), and its value is consistent across all instances.
 The radius variable is an instance variable specific to each instance of the class."""




