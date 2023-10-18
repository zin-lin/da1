import numpy as np
import pandas as pd
import matplotlib.pylab as plt

def q3b():
    # read file to begin with
    df = pd.read_csv("coursework.csv")
    plt.figure(figsize=(14, 6))
    df['job'] = df['job'].astype('category')
    df['job'].cat.rename_categories(
        ["'unemp/unskilled non res'", "'unskilled resident '", "'skilled'", "'high qualif/self emp/mgmt'"])

    df1 = df[df['job'] == "'male div/sep'"]
    plt.hist([df['job'][df['class'] == "good"],
              df['job'][df['class'] == "bad"]],
             label=['good', 'bad'])

    plt.legend(loc='upper right')
    plt.xlabel('job status')
    plt.show()