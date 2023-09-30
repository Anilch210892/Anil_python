


class Person:
    def __init__(self, name):
        self.__name = name  # Private variable

    def get_name(self):
        return self.__name

# Creating an instance of the class
person = Person("Charlie")

# Accessing a private variable using a getter method
print(person.get_name())  # Output: Charlie

# Attempting to access a private variable directly (throws an error)
# print(person.__name)  # This would raise an AttributeError


"""

In this example, __name is a private variable of the Person class, 
and it cannot be accessed directly from outside the class. Instead,
 a getter method (get_name) is provided to access the private variable's value.

Please note that in Python, even though private variables are not enforced by 
the language itself, they are still accessible with name mangling (_ClassName__variableName). 
However, it's considered a strong convention not to do so, and private variables are meant to be treated as non-public.
 Other programming languages may have stronger access control mechanisms.

"""