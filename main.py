# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import numpy as np
import pandas as pd
import matplotlib.pylab as plt
import q3a
import q3b
import q4

# For Question 3: Create two visual representations illustrating the distribution of credit class
# (e.g. good and bad) for different personal status and job status separately. To
# do this, start by restructuring the dataset into a new data frame for each
# condition (personal and job status) and include the total number of good and
# bad classes for each condition. [10%]

def int_main():
    # q3a.q3a()
    # q3b.q3b()
    # q4.q4p()
    # q4.q4j()

    q4.q4('personal_status', 4)
    q4.q4('job', 4)
    q4.q4('purpose', 4, [0,1,2,3,4,5,6,7,9,10])

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    int_main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
