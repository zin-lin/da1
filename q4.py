import numpy as np
import pandas as pd
import matplotlib.pylab as plt
import seaborn as sns
from scipy.stats import *

def q4j():
    # read file to begin with
    # Load the data
    df = pd.read_csv('CWNumeric.csv')
    x = [1, 2, 3, 4]
    # get total scores for each value
    one = df[df['job'] == 1]
    two = df[df['job'] == 2]
    three = df[df['job'] == 3]
    four = df[df['job'] == 4]
    vals = []
    vals.append(one['class'])
    vals.append(two['class'])
    vals.append(three['class'])
    vals.append(four['class'])
    dict = {}
    count = 0
    for i in x:
        dict[i] = vals[count]
        count += 1

    # Perform a one-way ANOVA test to see if there is a significant difference between the groups
    f_statistic, p_value = f_oneway(dict[1], dict[2], dict[3], dict[4]
                                    )

    # Print the results
    print('f-statistic:', f_statistic)
    print('p-value:', p_value)

    # Check if the p-value is less than 0.05 to determine significance
    if p_value < 0.05:
        print(
            'There is a significant difference between p_status and class. \n Thus job influences ')
    else:
        print('There is no significant difference between p_status and class.  \n Thus job does not influence the thing')

    print('\n')

def q4p():
    # read file to begin with
    # Load the data
    df = pd.read_csv('CWNumeric.csv')
    x = [1,2,3,4]
    # get total scores for each value
    one = df[df['personal_status'] == 1]
    two = df[df['personal_status'] == 2]
    three = df[df['personal_status'] == 3]
    four = df[df['personal_status'] == 4]
    vals = []
    vals.append(one['class'])
    vals.append(two['class'])
    vals.append(three['class'])
    vals.append(four['class'])
    dict = {}
    count = 0
    for i in x:
        dict[i] = vals[count]
        count+=1

    # Perform a one-way ANOVA test to see if there is a significant difference between the groups
    f_statistic, p_value = f_oneway(dict[1], dict[2], dict[3], dict[4]
                                    )

    # Print the results
    print('f-statistic:', f_statistic)
    print('p-value:', p_value)

    # Check if the p-value is less than 0.05 to determine significance
    if p_value < 0.05:
        print('There is a significant difference between p_status and class. \n Thus personal_status influences the thing')
    else:
        print('There is no significant difference between p_status and class.   \n Thus personal_status does not influence the thing')

    print('\n')

def q4pur():
    # read file to begin with
    # Load the data
    data = pd.read_csv('CWNumeric.csv')
    df = data[data['purpose']!= 8]
    x = [1, 2, 3, 4, 5, 6, 7, 9, 10, 11]
    # get total scores for each value
    one = df[df['purpose'] == 1]
    two = df[df['purpose'] == 2]
    three = df[df['purpose'] == 3]
    four = df[df['purpose'] == 4]
    five = df[df['purpose'] == 6]
    six = df[df['purpose'] == 6]
    seven = df[df['purpose'] == 7]
    eight = df[df['purpose'] == 8]
    nine = df[df['purpose'] == 9]
    ten = df[df['purpose'] == 10]
    eleven = df[df['purpose'] == 0]
    vals = []

    vals.append(one['class'])
    vals.append(two['class'])
    vals.append(three['class'])
    vals.append(four['class'])

    vals.append(five['class'])
    vals.append(six['class'])
    vals.append(seven['class'])
    vals.append(eight['class'])

    vals.append(nine['class'])
    vals.append(ten['class'])
    vals.append(eleven['class'])
    dict = {}
    count = 0
    for i in x:
        print(i)
        dict[i] = df[df['purpose'] == i]['class']
        count += 1

    # Perform a one-way ANOVA test to see if there is a significant difference between the groups
    f_statistic, p_value = f_oneway(dict[1], dict[2], dict[3], dict[4],
                                    dict[5], dict[6], dict[7], dict[9], dict[10], dict[11]
                                    )

    # Print the results
    print('f-statistic:', f_statistic)
    print('p-value:', p_value)

    # Check if the p-value is less than 0.05 to determine significance
    if p_value < 0.05:
        print(
            'There is a significant difference between p_status and class. \n Thus purpose influences the thing')
    else:
        print('There is no significant difference between p_status and class.   \n Thus purpose does not influence the thing')
    print('\n')

def re(n):
    return n
def q4(column, constraints = [1,2,3,4]):
    df= pd.read_csv("CWnumeric.csv")
    values = df[column]
    vals = []
    # all values
    # sets up dictionary
    dict = {}
    dicts = []
    for i in constraints:
        dict[i] = df[df[column] == i]['class'] # as list
        dicts.append(dict[i])


    # Print the results
    f_stats, p_val = 0,0
    f_stats, p_val = f_oneway(*dicts)
    print('f-statistic:', f_stats)
    print('p-value:', p_val)

    # Check if the p-value is less than 0.05 to determine significance
    if p_val < 0.05:
        print(f'There is a significant difference between class and {column}.\n-{column} influences class')
    else:
        print(f'There is no significant difference between class and {column}.\n-{column} does not influence class')
    print('\n')