#importing a module with an alias name

def function1():
    import MathOperations as m # m is an alias (another name)
    m.add(170,115)
    m.sub(28,24)
    m.mul(50,20)
    m.div(28,4)

function1()
print("-"*80)

def function2():
    import MathOperations as m
    m.mul(800,4)
    m.div(60,5)

function2()
