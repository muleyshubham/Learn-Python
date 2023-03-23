# logger
def logger(function):
    def inner_execute(*args,**kwargs):
        print("Inside Closure inner function ")
        print(f"Args = {args} KWARGS = {kwargs}")
        print(f"Name = {function.__name__}")
        result = function(*args,**kwargs)
        print(f"Result inside closure function = {result}")
        return result
    # returning inner function reference
    return inner_execute


@logger
def add(n1,n2):
    return n1+n2

@logger
def square(n):
    return n*n

def hello_funtion():
    print("Hello everyone")

print(add(20,15))
print("-"*80)
print(square(4))
print("-"*80)
hello_funtion()