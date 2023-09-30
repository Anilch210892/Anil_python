

# Superclass (Parent Class)
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

# Subclass (Child Class)
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

# Create instances of the subclass
dog = Dog("Buddy")
cat = Cat("Whiskers")

# Call the speak method on subclass instances
print(dog.speak())  # Output: Buddy says Woof!
print(cat.speak())  # Output: Whiskers says Meow!

"""

In this example, we have a superclass Animal with a constructor that takes a name as an argument and
 a method speak that is meant to be overridden by subclasses. We then define two subclasses, Dog and Cat,
  that inherit from the Animal superclass. Each subclass overrides the speak method
   to provide its own implementation.
When we create instances of the Dog and Cat subclasses, 
they inherit the name attribute from the Animal superclass,
 and they provide their own implementation of the speak method. 
 This demonstrates the concept of inheritance, where the child

"""










