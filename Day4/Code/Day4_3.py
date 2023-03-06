
#function with return value
def add(p1:int,p2:int):
    """
    function with return value
    """
    print(f"P1 = {p1} P2 = {p2}")  #p1 = 15  p2 = 12
    return p1+p2  #return 15+12   # return 27


print("-"*80)
result = add(15,12) #function call  # result will hold the value 27
# result is the locator
print(f"Result = {result}")
print("-"*80)
print(add(90,80))  #print(170)
print("-"*80)
print(f"Addition of two numbers = {add(25,22)}")

