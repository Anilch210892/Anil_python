
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says Woof!")

    def celebrate_birthday(self):
        self.age += 1
        print(f"{self.name} is now {self.age} years old!")

# Create instances of the Dog class
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 2)

# Call non-static methods on instances
dog1.bark()  # Output: Buddy says Woof!

# Celebrate birthdays
dog1.celebrate_birthday()  # Output: Buddy is now 4 years old!
dog2.celebrate_birthday()  # Output: Max is now 3 years old!

"""
In this example, bark and celebrate_birthday are non-static methods of the Dog class. 
    They are called on specific instances (dog1 and dog2)
    and operate on the instance's attributes (name and age).' 
    The self parameter in these methods allows them to access and modify the instance's data.
"""