# __init__(self) is called as DEFAULT INITIALIZER
# in this example init() is having three attributes
# so whenever any object is created it will be allocated with
# these three attributes


class Person:
    def __init__(self):
        print(f"Inside Intializer {self}")
        setattr(self,'name','')
        setattr(self,'age','')
        setattr(self,'address','')


p1=Person()
print(f"p1 = {p1.__dict__}")
setattr(p1,'name','akshita')
setattr(p1,'age','36')
setattr(p1,'address','pune')
print(f"p1 = {p1.__dict__}")
print("-"*80)
p2=Person()
print(f"p2 = {p2.__dict__}")
setattr(p2,'name','person2')
setattr(p2,'age','28')
setattr(p2,'address','mumbai')
setattr(p2,'email',"abc@gmail.com")
print(f"p2 = {p2.__dict__}")