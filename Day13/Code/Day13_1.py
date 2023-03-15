#any .py file is called as Module
# whenever any python file is getting executed currently
# python interpreter considers the name of the Module as "__main__"
# __name__ gives the output of name of the current module

def add(p1,p2):
    print(f" {p1} + {p2} = {p1+p2}")

def sub(p1,p2):
    print(f" {p1} - {p2} = {p1-p2}")

print(f"Module Name = {__name__}") # Module name as __main__
add(5,4)
sub(3,2)
