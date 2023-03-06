#outer and inner function
def math_operations(p1,p2): # math_operations() outer function
    print(f"P1 = {p1} P2 ={p2}")
    def add():  #add() inner function
        return p1+p2
    def sub(): #sub() inner function
        return p1-p2
    def mul(): #mul() inner function
        return p1*p2
    def div(): #div() inner function
        return p1/p2

    print(f"Addition = {add()}")
    print(f"Subtraction = {sub()}")
    print(f"Multiplication = {mul()}")
    print(f"Division = {div()}")

math_operations(60,2)
#add() # not allowed