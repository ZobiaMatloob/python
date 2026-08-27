# we have three types of operators no 1 is arithemetic operator.
#Arithmetic operators are used to perform basic mathematical operations like addition, 
#subtraction, multiplication and division.

#In Python, the division operator (/) returns a floating-point result, while floor division (//)
#returns an integer result.

a = 15
b = 4

print("Addition:", a + b)  

print("Subtraction:", a - b) 

print("Multiplication:", a * b)  

print("Division:", a / b) 

print("Floor Division:", a // b)  

print("Modulus:", a % b) 

print("Exponentiation:", a ** b)  

#Output
#Addition: 19
#Subtraction: 11
#Multiplication: 60
#Division: 3.75
#Floor Division: 3
#Modulus: 3
#Exponentiation: 50625

# Floor Division (//):Result: 3 Explanation: This operator divides the
#  left number by the right number and rounds the result down to the nearest whole integer.
#  Normal division of (15 / 4) gives (3.75). Floor division chops off the decimal part
#  to leave exactly

#Modulus (%):Result: 3 Explanation: This operator divides the left number by the right number
#  and returns only the remaining leftover value. Since (4) goes into (15) a total of (3) times
#  (4 \times 3 = 12), the remainder left over is (15 - 12 = 3)

#Exponentiation (**):Result: 50625Explanation: This operator raises the first number to the power
#  of the second number (a^{b}). It multiplies (15) by itself (4) times
#  ((15 \times 15 \times 15 \times 15 = 50625))

#Comparison Operators
#Comparison(or Relational) operators compares values. It either returns True or False
# according to the condition.


a = 13
b = 33

print(a > b)
print(a < b)
print(a == b)
print(a != b)#If a = 13 and b = 33, the expression print(a != b) will output
              #True because 13 is not equal to 33.
print(a <= b)

#Output
#False
#True
#False
#True
#False
#True

#Logical Operators
#Logical operators perform Logical AND, Logical OR and Logical NOT operations. It is used to combine conditional statements.

#The precedence of Logical Operators in Python is as follows:

#Logical not
#logical and
#logical or

a = True
b = False
print(a and b)
print(a or b)
print(not a)

#Output
#False
#True
#False

#The and operator returns True only if both conditions are true. If either condition is false,
#  the entire statement becomes False.

#The or operator returns True if at least one condition is true. It only returns False if both
# conditions are false

#not operator is a unary operator used to reverse or invert the Boolean result of a condition.