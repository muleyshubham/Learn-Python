import pandas as pd
#read the csv
def function1():
    df=pd.read_csv("./50_Startups.csv")
    print(df)
    print("-"*80)
    print(f"Columns = {df.columns}")

#function1()


def function2():
    df = pd.read_csv("./50_Startups.csv")
    print(f"Columns = {df.columns}")
    print("Reading first five records from dataframe")
    print(df.head())
    print("Reading first two records from dataframe")
    print(df.head(2))
    print(f"Read the last five records")
    print(df.tail())
    print("Reading last three records from dataframe")
    print(df.tail(3))
    print("*****show information about data frame*****")
    df.info()
#function2()


def function3():
    df = pd.read_csv("./50_Startups.csv")
    print(f"Columns = {df.columns}")
    print("Reading first ten records from dataframe")
    print(df.head(10))
    print("Reading last ten records from dataframe")
    print(df.tail(10))
#function3()


def function4():
    df = pd.read_csv("./50_Startups.csv")
    print(df.describe())
    #describe function is used to fetch the
    # statistical information about the data frame
function4()