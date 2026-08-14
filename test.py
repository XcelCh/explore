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

print('Text Columns:')
print(exp.text.columns)
print('\n')

print('Longest Text:')
print(exp.text.longest_text)
print('\n')

print('Shortest Text:')
print(exp.text.shortest_text)
print('\n')

print('Empty Text Count:')
print(exp.text.count_empty)
print('\n')

print('Text Occurence Count:')
print(exp.text.count_text_occur)
print('\n')

print('Has Symbol:')
print(exp.text.has_symbol)
print('\n')

