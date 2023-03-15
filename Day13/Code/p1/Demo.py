import p1

def function1():
    import p1.Faculty  # import the Module Faculty from Package p1
    import p1.Student # import the Module Student from Package p1
    p1.Student.m1()
    p1.Student.m2()
    p1.Faculty.m3()
    p1.Faculty.m4()
#function1()

def function2():
    from p1.Faculty import m3
    p1.Faculty.m3()

function2()

