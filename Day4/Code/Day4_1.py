#functions with default arguments
# while assigning default values to the function parameters
# it is compulsory to assign default values from right to left

def my_function(p1,p2,p3=222,p4=1111):
    print(f"P1 = {p1}")
    print(f"P2 = {p2}")
    print(f"P3 = {p3}")
    print(f"P4 = {p4}")

#my_function(10,5,3,20)
#my_function(1,2,3,4)


# my_function(100,200,300) # 100 200 300 1111
my_function(30,40) # 30 40 222 1111
my_function(9,8,7,6)