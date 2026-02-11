#task 1

import numpy as np
import pandas as pd 
values = pd.Series(data=[700,150,300], index = ['Laptop','Mouse','keyboard'])
print(values)
print("laptop price:", values['Laptop'])
print("first two products:",values[0:2])
 

#task2

grades = pd.Series( [85,None,92,45, None,78,55])
grades.isnull()
grades.fillna(0)
print(grades[grades > 60])

#task3

usernames = pd.Series( [' Alice ', 'bOB', ' Charlie_Data ', 'daisy'])
usernames.str.strip()
usernames.str.lower()
low = usernames.str.lower()
low.str.contains(('a'))
print(low[low.str.contains('a')])
    

