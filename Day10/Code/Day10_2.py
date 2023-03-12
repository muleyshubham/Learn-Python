# demo of __init__()
# initializer (function defined inside the class)
# self means current object
# __init__() gets called automatically when we create object of the class


class Person:
    def __init__(self):
        print(f"Inside initializer {self}")

p1=Person()
# p1.__init__() is getting called
#internally it is treated as
# Person.__init__(p1) ===> self ===> p1
print(p1)
print(f"Contents of p1 = {p1.__dict__}")
p2=Person()
print(p2)
print(f"Contents of P2 = {p2.__dict__}")

