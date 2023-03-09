
# create a list , we wish to eliminate duplicate elements from list

def function1():
    l1=[20,10,30,10,40,50]
    print(f"List = {l1}")
    elements = set(l1)
    print(f"unique elements = {elements}")

#function1()

def function2():
    l1=["akshita","sunbeam","pune","trainer","akshita","sunbeam"]
    print(f"List = {l1}")
    unique_words=set(l1)
    print(f"Unique words = {unique_words}")
function2()