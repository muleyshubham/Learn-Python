# named functions (defined using def keyword)
# the functions which are given a name

#unnamed / anonymous functions / lambda functions (use lambda)
# the functions which are not having given a name

#Syntax:
# lambda arguments : expression

def sqaure(number):
    return number*number

print(f"Sqaure of 4 is {sqaure(4)}")

#get the sqaure of a function using lambda
answer = lambda num : num * num
print(f"Result = {answer(2)}")