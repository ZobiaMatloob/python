# Break statement is used to terminate the loop when a certain condition is met.
# The break statement can be used in both while and for loops. 
# When the break statement is executed, the loop will stop executing and control 
# will be transferred to the next statement after the loop.

#Example no 1:
for i in range(12):
    if(i == 10):
        break
    print("5 x", i+1, "=", 5 *(i+1))

 #Contine statement is used to skip the current iteration of the loop and move on
 # to the next iteration.
for i in range(12):
    if(i == 10):
        continue
    print("5 x", i+1, "=", 5 *(i+1))