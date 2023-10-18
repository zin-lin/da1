
import numpy as np
import pandas as pd
import matplotlib.pylab as plt
def q3a():
    # read file to begin with
    df = pd.read_csv("coursework.csv")
    plt.figure(figsize=(14, 6))
    df['personal_status'] = df['personal_status'].astype('category')
    df['personal_status'].cat.rename_categories(["'male div/sep'", "'female div/dep/mar'", "'male single'", "'male mar/wid'"])

    df1 = df[df['personal_status'] == "'male div/sep'"]
    plt.hist([df['personal_status'][df['class'] == "good"],
              df['personal_status'][df['class'] == "bad"]],
    label=['good','bad'])

    plt.legend(loc='upper right')
    plt.xlabel('personal status')
    plt.show()

def q3b():
    # read file to begin with
    df = pd.read_csv("coursework.csv")
    plt.figure(figsize=(14, 6))
    df['credit_history'] = df['personal_status'].astype('category')
    df['personal_status'].cat.rename_categories(["'male div/sep'", "'female div/dep/mar'", "'male single'", "'male mar/wid'"])

    df1 = df[df['personal_status'] == "'male div/sep'"]
    plt.hist([df['personal_status'][df['class'] == "good"],
              df['personal_status'][df['class'] == "bad"]],
    label=['good','bad'])

    plt.legend(loc='upper right')
    plt.xlabel('personal status')
    plt.show()