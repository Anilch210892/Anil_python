

class MathUtility:
    @staticmethod
    def add(x, y):
        return x + y

# Call the static method without creating an instance of the class
result = MathUtility.add(5, 3)
print(result)  # Output: 8


"""
In this example, the add method is a static method defined within the MathUtility class.
 It can be called directly on the class without creating an instance of the class.

"""