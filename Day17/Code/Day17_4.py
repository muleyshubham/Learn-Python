# specific except blocks

def function1():
    file=open("my-file.txt","r")
    data=file.readlines()
    print(data)

#function1() #FileNotFoundError

def function2():
    try:
        file=open("my-file.txt","r")
        data=file.readlines()
        print(data)
    except:
        print("exception have occurred")
#function2()

def function3():
    try:
        file=open("test.txt","r")
        data=file.readlines()
        print(data)
        n1=5
        n2=0
        print(n1/n2)
    except:
        print("exception have occurred")

#function3()



def function4():
    try:
        file=open("test.txt","r")
        data=file.readlines()
        print(data)
        n1=5
        n2=0
        print(n1/n2)
    except ZeroDivisionError:
        print("second number in division can't be zero")
    except FileNotFoundError:
        print("File is unavailable")

function4()