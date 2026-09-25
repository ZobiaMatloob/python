# A constructor is used to initializethe object of a class.
# A constructor is a unique function that gets called automatically when an object is created of a class.

 # Example
class person:
    def __init__(self, name, occ):
        self.name = name
        self.occ = occ
        print("hi i am a human")

    def info(self):
        print(f"{self.name} is a {self.occ}")


a = person("mariam","developer")
b = person("jake","artist")
a.info()
b.info()
   