

class Animal:
    kingdom="Animal kingdom"
    life=True
    @staticmethod
    def has_life():
        print("it has life")
        return True
    def __init__(self,animal_name,legs):
        self.animal_name=animal_name
        self.legs=legs
    def show_animal_info(self):
        print(f"animal name is {self.animal_name} and legs is {self.legs}")

dog=Animal("dog",4)
parrot=Animal("parrot",4)
animal_has_life()



