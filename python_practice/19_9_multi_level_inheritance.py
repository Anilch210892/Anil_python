



# Grandparent Class
class Animal:
    def speak(self):
        pass

# Parent Class (inherits from Animal)
class Bird(Animal):
    def chirp(self):
        return "Chirp, chirp!"

# Child Class (inherits from Bird)
class Parrot(Bird):
    def speak(self):
        return "Squawk!"

# Create an instance of the Parrot class
parrot = Parrot()

# Call methods from all levels of the inheritance chain
print(parrot.speak())  # Output: Squawk!
print(parrot.chirp())  # Output: Chirp, chirp!


"""


The Animal class is the grandparent class, which defines a method speak. 
It serves as the base class in the multilevel inheritance hierarchy.

The Bird class is the parent class, which inherits from Animal and adds its own method chirp.

The Parrot class is the child class, which inherits from Bird and overrides the speak method to
 provide its own implementation.

When we create an instance of the Parrot class (parrot) and call its methods,
 it can access methods from all levels of the inheritance chain, allowing it to speak and chirp.

Multilevel inheritance allows for a hierarchical organization of classes, 
where each level of the hierarchy can introduce new attributes and behaviors while still inheriting from the previous level. It provides a way to create specialized classes that build upon the functionality of their parent classes.

"""








