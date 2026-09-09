# Parameters in Python are the variable names listed inside the parentheses () when you define a function.
# Think of a parameter as a named storage box created inside the function definition. 
# It has no value until someone runs the function and drops an object (an argument) inside it.

# Example 1 :
# 1. Defining the Function (with Parameters)
def greet_user(username):  # 'username' is the PARAMETER
    print(f"Hello, {username}!")

greet_user("Alice")     # Calling the Function (with Arguments)
                             # "Alice" is the ARGUMENT passed to the 'username' parameter

# Example 2 :
# 1. Defining the Function (with Multiple Parameters)
def greet_user(username, age):  # 'username' and 'age' are the PARAMETERS
    print(f"Hello, {username}! You are {age} years old.")

greet_user("Bob", 25)  # Calling the Function (with Arguments)
                        # "Bob" is the ARGUMENT passed to the 'username' parameter
                        # 25 is the ARGUMENT passed to the 'age' parameter