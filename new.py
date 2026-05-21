import pandas as pd

new = ['a','b','c','d','e']
index = ['0','1','2','3','4']
new_series= pd.Series(new, index=index)
print(new_series)