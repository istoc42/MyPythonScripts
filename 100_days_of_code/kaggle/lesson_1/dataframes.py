import pandas as pd

df = pd.DataFrame({'Yes': [50, 21], 'No': [131, 2]})
df2 = pd.DataFrame({'Column 1': [10,20,30], 'Column 2': [40,50,60]})
df3 = pd.DataFrame({'Hit points': [86, 114, 50], 'AC': [16, 17, 11]}, index=['Tullius', 'Wilburforth', 'Crow'])

print(df)
print(df2)
print(df3)