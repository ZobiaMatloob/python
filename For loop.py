 # For loops are used to iterate over a sequence (like a list, tuple, dictionary, set, or string).

# Example 1: Iterating through a list
countries = ["Pakistan", "Palestine", "Turkey", "Iran"]
for  country in countries:
 print(country)

 # Example 2: Iterating through a string
for letter in "PAKISTAN":
 print(letter)

 # Example 3: Using the range() function to iterate through a sequence of numbers
for number in range(5):
    print(number)
    
 # Example 4: Using the range() function with a start and end value
for number in range(0, 7):
    print(number)

# Example 5: Using the range() function with a start, end, and step value. for the numbers 0 to 10, it start with 0
# and goes up to 10, but the third number is 2 there will be an increment of 2 after every number so this will 
# print even numbers from 0 to 10 like(0, 2, 4, 6, 8).
for number in range(0, 10, 2):
    print(number)