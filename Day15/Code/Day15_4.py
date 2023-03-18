import pandas as pd

def function1():
    #list
    marks=[45,35,48,37,42]
    students=["s1","s2","s3","s4","s5"]

    #create series of marks and students
    m_series = pd.Series(marks)  # it will create a Series of marks with index 0 to 4
    s_series = pd.Series(students) # it will create a series of students with index 0 to 4

    print(m_series)
    print(s_series)
    print("-"*80)
    print(m_series.keys())
    print(m_series.values)
    print(s_series.keys())
    print(s_series.values)

#function1()

# requirment
# create a Series where one list "students" is treating as values
# another list " marks" can be treated as keys

def function2():
    #list
    marks=[45,35,48,37,42]
    students=["s1","s2","s3","s4","s5"]

    # series of students having index as marks
    s_series = pd.Series(students,index=marks)

    print(s_series)
    print(s_series.keys())
    print(s_series.values)

function2()