#matplotlib is third party library used for data visualization
# pyplot is python version of matplot for plotting the graphs

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

# define a function
# np array data , plot it in a graph
def function1():
    experience = np.array([1,1.5,2,2.5,3,3.5,4,4.5,5])
    salaries = np.array([15,18,20,23,25,28,32,35,40])

    #draw scatter plot
    plt.scatter(experience,salaries)

    # show the chart
    plt.show()

#function1()

def function2():
    experience = np.array([1,1.5,2,2.5,3,3.5,4,4.5,5])
    salaries = np.array([15,18,20,23,25,28,32,35,40])

    #draw scatter plot
    plt.scatter(experience,salaries)

    # customize the chart
    plt.xlabel("EXPERIENCE")
    plt.ylabel("SALARIES")
    plt.title("SALARIES OF EMPLOYEES")

    # show the chart
    plt.show()
#function2()

def function3():
    experience = np.array([1,1.5,2,2.5,3,3.5,4,4.5,5])
    salaries = np.array([15,18,20,23,25,28,32,35,40])

    #draw scatter plot
    plt.scatter(experience,salaries,color='red',label="salary")

    # customize the chart
    plt.xlabel("EXPERIENCE")
    plt.ylabel("SALARIES")
    plt.title("SALARIES OF EMPLOYEES")

    plt.legend()
    # show the chart
    plt.show()

    plt.tight_layout() # it shows the plot in better way
                       #with the proper margins
#function3()

# apply some style to the graph
def function4():
    experience = np.array([1,1.5,2,2.5,3,3.5,4,4.5,5])
    salaries = np.array([15,18,20,23,25,28,32,35,40])
    expenses = np.array([11,15,17,21,22,24,30,32,37])

    #set the style
    #plt.style.use('ggplot')
    #plt.style.use('dark_background')
    plt.style.use('Solarize_Light2')

    #draw scatter plot
    plt.scatter(experience,salaries,color='red',label="salary")
    plt.scatter(experience, expenses, color='green', label="expense")

    # customize the chart
    plt.xlabel("EXPERIENCE")
    plt.ylabel("SALARIES / EXPENSES")
    plt.title("SALARIES OF EMPLOYEES")

    plt.legend()
    # show the chart
    plt.show()

    plt.tight_layout()
#function4()

#from matplotlib import style
#print(plt.style.available) # list of available style


def function5():
    experience = np.array([1,1.5,2,2.5,3,3.5,4,4.5,5])
    salaries = np.array([15,18,20,23,25,28,32,35,40])
    expenses = np.array([11,15,17,21,22,24,30,32,37])

    #set the style
    #plt.style.use('ggplot')
    #plt.style.use('dark_background')
    plt.style.use('Solarize_Light2')

    #draw scatter plot
    plt.scatter(experience,salaries,color='red',label="salary")
    plt.scatter(experience, expenses, color='green', label="expense")

    # customize the chart
    plt.xlabel("EXPERIENCE")
    plt.ylabel("SALARIES / EXPENSES")
    plt.title("SALARIES OF EMPLOYEES")

    plt.legend()

    # save the chart
    plt.savefig("EMP_SALARIES.png")

    # show the chart
    plt.show()

    plt.tight_layout()

#function5()

#line graph

def function6():
    experience = np.array([1,1.5,2,2.5,3,3.5,4,4.5,5])
    salaries = np.array([15,18,20,23,25,28,32,35,40])
    expenses = np.array([11,15,17,21,22,24,30,32,37])

    #set the style
    plt.style.use('ggplot')

    #draw line chart
    plt.plot(experience,salaries,color='red',label="salary")
    plt.plot(experience, expenses, color='green', label="expense")

    # customize the chart
    plt.xlabel("EXPERIENCE")
    plt.ylabel("SALARIES / EXPENSES")
    plt.title("SALARIES OF EMPLOYEES")

    plt.legend()

    # save the chart
    plt.savefig("EMP_SALARIES_Line_GRAPH.png")

    # show the chart
    plt.show()

    plt.tight_layout()

function6()


