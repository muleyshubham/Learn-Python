#example inner function

def function1():
    n1=input("Enter first number")
    n2=input("Enter second number")
    n1=int(n1)
    n2=int(n2)

    addition = n1 - n2  # wrong logic
    print(f"Addition = {addition}")
#function1()

def function2():
    n1=input("Enter first number")
    n2=input("Enter second number")
    n1=int(n1)
    n2=int(n2)

    addition = n1 +n2
    print(f"Addition = {addition}")
#function2()

# log lines (logs)
def add(n1,n2):
    print(f"N1 = {n1} N2 = {n2}")
    addition = n1+n2
    print(f"Return Value = {addition}")
    return addition

def function3():
    n1=int(input("Enter first number"))
    n2 =int(input("Enter Second number"))
    result = add(n1,n2)
    print(f"Result = {result}")
function3()