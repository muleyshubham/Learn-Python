# pandas
# there are two important things
# 1. Series  2. DataFrame
# one dimensional data - series
# multi dimensional data - data frame

import pandas as pd
import numpy as np

# create a list, array, series
def function1():
    # list of numbers
    numbers_list=[10,20,30,40,50]
    print(f"List = {numbers_list} Type = {type(numbers_list)}")

    #array of numbers
    numbers_arr=np.array([1,2,3,4,5])
    print(f"Array = {numbers_arr} Type = {type(numbers_arr)}")

    # array of series
    # Series is a class
    numbers_series = pd.Series([11,22,33,44,55])
    print(f"Series = {numbers_series} Type = {type(numbers_series)}")

#function1()

# properties of pandas
def function2():
    number_series=pd.Series([10,20,30,40,50])
    print(f"Number Series = {number_series}")
    print(f"Type = {type(number_series)}")
    print(f" Dtype = {number_series.dtype}")
    print(f"size = {number_series.size}")
    print(f"ndim = {number_series.ndim}")
    print(f"Nbytes = {number_series.nbytes}")
    print(f"Shape = {number_series.shape}")
    print(f"Keys = {number_series.keys()}")
    print(f" Values= {number_series.values}")
    print("-"*80)

function2()





