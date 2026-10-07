class Student:
    college_name = "abc college"
    def __init__(self, name , marks ,grade):
        self.name = name
        self.marks = marks
        self.grade = grade 
        print("adding new student in database")


# creating object
s1 = Student("joe",78,"B")
print(s1.name,s1.marks)

print(s1.college_name) # accessing class attribute using object


class student:
    institute_name = "Oxford University"
    def __init__(self, name):
        self.name = name

        # creating object
s1 = student("Bill Clinton")
print(s1.name)
print(s1.institute_name)

s2 = student("Imran Khan")
print(s2.name)
print(s2.institute_name)

s3 = student("Tony Blair")
print(s3.name)
print(s3.institute_name)
