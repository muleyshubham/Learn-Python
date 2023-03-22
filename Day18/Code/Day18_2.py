#list comprehension

#find sqaures of numbers using lambda
def function1():
    numbers=[1,2,3,4,5,6,7,8,9,10]
    squares=list(map(lambda n : n ** 2 , numbers))
    print(numbers)
    print(squares)
#function1()

def function2():
    numbers=[1,2,3,4,5,6,7,8,9,10]
    sqaures=[]
    for i in numbers:
        sqaures.append(i**2)
    print(numbers)
    print(sqaures)
#function2()

#sqaures using list comprehension
def function3():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    sqaures = [n**2 for n in numbers]
    cubes = [n ** 3 for n in numbers]
    print(numbers)
    print(sqaures)
    print(cubes)
function3()


