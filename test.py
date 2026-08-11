import pandas as pd
import seaborn as sns
import explore

df = sns.load_dataset('titanic')
exp = explore.Explore(df)

print(exp.dtypes)
print('\n')
print(exp.min)
print('\n')
print(exp.max)