# requirement is to call the functions add() and sub()
# from the file Day13_1

#first way is to import the entire Module

def function1():
    import Day13_1 # imported the module Day13_1
    Day13_1.add(80,30)
    Day13_1.sub(70,40)

print(f"Module name = {__name__}")
function1()

#as soon as we are importing a Module then
# the whole Module is also getting executed
# problem is whenever we are executing any file
#and if we have imported any specific module
#the module should not get executed completely


