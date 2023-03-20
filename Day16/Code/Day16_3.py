import pandas as pd
import numpy as np

def function1():
    df = pd.read_csv("./Salary_Data.csv")
    print(df.head())
    print(f"Columns = {df.columns}")

    #remove a column
    # while dropping a column axis is compulsory
    # rows : axis = 0
    # cols : axis = 1
    df = df.drop(['Salary'],axis=1)
    # axis = 1 indicates , complete column must be removed
    print(df.head(5))
#function1()

#read some specific record
# iloc ===> ith Location

def function2():
    df=pd.read_csv("50_Startups.csv")
    print(df.head())
    print("-"*80)
    print("Read 4th row with all the column values")
    print(df.iloc[4,])
    print("-"*80)
    print("Reading only Adminstration column from 4th row")
    print(df.iloc[4,1])
    print("-"*80)
    print("Print multiple rows and multiple column data")
    print(df.iloc[:5,1:3])


function2()

#print(df.iloc[:5,1:3])
# iloc[rows,columns]
# iloc[:5,1:3]
# it will consider taking the data from 0th row to 4th row
# it will take the data from 1st column to 3rd column from df