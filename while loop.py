# while loop remains true as long as the condition remains true. 
# It will keep executing the block of code inside it until the condition becomes false.

#Example no 1:
name = input("Enter your name: ")
while name == "":
    name = input("Enter your name: ")
print("Hello, " + name + "!")


#Example no 2:
num = int(input("Enter a number: "))
while num < 1 or num > 10:
    num = int(input("Enter a number between 1 and 10: "))
print(f"You entered {num}.")


#Example no 3:
count = 0
while count < 5:
    print("Count is:", count)
    count += 1