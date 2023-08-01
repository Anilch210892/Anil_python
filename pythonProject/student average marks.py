"""
author anilkumar
problem statement:
finding average marks of student

"""
class Student:
    def __init__(self,name,chem,math,phy,bio,eng):
        self.name=name
        self.chem=chem
        self.math=math
        self.phy = phy
        self.bio = bio
        self.eng = eng
    def get_average(self):
        return (self.chem+self.math+self.phy+self.bio+self.eng)/5
    avinash=Student("avinash",95,92,89,90,87)
    raviteja=Student("raviteja",90,98,85,91,83)
    anil=Student("anil",96,93,89,90,82)
    vinay=Student("vinay",96,93,89,95,80)
    ramana=Student("ramana",90,93,85,92,88)
    obj _list=["avinash","raviteja","anil","vinay","ramana"]
    for obj in obj _list:
        print(f"student name is{obj.name}and his average is){obj.get_average()}")







