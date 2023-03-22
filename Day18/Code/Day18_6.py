# if we write a function within a function , and outer function
# returns a reference of inner function
# it is called as closure
# it is also called as logger
# it is used as Decorators



def add(n1,n2):
    addition = n1+n2
    return addition

def subtract(n1,n2):
    subtraction = n1-n2
    return subtraction

def execute1(fn,n1,n2):  # fn is alias name given to a function
    print(f"fn = {fn.__name__}")
    print(f"N1 = {n1} N2 = {n2}")
    result = fn(n1,n2)  # add(n1,n2)   # subtract(n1,n2)
    print(f"Result = {result}")

#execute1(add,5,4)
#print("-"*80)
#execute1(subtract,8,4)


def execute2(fn):
    #inner function
    def inner_execute(n1,n2):
        print(f"N1 = {n1} N2 = {n2}")
        print(f"name of fn = {fn.__name__}")
        result = fn(n1,n2)
        print(f"Result {result}")
        return result
    return inner_execute

#value = execute2(add)
#value(25,15)



def logger(fn):
    #inner function
    def inner_execute(n1,n2):
        print(f"N1 = {n1} N2 = {n2}")
        print(f"name of fn = {fn.__name__}")
        result = fn(n1, n2)
        print(f"Result {result}")
        return result
    return inner_execute # returning reference of inner function

# @something ==> it is called as decorator

@logger
def add(n1,n2):
    addition=n1+n2
    return addition

@logger
def sub(n1,n2):
    subtraction = n1-n2
    return subtraction


print(add(10,5))
print("-"*80)
print(sub(20,15))