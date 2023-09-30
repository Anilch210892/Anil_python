class Student:
    def __init__(self, name, age):
        self.__name = name  # Private attribute
        self.__age = age    # Private attribute

    # Public methods to access and modify private attributes
    def get_name(self):
        return self.__name

    def set_name(self, name):
        if len(name) >= 2:
            self.__name = name
        else:
            print("Name must be at least 2 characters long.")

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age >= 0:
            self.__age = age
        else:
            print("Age cannot be negative.")

# Create an instance of the Student class
student = Student("Alice", 20)

# Access and modify private attributes using public methods
print(f"Name: {student.get_name()}")
print(f"Age: {student.get_age()}")

student.set_name("Bob"_)
student.set_age(25)

print(f"Updated Name: {student.get_name()}")
print(f"Updated Age: {student.get_age()}")
