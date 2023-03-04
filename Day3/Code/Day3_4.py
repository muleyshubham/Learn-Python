#function with one parameter
# function was not returning any value

def demo(param):
    """
    this is demo of function with one parameter
    """
    print("Inside Demo function")
    print(f"Parameter Value = {param} Type = {type(param)}")

#demo() #ERROR #TypeError # missing 1 argument
demo(25)  #Function call # 25 is called as Actual argument
print("-"*80)
demo(8.7) #Function call
print("-"*80)
demo('Sunbeam') #Function call
print("-"*80)
demo(True)  #Function call
