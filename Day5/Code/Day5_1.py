# lambda / Anonumous functions
# take two parameters and perform arithmetic operations

#def add(p1,p2):
    #print(f"Addition = {p1+p2}")


add = lambda p1,p2 : p1+p2
sub = lambda p1,p2 : p1-p2
mul = lambda p1,p2 : p1*p2
div = lambda p1,p2 : p1/p2

print(f"Addition = {add(5,5)}")
print(f"Subtraction = {sub(8,4)}")
print(f"Multiplication = {mul(9,8)}")
print(f"Division = {div(10,2)}")