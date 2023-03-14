#variable argument concept
def test(param):
    print(f"Param = {param}")

#test(10) # OK
#test(20,30) # TypeError

def demo(*args):
    print(f"args = {args}")

#demo(10)  # OK
#demo(25,15)  #OK
#demo(5,4,3)  #OK
#demo() #OK
#demo(9,8,7,5) #OK

def add(*args):
    print(f"Args = {args}")
    result = sum(args)
    print(f"Addition = {result}")

add(5,2)
add(9,3,5)
add(10,20)
add(10,20,15,25)


