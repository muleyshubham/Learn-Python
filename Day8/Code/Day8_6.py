def add(p1,p2):
    print(f"P1 = {p1} P2 = {p2} Addition = {p1+p2}")

def sub(p1,p2):
    print(f"P1 = {p1} P2 = {p2} Subtraction = {p1-p2}")

def execute(param):
    print(f"Inside Execute function")
    print(f"Param = {param} Type = {type(param)}")
    param(30,20)

execute(add)
execute(sub)




