
class MyClass:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print(f"{self.name} is being destroyed")

# Create an instance of the class
obj = MyClass("MyObject")

# Explicitly delete the object
del obj  # This calls the destructor

# Output: MyObject is being destroyed


"""
In this example, the __del__ method serves as a destructor. 
When we explicitly delete the object using del, it calls the destructor, which prints a message 
indicating that the object is being destroyed. Please note that in Python, destructors are not commonly used
 because Python's garbage collector
 automatically manages memory deallocation.


"""







