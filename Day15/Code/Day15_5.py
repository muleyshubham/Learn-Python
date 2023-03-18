import pandas as pd
import numpy as np

def function1():
    #create a dictionary
    p1=({"name":"person1","address":"pune"})
    p2 = ({"name": "person2", "address": "mumbai"})

    #create series
    s1=pd.Series(p1)
    s2=pd.Series(p2)

    print(s1)
    print(s2)
#function1()


def function2():
    #create a dictionary
    p1=({"name":"person1","address":"pune","age":25})
    p2 = ({"name": "person2", "address": "mumbai","age":28})

    # create Series
    s1=pd.Series(p1)
    s2=pd.Series(p2)

    # data frame
    df=pd.DataFrame([s1,s2])
    print("printing the data frame")
    print(df)

function2()