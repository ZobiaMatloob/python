# Magic methods are special methods whose names start and end with double underscores,
# like __init__() and __str__(). Because of the double underscores,
#  they are also called dunder methods (short for "double underscore").

# Example 1 :

class employe:
    name = "leo"

    def __len__(self):
        i = 0
        for v in self.name:
            i = i + 1
        return i


e = employe()
print(e.name)
print(len(e))

# Example 2

class country:
    nation = "pakistan"

    def __len__(self):
        i = 0
        for h in self.nation:
            i = i + 1
        return i


p = country()
print(p.nation)
print(len(p))