#defining a function and calling the function
#docstring : describes about the function
# RULE : it must be specified immediately after the
# first line of the function


#Function definition
def function1():
    print("Inside the function1")
    print("this is function introduction")
    print("-"*70)

#function1() #function call

def test():
    """
    this is test function docstring,having two print statement
    :return: no this function is not returning anything
    """
    print("inside test function")
    print("this is my second function")

test() #function call
print("Fetching the docstring of the test function ")
print(test.__doc__)
print("-"*70)

print(print.__doc__)








