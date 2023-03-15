#MathOperations module is having four function definitions
# when we import MathOperations module, all the four functions can be called
# if we wish to put a restriction on some function calls

# function1() can give a call to only add()

def function1():
    from MathOperations import add
    add(90,80)
    #sub(7,3) #unresolved reference
    #MathOperations.sub(70,50) # unresolved reference
    #mul(9,8) #unresolved reference
    #div(6,2) #unresolved reference

#function1()

def function2():
    from MathOperations import add,mul
    add(45,25)
    mul(3,2)
    #sub(9,3) #unresolved
    #div(10,2) # unresolved
function2()