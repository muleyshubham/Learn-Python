
num=65 # global variable
def my_function():
    #print(f"Access the global variable inside function {num}") #error
    num=99 #local
    print(f"Updated value of num = {num}")

my_function()
print(f"Value of num outside the function {num}")
