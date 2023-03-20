#read the csv and save the data in another csv
import pandas as pd


def function1():
    df=pd.read_csv("./Salary_Data.csv")
    print(df)
    print(f"Columns = {df.columns}")

    #add a new column
    df['bonus']=1000
    print(df)
    print(f"columns = {df.columns}")
    print("-"*80)

#function1()

def function2():
    df = pd.read_csv("./Salary_Data.csv")
    print(df)
    print(f"Columns = {df.columns}")

    # add a column
    # 10% bonus to each employee record
    df['bonus']=df['Salary'] * 0.10
    print(df.head())
    print(f"Columns = {df.columns}")

    #save the changes in another CSV
    df.to_csv("new_salary_data.csv")

function2()

# comparasion of some columns
# take first csv in df1
# take second csv in df2
# fetch column of df1['empid']
# fetch column of df2['empid]
# conditional statment if else...while ...check the data

# df3['salary'] = df2['salary'] - df1['salary]
