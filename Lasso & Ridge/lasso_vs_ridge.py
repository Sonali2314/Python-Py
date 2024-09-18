import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import Lasso, Ridge
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

np.random.seed(42)
X=np.random.rand(80,1)*10
y= 2+0.5*X**2-3*X+np.random.randn(80,1)*5

poly= PolynomialFeatures(degree=2,include_bias=False)
X_poly = poly.fit_transform(X)

X_train,X_test,y_train,y_test=train_test_split(X_poly,y,test_size = 0.2, random_state=42)

lasso=Lasso(alpha=1.0)
lasso.fit(X_train,y_train)
y_pre_L=lasso.predict(X_test)
lasso_mse=mean_squared_error(y_test, y_pre_L)

ridge=Ridge(alpha=1.0)
ridge.fit(X_train,y_train)
y_pre_R=ridge.predict(X_test)
ridge_mse=mean_squared_error(y_test,y_pre_R)

plt.scatter(X,y,color='cyan',label='Original Data')
plt.scatter(X,ridge.predict(poly.transform(X)),color='green',label='Ridge Regression: ')
plt.scatter(X,lasso.predict(poly.transform(X)),color='yellow',label='Lasso Regression: ')
plt.title('Lasso Vs Ridge')
plt.legend()
plt.show()
