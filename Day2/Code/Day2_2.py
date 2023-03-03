# Data type Hinting
# hint given to developer

val : int = 50
print(f"Value = {val}")
print(f"Type = {type(val)}")


result : int = "70"
# result is storing "70" which will be considered as String
#even if we supply type hinting it does not matter

print(f"Result = {result}")
print(f"Type = {type(result)}")

