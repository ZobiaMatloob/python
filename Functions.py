# Functions are defined using the 'def' keyword, followed by thefunction name and parentheses.
# Inside the parentheses, you can specify parameters that the function can accept.
# The function body is indented and contains the code that will be executed
#  when the function is called.

# Without functions - repetitive code:

temp1 = 80
celsius1 = (temp1 - 32) * 5 / 9
print(celsius1)

temp2 = 90
celsius2 = (temp2 - 32) * 5 / 9
print(celsius2)

temp3 = 50
celsius3 = (temp3 - 32) * 5 / 9
print(celsius3)

 # With functions - reusable code:

def fahrenheit_to_celsius(fahrenheit):
  return (fahrenheit - 32) * 5 / 9

print(fahrenheit_to_celsius(80))
print(fahrenheit_to_celsius(90))
print(fahrenheit_to_celsius(50))