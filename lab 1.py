import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer

DataFrame = pd.DataFrame({'team': ['A','A','A','A',np.nan,'B','B','B'],
                          'position' : ['G','G','F','G','F','C','C','H'],
                          'Age':[30,31,52,64,24,np.nan,44,33],
                          'Salarty':[5000,2645,9400,3600,8000,6741,6571,9500]})
Numerical_Features = DataFrame.select_dtypes(exclude=['object']).columns.to_list()
print(Numerical_Features)
DataFrame_N = DataFrame[Numerical_Features]
print(DataFrame_N)

imp_mean = SimpleImputer(missing_values=np.nan, strategy='mean')
imp_mean.fit(DataFrame_N)
DataFrame_N = imp_mean.transform(DataFrame_N)
print(DataFrame_N)

c_Features = DataFrame.select_dtypes(include=['object']).columns.to_list()
print(c_Features)
DataFrame_C = DataFrame[c_Features]
print(DataFrame_C)

imp_mean = SimpleImputer(missing_values=np.nan, strategy='most_frequent')
imp_mean.fit(DataFrame_C)
DataFrame_C = imp_mean.transform(DataFrame_C)
print(DataFrame_C)

DataFrame[Numerical_Features] = DataFrame_N
DataFrame[c_Features]=DataFrame_C