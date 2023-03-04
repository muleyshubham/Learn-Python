#Functions with default parameters/ arguments

#DEFAULT PARAMETERS
# OPTIONAL PARAMETERS
#address parameter is given a default value "DEFAULT"
# if user is supplying both parameters values then those will be considered
# if user is not supplying address information then it will be considered as DEFAULT

def print_person(name="DEFAULT",address="DEFAULT"):
    print(f"Name = {name}")
    print(f"Address = {address}")

print_person("Akshita","Pune") #VALID   Akshita Pune
print("-"*80)
print_person("Sparsh")  # VALID   Sparsh  DEFAULT
print_person() # VALID   DEFAULT DEFAULT