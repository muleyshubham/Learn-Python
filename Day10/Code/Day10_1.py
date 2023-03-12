class Mobile:
    pass

m1=Mobile()
print(f"M1 = {m1} Type = {type(m1)}")
print(f"Dict = {m1.__dict__}")
setattr(m1,"Name","OnePlus")
setattr(m1,"Price",40000)
print(f"Dict = {m1.__dict__}")

#delete the attribute
delattr(m1,"Price")
print(f"Dict = {m1.__dict__}")