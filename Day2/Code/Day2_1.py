# Data types
# In python data types are inferred
# inferred , automatically assigned by python

num = 55
print(num) # 55
print(type(num)) # <class 'int'>

#Ouput , Number = 55
print(f"Number = {num}")
#while formatting the output ,
# whatever you put in curly brackets its value will be considered
print()

#float
percentage = 80.5
print(f"Percentage {percentage}")
print(f"Type = {type(percentage)}") # <class 'float'>
print()

name="Akshita"
print(f"Name = {name}")
print(f"Type = {type(name)}") # <class 'str'>
print()
org="sunbeam"
print(f"Organization = {org}")
print(f"Type = {type(org)}")

print()
n1=20
n2=15
print(f"Num1 = {n1}")
print(f"Num2 = {n2}")

print()
grade='A'
print(f"Grade = {grade}")
print(f"Type = {type(grade)}") #<class 'str'>

print()
locations="""pune,
hinjewadi,
marketyard,
karad"""
print(f"Locations = {locations}")
print(f"Type = {type(locations)}")

print()
can_vote=True # True or False (T and F must be capital)
print(f"Can Vote = {can_vote}")
print(f"Type = {type(can_vote)}") #<class 'bool'>




