#file operations
# read (r) , write (w) , append (a)
# "w" mode specifies write the contents in the file
# if file is not existing it will create the file
# if file is existing it will overwrite the contents within the file

# "a" mode specifies  append , add the contents at the end of the file
# if file is not exisiting it first creates it and add the contents
# if file is existing then it will add the contents at the end of the file

#"r" mode used for reading the data


file_name="demo.txt"
def write_data():
    data="This is my data to be written inside the file"

    #step1: open the file
    f1 = open(file_name,"w")

    #step2: write the contents
    f1.write(data)

    #step3: close the file
    f1.close()

#write_data()

# accept some data from user and write the data inside the file

def write_own_data():

    data=input("Enter your data")

    #step1:open the file
    f1= open("test.txt","w")

    #step2: write the contents
    f1.write(data)

    #step3: close the file
    f1.close()
#write_own_data()



def append_data():

    data=input("Enter your data")

    #step1:open the file
    f1= open("test.txt","a")

    #step2: write the contents
    f1.write(data)

    #step3: close the file
    f1.close()

#append_data()

def read_data():
    #step1 : open a file , mode = "r"
    f1=open("test.txt","r")
    #step2: read the contents
    data = f1.read(15) # it will read first 15 characters from the file
    print(data)
    data = f1.read(5) # it will read next five characters
    print(data)
    # step3: close the file
    f1.close()
#read_data()



def read_data1():
    #step1 : open a file , mode = "r"
    f1=open("test.txt","r")
    #step2: read the contents
    data=f1.readline() # it reads first line from the file
    print(data)
    # step3: close the file
    f1.close()
#read_data1()



def read_data2():
    #step1 : open a file , mode = "r"
    f1=open("test.txt","r")
    #step2: read the contents
    data=f1.readlines() # it reads all the lines from the file returns a list
    print(data)
    # step3: close the file
    f1.close()
#read_data2()

def read_data3():
    #step1 : open a file , mode = "r"
    f1=open("test.txt","r")
    #step2: read the contents
    data=f1.readlines() # it reads all the lines from the file returns a list
    for line in data:
        print(line)
    # step3: close the file
    f1.close()

#read_data3()


def read_data4():
    #step1 : open a file , mode = "r"
    f1=open("test.txt","r")
    #step2: read the contents
    data=f1.readlines() # it reads all the lines from the file returns a list
    for line in data:
        print(line.replace("\n",""))
    # step3: close the file
    f1.close()
read_data4()
