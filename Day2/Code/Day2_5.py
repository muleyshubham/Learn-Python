#Comparsion operators

num1=25
num2=15

print(f" num1>num2 {num1>num2}")
print(f" num1<num2 {num1<num2}")
print(f" num1==num2 {num1==num2}")
print(f" num1>=num2 {num1>=num2}")
print(f" num1<=num2 {num1<=num2}")
print(f" num1!=num2 {num1!=num2}")

str1="sunbeam"
str2="sunbeam"
str3="infotech"
str4="Sunbeam"
print(f"Compare = {str1==str2}")
print(f"Compare = {str1==str3}")
print(f"Compare = {str1==str4}")
print("-"*70)
#Logical Operators
b1=True
b2=False
print(f"Logical OR  = {b1 or b2}")
print(f"Logical And = {b1 and b2}")
print(f"Logical Not = {not b1}")

print("-"*70)

#assignment operators
num=15
num+=5  # num = num+5
print(f"Num = {num}")
num*=2  #num = num * 2
print(f"Num = {num}")

print("-"*70)
#Bitwise operators 
v1=12
v2=3
print(f"Left Shift {v1 << v2}")
# 12 ==> x   3 ===> n
# x << n ===> x * 2^n    12 * 2^3   12 * 8  ==> 96

print(f"Right Shift {v1 >> v2}")
# 12 ==> x   3 ===> n
# x >> n ===> x / 2^n    12 / 2^3   12 / 8  ==> 1