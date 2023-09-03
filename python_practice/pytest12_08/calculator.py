


class Caliculator:
    def __init__(self,operation,value_1,value_2):
        self.operation = operation
        self.value_1 = value_1
        self.value_2 = value_2
    def caliculate_result(self):
        if self.operation == "add":
            return self.value_1+self.value_2
        elif self.operation == "subtraction":
            return self.value_1-self.value_2
        elif self.operation == "multiplication":
            return self.value_1*self.value_2
        elif self.operation == "division":
            if self.value_2==0:
                return "invalid division"
            else:
                return self.value_1/self.value_2
        else:
            return "invalid operation"



