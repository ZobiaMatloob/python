# lists comprehension are used to create new lists from existing iterables in a concise and readable way. 

 # Example 1: Without list comprehension 

marks = [85, 90, 78, 92, 88]
new_marks = []
for x in marks :
    new_marks.append(x + 5)
    print(new_marks)

    # With list comprehension
marks = [85, 90, 78, 92, 88]
new_marks = [x + 5 for x in marks]
print(new_marks)

# Example 2: Without list comprehension
squares = []
for x in range(1, 6):
    squares.append(x ** 2)
print(squares)

# With list comprehension
squares = [x ** 2 for x in range(1, 6)]
print(squares)