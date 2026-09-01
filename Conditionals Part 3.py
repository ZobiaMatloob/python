# Nested if statements are used when you want to check for multiple conditions that depend on each other
# . Here's an example of how to use nested if statements in Python:
#Example 1:

temperature = 25
is_sunny = True

if temperature > 20:
  if is_sunny:
    print("Perfect beach weather!")

 #Example 2:
age = 70
is_employee = True

if age >= 60:
    if is_employee:
        print("30% employee discount!")
    else:
        print("20% employee discount.")
else:
    print("Not eligible for a senior discount.")


 #Example 3:
score = 85
if score >= 80:
    if score >= 90:
        print("Excellent! You got an A.")
    else:
        print("Good job! You got a B.")
else:
    print("Keep studying. You can do better.")