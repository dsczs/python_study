# -*- coding: utf-8 -*-
"""
Linear Regression Example
@see https://scikit-learn.org/stable/auto_examples/linear_model/plot_ols.html
Version: 0.1
Author: dsczs
"""


import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score

# load the diabetes dataset
diabetes_X, diabetes_y = datasets.load_diabetes(return_X_y=True)

# use only one feature
diabetes_X = diabetes_X[:, np.newaxis, 2]

# split the data into train/testing sets
diabetes_X_train = diabetes_X[:-20]
diabetes_X_test = diabetes_X[-20:]

# split the targets into train/testing set
diabetes_y_train = diabetes_y[:-20]
diabetes_y_test = diabetes_y[-20:]

# create linear regression object
regr = linear_model.LinearRegression()

# train the model using the training sets
regr.fit(diabetes_X_train, diabetes_y_train)

# make predictions using the testing set
diabetes_y_pred = regr.predict(diabetes_X_test)

# the coefficients
print('coefficients:\n', regr.coef_)

# the mean squared error
print('Mean squared error: %.2f'
      % mean_squared_error(diabetes_y_test, diabetes_y_pred))
# The coefficient of determination: 1 is perfect prediction
print('Coefficient of determination: %.2f'
      % r2_score(diabetes_y_test, diabetes_y_pred))

# Plot outputs
plt.scatter(diabetes_X_test, diabetes_y_test,  color='black')
plt.plot(diabetes_X_test, diabetes_y_pred, color='blue', linewidth=3)

plt.xticks(())
plt.yticks(())

plt.show()












