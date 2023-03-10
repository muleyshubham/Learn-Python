#Function Alias / Giving another name to the function

def test():
    print("inside test function")


test() #function call
print(f"test = {test} type = {type(test)} id = {id(test)}")

my_function = test # function alias
print(f"my_function = {my_function} type ={type(my_function)} id = {id(my_function)}")

print("-"*80)
#call test function
test()
#call test function indirectly
# we need function alias
my_function()
