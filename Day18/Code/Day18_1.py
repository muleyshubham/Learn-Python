#Custom Exception (user defined exceptions)
#input from user as age
# if age<20 or age>60 raise an exception "Invalid Age"

class AgeException(Exception):
    pass

class NumberException(Exception):
    pass

def function1():
    name=input("Enter Your name")
    age=input("Enter your age")
    number=input("Enter some number")
    try:
        age=int(age)
        if age<20 or age>60:
            raise AgeException()
        print(f"Name = {name} Age = {age}")

        number=int(number)
        if number>50:
            raise NumberException()


    except AgeException:
        print("Invalid Age")
    except NumberException:
        print("Number is greater than 50")
    except:
        print("Exception have occured")

function1()
