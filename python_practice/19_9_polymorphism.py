
# Parent Class (Superclass)
class Animal:
    def speak(self):
        pass

# Child Class 1 (Subclass)
class Dog(Animal):
    def speak(self):
        return "Woof!"

# Child Class 2 (Subclass)
class Cat(Animal):
    def speak(self):
        return "Meow!"

# Function to make an animal speak
def make_animal_speak(animal):
    return animal.speak()

# Create instances of the child classes
dog = Dog()
cat = Cat()

# Call the make_animal_speak function with different objects
print(make_animal_speak(dog))  # Output: Woof!
print(make_animal_speak(cat))  # Output: Meow!
