import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

# read the csv and then plot it

def function1():
    df = pd.read_csv('./Salary_Data.csv')
    plt.style.use('ggplot')
    #plot the graph
    plt.plot(df['YearsExperience'],df['Salary'],color='blue',label='salary')
    #customize the chart
    plt.xlabel("EXPERIENCE")
    plt.ylabel("SALARY")
    plt.title("EMPLOYEE SALARIES")

    plt.legend()

    # show the plot
    plt.show()
    plt.tight_layout()

#function1()

def function2():
    fig, ax = plt.subplots()

    fruits = ['apple', 'blueberry', 'cherry', 'orange']
    counts = [40, 100, 30, 55]
    bar_labels = ['red', 'blue', '_red', 'orange']
    bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange']

    ax.bar(fruits, counts, label=bar_labels, color=bar_colors)

    ax.set_ylabel('fruit supply')
    ax.set_title('Fruit supply by kind and color')
    ax.legend(title='Fruit color')

    plt.show()
#function2()

def function3():
    subjects='C','C++','Python','Java'
    marks=[38,37,34,39]

    plt.pie(marks,labels=subjects)
    plt.show()
#function3()

def function4():
    label_values = 'Frogs', 'Hogs', 'Dogs', 'Logs'
    sizes = [15, 30, 45, 10]
    explode_values = (0,0.1,0,0)

    fig, ax = plt.subplots()

    ax.pie(sizes, explode = explode_values, labels=label_values)
    plt.show()
#function4()



def function5():
    label_values = 'Frogs', 'Hogs', 'Dogs', 'Logs'
    sizes = [15, 30, 45, 10]
    explode_values = (0,0.1,0,0)

    fig, ax = plt.subplots()

    ax.pie(sizes, explode = explode_values, labels=label_values,shadow=True)

    plt.show()

function5()