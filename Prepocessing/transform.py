import pandas as pd
import numpy as np

data=pd.read_csv('data.csv')
print(data)

#creating X and y
from sklearn.impute import SimpleImputer
X=data.iloc[:,:-1].values
y=data.iloc[:,-1].values

# filling nan
imputer = SimpleImputer(missing_values = np.nan, strategy ='mean')
imputer.fit(X[:,1:])
X[:,1:]=imputer.transform(X[:,1:])
print(X[:,:])

from sklearn.preprocessing import OneHotEncoder
