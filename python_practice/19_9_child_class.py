

# Parent Class (Superclass)
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start_engine(self):
        print(f"{self.make} {self.model}'s engine started.")

# Child Class (Subclass)
class Car(Vehicle):
    def __init__(self, make, model, num_doors):
        # Call the parent class constructor using super()
        super().__init__(make, model)
        self.num_doors = num_doors

    def honk_horn(self):
        print(f"{self.make} {self.model} honks the horn!")

# Create an instance of the Car class (Child Class)
my_car = Car("Toyota", "Camry", 4)

# Access attributes and methods of the Child Class
print(f"Make: {my_car.make}")
print(f"Model: {my_car.model}")
print(f"Number of Doors: {my_car.num_doors}")

# Call methods from the Parent Class
my_car.start_engine()  # Output: Toyota Camry's engine started.

# Call methods unique to the Child Class
my_car.honk_horn()  # Output: Toyota Camry honks the horn!



"""
In this example, we have a parent class Vehicle with attributes make and model and a method start_engine.
 The child class Car inherits from Vehicle and adds its own attribute num_doors and method honk_horn.

When we create an instance of the Car class (my_car), it inherits the make and model attributes and
 the start_engine method from the parent class Vehicle. Additionally, it has its own attributes and methods. 
This is a common example of using inheritance to create a more specialized class based on a more general one.


"""





