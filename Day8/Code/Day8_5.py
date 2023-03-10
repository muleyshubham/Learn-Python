def function1():
    print("Inside function1")

def function2():
    print("Inside function2")

def disp(param):
    print("Inside display function")
    print(f"Param {param} type = {type(param)}")

a1=function1
disp(a1)
a1=function2
disp(a1)