#creating an empty class
class Person:
    """
    adding a doc string for the class person
    creating an empty class
    """
    pass

p1=Person()
print(f"P1 = {p1} Type = {type(p1)}")
print(p1.__doc__)
print(p1.__dict__)
print("-"*80)
setattr(p1,"name","Akshita")
print(p1.__dict__)
setattr(p1,"Organization","Sunbeam")
print(p1.__dict__)
print("-"*80)
p2=Person()
print(p2.__dict__)
setattr(p2,"name","Person2")
setattr(p2,"age",20)
print(p2.__dict__)



