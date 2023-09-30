

# Parent Class 1
class Animal:
    def speak(self):
        pass

# Parent Class 2
class Bird:
    def chirp(self):
        pass

# Child Class inheriting from both Animal and Bird
class Parrot(Animal, Bird):
    def speak(self):
        return "Squawk!"

    def chirp(self):
        return "Chirp, chirp!"

# Create an instance of the Parrot class
parrot = Parrot()

# Call methods from both parent classes
print(parrot.speak())  # Output: Squawk!
print(parrot.chirp())  # Output: Chirp, chirp!





"""


We have two parent classes, Animal and Bird, each with their own methods (speak and chirp).

The Parrot class is a child class that inherits from both Animal and Bird. This means instances of Parrot can use methods from both parent classes.

The Parrot class overrides both the speak and chirp methods to provide its own implementations.

When we create an instance of the Parrot class (parrot) and call its methods, it can access and use methods from both parent classes due to multiple inheritance.

Multiple inheritance can be a powerful feature, but it can also lead to complexity and potential conflicts, 
especially when multiple parent classes define methods or attributes with the same name. In such cases,
 languages like Python provide a method resolution order (MRO) mechanism to determine which method to call
  when there are conflicts.

"""