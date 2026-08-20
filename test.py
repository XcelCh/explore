import explore
import pandas as pd
import seaborn as sns

df = sns.load_dataset('dowjones')
exp = explore.Explore(df)

#print(exp.numeric.count_quartile)

"""
print('Data Types:')
print(exp.dtypes)
print('\n')

print('Null Values:')
print(exp.null)
print('\n')

print('Numeric Summary:')
print(exp.numeric)
print('\n')

print('Text Summary:')
print(exp.text)
print('\n')

print('Category Summary:')
print(exp.category)
print('\n')

print('Date Summary:')
print(exp.date)
print('\n')
"""

print('Numeric Summary:')
print(exp.numeric_summary())
print('\n')

print('Text Summary:')
print(exp.text_summary())
print('\n')

print('Category Summary:')
print(exp.category_summary())
print('\n')

print('Date Summary:')
print(exp.date_summary())
print('\n')