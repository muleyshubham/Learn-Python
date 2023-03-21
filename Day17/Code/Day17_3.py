
def divide(n1,n2):
    result = n1/n2
    print(result)

#divide(10,2) # works fine
#divide(3,0) # ZeroDivisionError: division by zero

def function1(n1,n2):
    #write the code which may generate the exception
    try:
        result = n1/n2
        print(result)
    except:# here we can take corrective actions
        print("Second number can not be zero while performing division")

#function1(9,3) # ok

#function1(5,0) #exception occured but it moves to except block
#and displays the proper messege


# try : will have number of statements to be observed
# inside the try block if exception occurs it goes to "except" block
# inside the try block if exception do not occur it goes to "else" block
def function2(n1,n2):
    #write the code which may generate the exception
    try:
        result = n1/n2
    except:
        print("Second number can not be zero while performing division")
    else:
        print(result)

#function2(20,10)
#function2(9,0)

# finally block gets executed compulsory irrespective of
#exception have occured or didn't occured
def function3(n1,n2):
    #write the code which may generate the exception
    try:
        result = n1/n2
    except:
        print("Second number can not be zero while performing division")
    else:
        print(result)
    finally:
        print("inside finally block")

#function3(15,5)
function3(8,0)