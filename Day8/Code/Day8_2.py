#Functional Programming
# reduces line of code
# clean code

#whenever we declare a function it is actually stored at some
#memory location (function body is reffered by one reference variable)
# which is nothing but name of the function


def demo():
    print("Inside the function1")

demo() # call the  function

print(f"Function1 = {demo} Type = {type(demo)}")


num1=50
print(f"Num1 = {num1} type {type(num1)} {id(num1)}")

num2=99
print(f"Num2 = {num2} type {type(num2)} {id(num2)}")

num2=888
print(f"Num2 = {num2} type {type(num2)} {id(num2)}")

# here num2 =99 it is a different object
# here num2 = 888 value is not getting overwritten rather
#it is creating one more new object num2



