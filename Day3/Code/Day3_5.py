# function with parameters
# function not returning any value
def add(n1,n2):
    """
    adding two numbers
    :param n1:
    :param n2:
    :return: nothing
    """
    print(f"Type of N1 = {type(n1)} Type of N2 = {type(n2)}")
    print(f"N1 = {n1} N2 = {n2} Result = {n1+n2}")

add(25,15)
print("-"*80)
add(4.5,2.5)
print("-"*80)
print(add.__doc__)


def test(n1,n2,n3):
    print(f"Addition = {n1+n2+n3}")
test(5,4,3)
test(3,15,12)



