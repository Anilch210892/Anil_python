



class MyClass:
    class_variable = 0

    def __init__(self, value):
        self.value = value

    @classmethod
    def increment_class_variable(cls):
        cls.class_variable += 1

# Create instances of the class
obj1 = MyClass(10)
obj2 = MyClass(20)

# Call the class method to increment the class variable
MyClass.increment_class_variable()

# Access class variable through the class
print(MyClass.class_variable)  # Output: 1


"""
In this example,
increment_class_variable is a class method 
that increments the class_variable belonging to the MyClass class
""".
