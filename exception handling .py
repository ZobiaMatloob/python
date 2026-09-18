# Exception handling helps us to handle the errors in the program and continue  the execution of the
#  program without any interruption.

# Example 1:
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

# Explanation: Dividing a number by 0 raises a ZeroDivisionError.
# The try block contains code that may fail and except block catches the error, printing a safe message
# instead of stopping the program

# Example 2 :
try:
    x = int(input("Enter a number: "))
    if x < 8:
        raise ValueError("Value must be greater than or equal to 8.")
    else:
        print("You entered:", x)
except ValueError as e:
    print("Error:", e)
