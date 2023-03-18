# create pandas series using different collections
# we can create pandas series using list, tuple and dictionary
# we can not create pandas series using set (coz its unordered)


import pandas as pd
import numpy as np

def function1():
    # create series using list
    s1=pd.Series([10,20,30,40,50])
    print(s1)
    print(f"Value at location 2 = {s1[2]}") # indexing
    print("-"*80)
    #create series using tuple
    s2=pd.Series((11,22,33,44,55))
    print(s2)
    print(s2.keys())
    print(s2.values)
    print(f"Value at location 3 = {s2[3]}")  # indexing
    print("-" * 80)
    #create series using set is not possible
    # set is unordered
    #s3=pd.Series(set(33,44,55,66)) # TypeError
    #s3=pd.Series({33,44,55,66}) # type Error

    #create series using dictionary
    s4=pd.Series({"name":"Akshita","org":"sunbeam","Address":"Pune"})
    print(s4)
    print("-"*80)
    print(s4.keys())
    print(s4.values)
    print("-"*80)
    print(f"Value at 2nd location from series = {s4[2]}")
    print(f"Value at location Address = {s4['Address']}")

    print(f"Value at 0th location from series = {s4[0]}")
    print(f"Value at location name = {s4['name']}")
    #print(f"Value at location name = {s4['Name']}") # KeyError , key is case sensitive

function1()