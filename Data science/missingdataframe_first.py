# importing pandas as pd 
import pandas as pd 

# importing numpy as np 
import numpy as np 

# dictionary of lists 
dict = {'First Score':[100, 90, None, 95], 
		'Second Score': [30, 45, 56, None], 
		'Third Score':[None, 40, 80, 98]} 

# creating a dataframe from list 
df = pd.DataFrame(dict) 

# using isnull() function 
x=df.fillna(df.mean())
print(x)