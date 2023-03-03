#Type Conversion

#implicit type casting
num=10
f_val=5.5
addition = num + f_val
print(f"Num = {num} F_VAL = {f_val} Addition = {addition}")
print(f"Num = {type(num)}  F_VAL = {type(f_val)} Addition = {type(addition)}")

print()
num1=60
str1="hello"
#res = num1+str1
#print(f"Type = {type(res)}")
#TypeError: unsupported operand type(s) for +: 'int' and 'str1'

#explicit typecasting
#str() is a function which is used to convert any value in String format
#str() explicitely converts value in string type

res=str(num1)+str1   # "60" + hello #concatination operation
print(f"Result = {res}")
print(f"Type = {type(res)}")

v1="35"
v2="15"
result = v1+v2  #3515
print(f"Result = {result}")
print(f"Type = {type(result)}")

#explicit typecasting
#int() is used to convert string to int value
result = int(v1)+int(v2)
print(f"Result = {result}")
print(f"Type = {type(result)}")

