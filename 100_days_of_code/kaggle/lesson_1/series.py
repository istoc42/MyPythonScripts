import pandas as pd

srs = pd.Series([1,2,3,4,5])
srs2 = pd.Series([1,2,3,4,5], index=['first', 'second', 'third', 'fourth', 'fifth'], name='The order')

print(srs)
print(srs2)