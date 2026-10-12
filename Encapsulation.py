# encapsulation is wraping data and methods into a single unit (class) and restricting access to some of the object's components.

class Employee:
    def __init__(self, name, salary):
        self.name = name          # public attribute
        self.__salary = salary    # private attribute

emp = Employee("Fedrick", 50000)
print(emp.name)       
# print(emp.__salary)  # This will raise an AttributeError

# there are three types of access modifiers in python:
# 1. Public (no underscore)
# 2. Protected (single underscore)
# 3. Private (double underscore)