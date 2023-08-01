"""
Author anilkumar
problem statement:
Inheritance of scenario 1
here we are taking 2 classes siddu and vijaya and anil as subclass,taking anil priority of food
"""

class Siddu:
    def eat(self):
        print("eat rice")
class Vijaya:
    def eat(self):
        print("eat biryani")
class Anil(Siddu,Vijaya):
    def eat(self):
        print("eat sweet")
anil=Anil()
anil.eat()