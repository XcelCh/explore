import seaborn as sns
import explore

df = sns.load_dataset('titanic')
exp = explore.Explore(df)

print('Data Types:')
print(exp.dtypes)
print('\n')

print('Null Values:')
print(exp.null)
print('\n')

print('Numeric Summary:')
print(exp.numeric)
print('\n')