
class Person:
    def __init__(self, name):
        self._name = name  # Protected variable (by convention)

# Creating an instance of the class
person = Person("Bob")

# Accessing a protected variable (by convention)
print(person._name)  # Output: Bob


"""
In this example, _name is a protected variable, but it can still be accessed from outside the class.
 However,
 it's considered a best practice not to access protected variables directly from outside the class.


"""