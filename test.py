import explore
import pandas as pd

df = pd.read_csv('sample.csv')
df2 = pd.DataFrame({'a':['123#$%%', '214124fsfaf)(*&^%^&^%$%^', ',./.asf/.fwf/[]qwf.qfq./f123(*+_+_=-'], 'b': ['12324wed)(*&()(_', 'iuhsajkbusai^&$^%&^*&(**^543', 'iuyvbionaub(&*^&()&^%$#$@#$@!#!~!~']})
exp = explore.Explore(df2)

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