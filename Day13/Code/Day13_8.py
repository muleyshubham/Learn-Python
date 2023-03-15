# dir() is used for viewing the functionalities supplied by any module

def function1():
    import os
    print(f"{dir(os)}")
#function1()

def function2():
    import os
    print(os.listdir.__doc__)
#function2()


def function3():
    import os
    files=os.listdir("D:\Sunbeam\February2023\Modular Batches\Python_O-09")
    print(files)
#function3()

def function4():
    import os
    from os.path import join, getsize
    for root, dirs, files in os.walk('D:\Sunbeam\Akshita_Python'):
        print(root, "consumes", end=" ")
        print(sum(getsize(join(root, name)) for name in files), end=" ")
        print("bytes in", len(files), "non-directory files")
        if 'CVS' in dirs:
            dirs.remove('CVS')  # don't visit CVS directories
#function4()


def function5():
    import os
    from os.path import join, getsize
    for root, dirs, files in os.walk('D:\Sunbeam\February2023\Modular Batches\Python_O-09\DAY12'):
        print("-"*80)
        print("ROOT")
        print(root)
        print("-" * 80)
        print("DIRECTORIES")
        print(dirs)
        print("-" * 80)
        print("FILES")
        print(files)
#function5()


def function6():
    import os
    print(os.getcwd())

function6()