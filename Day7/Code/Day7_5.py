#list inside tuple

# (10) ==> type ===> int
# (10,) ==> type ==> tuple


def function1():
    #list inside tuple
    numbers=(
        [10,20]
    )
    print(f"Numbers = {numbers}")
    numbers.append((30,40)) #allowed
    # numbers [10,20] without comma inside tuple are
    #considered as individual element of type int
    print(f"Numbers = {numbers}")

#function1()


def function2():
    #list inside tuple
    numbers=(
        [10,20],
    )
    print(f"Numbers = {numbers}")
    numbers.append((30,40)) # AttributeError
    print(f"Numbers = {numbers}")

#function2()


def function3():
    #list inside tuple
    numbers=(
        [10,20],
    )
    print(f"Numbers = {numbers}")
    numbers[0].append(99)
    print(f"Numbers = {numbers}")


function3()