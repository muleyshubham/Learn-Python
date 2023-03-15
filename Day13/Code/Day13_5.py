#importing a module in global area
# so we can use the functions from module
# in the whole file anywhere

import MathOperations as m # m is an alias (another name)

def function1():
    m.add(170,115)
    m.sub(28,24)
    m.mul(50,20)
    m.div(28,4)

function1()
print("-"*80)

def function2():
    m.mul(800,4)
    m.div(60,5)

function2()
