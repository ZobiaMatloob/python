# del keyword in python is used to delete objects. It can be used to delete variables, lists, dictionaries, or any other object.
# Example 1: Deleting a variable
class student:
    def __init__(self, name):
        self.name = name

s = student("Alice")
print(s.name)  # Output: Alice
del s
print(s.name)  # Output: NameError: name 's' is not defined

# Example 2: Deleting an element from a list


class student:
    def __init__(self, name):
        self.name = name

list_of_students = [student("Alice"), student("Bob"), student("Charlie")]
print([s.name for s in list_of_students])  # Output: ['Alice', 'Bob', 'Charlie']

# Deleting an element from the list
del list_of_students[1]  # Deletes the student with name "Bob"
print([s.name for s in list_of_students])  # Output: ['Alice', 'Charlie']
