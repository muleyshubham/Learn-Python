# if we just specify *args
# we can not go for positional parameter passing

def add(*args):
    result=sum(args)
    print(f"result = {result}")

#add(3,2)
#add(p1=50,p2=30) # TypeError

#Solution is kwargs
# args is tuple of input arguments
# kwargs dictionary of input values

def print_data(*args,**kwargs):
    print(f"Args = {args}")
    print(f"Kwargs = {kwargs}")

#print_data(45,25)
#print("-"*80)
#print_data(p1=50,p2=30)


def calc(*args,**kwargs):
    print(f"Args = {args}")
    print(f"Sum = {sum(args)}")
    print(f"Kwargs = {kwargs}")

calc(45,25)
print("-"*80)
calc(p1=50,p2=30)

