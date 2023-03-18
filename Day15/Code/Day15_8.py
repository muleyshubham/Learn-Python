# read the csv file using pandas

import pandas as pd
def function1():
    df=pd.read_csv("./50_Startups.csv")
    print(df)
    print("-"*80)
    print(f"Columns = {df.columns}")
function1()