#list comprehension normally is used in place of map or filter

def function1():
    numbers=[1,2,3,4,5,6,7,8,9,10]
    even_numbers= list(map(lambda n : n%2 == 0 ,numbers))
    print(numbers)
    print(even_numbers)
#function1()


def function2():
    numbers=[1,2,3,4,5,6,7,8,9,10]
    even_numbers= list(filter(lambda n : n%2 == 0 ,numbers))
    odd_numbers = list(filter(lambda n: n % 2 != 0, numbers))
    print(numbers)
    print(even_numbers)
    print(odd_numbers)
#function2()
def function3():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even_numbers=[val for val in numbers if val%2 == 0]
    odd_numbers = [val for val in numbers if val % 2 != 0]
    print(numbers)
    print(even_numbers)
    print(odd_numbers)
function3()