# we wish to modify global variable inside the function scope

num=88
print(f"Num in Global Area = {num}")

def test():
    print("Inside test function")
    #modify the global variable
    global num #it means consider num as a global value
    num=77
    print(f"Num in Test Function = {num}")
test()
print(f"Accessing num after function call = {num}")