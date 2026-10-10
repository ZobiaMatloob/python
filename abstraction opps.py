# Abstraction is hiding unnecessary details from the user and showing only essential features of an object.
#  It helps to reduce complexity and allows the programmer to focus on interactions at a higher level.

# Example of abstraction in python is shown below:

class car():

    def __init__(self):
        self.acc = False
        self.brk = False
        self.cluch = False


    def start(self):
        self.acc = True
        self.brk = True
        print("Car is started")

car1 = car()
car1.start()

# Example 2 :
# 1. The Abstraction (The visible switch on the wall)
class Switch():

    def flip(self):
        pass

# 2. The Implementation (The hidden wires behind the wall)
class LightSwitch(Switch):
    def flip(self):
        return " Wires connect -> Electricity flows -> Light turns ON!"

# --- Using it ---
my_switch = LightSwitch()
print(my_switch.flip())

     

