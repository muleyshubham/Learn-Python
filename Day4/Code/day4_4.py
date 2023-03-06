#local variables

def function1():
    num=45 # num is a variable declared inside the function body
    # num is a local variable
    print(f"Accessing the num value inside function1 = {num}")

function1()

print(f"Accessing the num value outside the function1 = {num}") #error
# num is not defined (unresolved reference to num)