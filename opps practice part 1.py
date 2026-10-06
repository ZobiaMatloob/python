# class is the blueprint for creating objects
# Example 1:

# creating classes by init(constructor) function
# parameterized constructor

class Student:
    def __init__(self, name , marks ,grade):
        self.name = name
        self.marks = marks
        self.grade = grade 
        print("adding new student in database")


# creating object
s1 = Student("joe",78,"B")
print(s1.name,s1.marks)

# default constructor example
# def __init__(self):
#     pass

# Example no 2:
# creating classes 
class Cars:
    color = "blue"
    brand = "toyota"


car1 = Cars()
print(car1.color)
print(car1.brand)

# Example no 3:
class Animals:
    dangerous = "lion"
    cute = "cat"


animal1 = Animals()
print(animal1.dangerous)
print(animal1.cute)





 





