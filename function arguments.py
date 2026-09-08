# Example 1: Required Arguments are those that are passed to a function in the correct positional order.
def greet(name, age):print(f"Hello, {name}! You are {age} years old.")

greet("Alice", 30)  # Both arguments are provided in the correct order
# greet("Alice")  # This would raise a TypeError because the 'age' argument is missing


# Example 2 : Default Arguments are those that take a default value if no value is provided in the function call for that argument.
def greet(name, age=25):  # 'age' has a default value of 25
    print(f"Hello, {name}! You are {age} years old.")

greet("Alice")  # Uses the default value for 'age'
greet("Bob", 30)  # Provides a value for 'age'

#Example 3:Keyword Arguments are those that can be given in any order,as long as you specify the name of the parameter when calling 
# the function.
def average(a, b, c= 1):# c has a default value of 1
    print(f"The average is {(a + b + c) / 2}")
average(b= 10, a= 20) # c will take the default value of 1

# Example 4: Variable-length Arguments are those that allow you to pass a variable number of arguments to a function.
def average(*numbers):  # The asterisk (*) allows for variable-length arguments
    sum = 0
    for i in numbers:
        sum = sum + i
    print(f"The average is {sum / len(numbers)}")
average(10, 20)  # Passes two arguments