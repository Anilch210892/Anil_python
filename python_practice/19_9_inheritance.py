

# Parent Class (Superclass)
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

# Child Class (Subclass)
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

# Create instances of the Child Class
dog = Dog("Buddy")
cat = Cat("Whiskers")

# Call the speak method on Child Class instances
print(dog.speak())  # Output: Buddy says Woof!
print(cat.speak())  # Output: Whiskers says Meow!

"""

In this example:

The Animal class is the parent class, which has an __init__ constructor method 
to initialize the name attribute and a speak method (although it's defined as a stub method with pass).

Two child classes, Dog and Cat, inherit from the Animal class. 
These child classes override the speak method to provide their own implementations.

We create instances of the Dog and Cat classes (dog and cat),
 
 and each instance has access to the name attribute inherited from the Animal class.

When we call the speak method on these instances, the overridden method from the child class is invoked,
 providing different behaviors for each class.

Inheritance allows you to model the "is-a" relationship,
 where a subclass is a more specialized version of its superclass. 
 In this example, both Dog and Cat are animals,
  and they inherit common attributes and behaviors from 
  the Animal superclass while adding their own specific behaviors.




"""

