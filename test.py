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

print('Text Summary:')
print(exp.text)
print('\n')

print('Category Summary:')
print(exp.category)
print('\n')

print('Date Summary:')
print(exp.date)
print('\n')
