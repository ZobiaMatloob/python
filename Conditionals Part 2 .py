# The elif keyword is Python's way of saying "if the previous conditions were 
# not true, then try this condition"

#Example 1
score = 75

if score >= 90:
  print("Grade: A")
elif score >= 80:
  print("Grade: B")
elif score >= 70:
  print("Grade: C")
elif score >= 60:
  print("Grade: D")

  #Use elif when you have multiple mutually exclusive conditions to check. 
  # This is more efficient than using multiple separate if statements because
  # Python stops checking once it finds a true condition.

  #Example 2:
age = 25
if age < 13:
      print("You are a child.")
elif age < 20:
      print("You are a teenager.")
else:
      print("You are an adult.")

  #Example 3: 
country = "pakistan"
if country == "pakistan":
    print("You are from Pakistan.")
elif country == "india":
    print("You are from japan.")
else:
    print("You are from another country.")