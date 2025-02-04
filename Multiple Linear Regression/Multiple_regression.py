import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("manufacturing.csv")
df.head()

#check missing values
df.isnull().sum()

X = df.iloc[:,:-1]
y = df.iloc[:,-1]
print(X)
print("/n",y)

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=42)

# polynomial transformation
degree = 2  
poly = PolynomialFeatures(degree=degree)
X_poly_train = poly.fit_transform(X_train)
X_poly_test = poly.transform(X_test)
# Trainning polynomial regression model
model = LinearRegression()
model.fit(X_poly_train, y_train)

# Predict on the test set
y_pred = model.predict(X_poly_test)
print("Predictions of models are:",y_pred)

# Model evaluation
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f'Mean Squared Error (MSE):',mse)
print(f'R-squared (R2):',r2)

# Visualizing the results (1D for simplicity)
plt.scatter(X_test['Temperature (°C)'], y_test, color='yellow', label='Actual Quality Rating')
plt.scatter(X_test['Temperature (°C)'], y_pred, color='pink', label='Predicted Quality Rating')
plt.title('Polynomial Regression:Quality Rating')
plt.xlabel('Temperature (°C)')
plt.ylabel('Quality Rating')
plt.legend()
plt.show()
#------------------------------------------------------------------------------------FOR DEGREE 2-----------------------------------------------------------------------------------
degree = 4  
poly = PolynomialFeatures(degree=degree)
X_poly_train = poly.fit_transform(X_train)
X_poly_test = poly.transform(X_test)


# Trainning polynomial regression model
model = LinearRegression()
model.fit(X_poly_train, y_train)

# Predict on the test set
y_pred = model.predict(X_poly_test)
print("Predictions of models are:",y_pred)

# Model evaluation
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f'Mean Squared Error (MSE):',mse)
print(f'R-squared (R2):',r2)

# Visualizing the results (1D for simplicity)
plt.scatter(X_test['Temperature (°C)'], y_test, color='yellow', label='Actual Quality Rating')
plt.scatter(X_test['Temperature (°C)'], y_pred, color='pink', label='Predicted Quality Rating')
plt.title('Polynomial Regression:Quality Rating')
plt.xlabel('Temperature (°C)')
plt.ylabel('Quality Rating')
plt.legend()
plt.show()
#------------------------------------------------------------------------------------FOR DEGREE 4-----------------------------------------------------------------------------------
degree = 6  
poly = PolynomialFeatures(degree=degree)
X_poly_train = poly.fit_transform(X_train)
X_poly_test = poly.transform(X_test)


# Trainning polynomial regression model
model = LinearRegression()
model.fit(X_poly_train, y_train)

# Predict on the test set
y_pred = model.predict(X_poly_test)
print("Predictions of models are:",y_pred)

# Model evaluation
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f'Mean Squared Error (MSE):',mse)
print(f'R-squared (R2):',r2)

# Visualizing the results (1D for simplicity)
plt.scatter(X_test['Temperature (°C)'], y_test, color='yellow', label='Actual Quality Rating')
plt.scatter(X_test['Temperature (°C)'], y_pred, color='pink', label='Predicted Quality Rating')
plt.title('Polynomial Regression:Quality Rating')
plt.xlabel('Temperature (°C)')
plt.ylabel('Quality Rating')
plt.legend()
plt.show()
#------------------------------------------------------------------------------------FOR DEGREE 6-----------------------------------------------------------------------------------

degree = 8
poly = PolynomialFeatures(degree=degree)
X_poly_train = poly.fit_transform(X_train)
X_poly_test = poly.transform(X_test)


# Trainning polynomial regression model
model = LinearRegression()
model.fit(X_poly_train, y_train)

# Predict on the test set
y_pred = model.predict(X_poly_test)
print("Predictions of models are:",y_pred)
# Model evaluation
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f'Mean Squared Error (MSE):',mse)
print(f'R-squared (R2):',r2)

# Visualizing the results (1D for simplicity)
plt.scatter(X_test['Temperature (°C)'], y_test, color='yellow', label='Actual Quality Rating')
plt.scatter(X_test['Temperature (°C)'], y_pred, color='pink', label='Predicted Quality Rating')
plt.title('Polynomial Regression:Quality Rating')
plt.xlabel('Temperature (°C)')
plt.ylabel('Quality Rating')
plt.legend()
plt.show()
#------------------------------------------------------------------------------------FOR DEGREE 8-----------------------------------------------------------------------------------

degree = 12
poly = PolynomialFeatures(degree=degree)
X_poly_train = poly.fit_transform(X_train)
X_poly_test = poly.transform(X_test)


# Trainning polynomial regression model
model = LinearRegression()
model.fit(X_poly_train, y_train)

# Predict on the test set
y_pred = model.predict(X_poly_test)
print("Predictions of models are:",y_pred)
# Model evaluation
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f'Mean Squared Error (MSE):',mse)
print(f'R-squared (R2):',r2)

# Visualizing the results (1D for simplicity)
plt.scatter(X_test['Temperature (°C)'], y_test, color='yellow', label='Actual Quality Rating')
plt.scatter(X_test['Temperature (°C)'], y_pred, color='pink', label='Predicted Quality Rating')
plt.title('Polynomial Regression:Quality Rating')
plt.xlabel('Temperature (°C)')
plt.ylabel('Quality Rating')
plt.legend()
plt.show()
#------------------------------------------------------------------------------------FOR DEGREE 12-----------------------------------------------------------------------------------
#This 8 degree is suitable for this ml model
