#function overloading
# function name is same , but parameters are different
#scope is same

# python does not allow function overloading
# it overwrites the initial function

def printDetails(param):
    print(f"Param = {param}")

def printDetails(param1,param2):
    print(f"Param1 = {param1} Param2 = {param2}")

#printDetails(10) # Error # type error
printDetails(5,4)