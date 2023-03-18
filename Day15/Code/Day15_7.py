#create data frame from dictionay and display properties

#NaN ( Not a Number)
# if the value of some column is missing it assigns it as NaN
import pandas as pd
def function1():
    #create a data frame and pass dictionary
    df=pd.DataFrame([{"model":"oneplus7","company":"ONEPLUS","price":50000,"color":"black"},
                     {"model": "lg6", "company": "LG", "price": 30000,"memory":"8gb"},
                     {"model": "apple13", "company": "APPLE", "price": 70000},
                     {"model": "samsung8", "company": "SAMSUNG", "price": 40000}
    ]
    )
    print(df)
    print("-"*70)
    print(f"Type = {type(df)}")
    print(f"dtypes = {df.dtypes}")
    print(f"size = {df.size}")
    print(f" dimension = {df.ndim}")
    print(f" shape = {df.shape}")
    print(f" keys = {df.keys()}")
    print(f"values = {df.values}")
    print(f" Index {df.index}")
    print(f" Columns {df.columns}")


function1()
