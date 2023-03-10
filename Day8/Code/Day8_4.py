#need of function alias
def disp(param):
    print(f"Param = {param} type = {type(param)}")

disp(25)
disp("Akshita")
print(f"disp = {disp} type = {type(disp)}")

test = disp # test is an function alias
test("sunbeam")
print("-"*80)
disp(test)
# internally , param = test , test = function alias

a1=test
a2=disp
print(f"a1 = {a1} type = {type(a1)}")
print(f"a2 = {a2} type = {type(a2)}")