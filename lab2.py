# -*- coding: utf-8 -*-
"""Lab2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/14v0TgfAg1fbYR6I2_W2fRZY-vpd_XyMe

## Lab 2
### Name: Behnam Sobhani Nadri
### Student ID: 801368949

## All libraries that we use in the lab is defined here
"""

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
import numpy as np
import pylab as pl
from sklearn import preprocessing
from google.colab import drive
drive.mount('/content/drive')

"""## Cost function and the Gradient Descent Algorithm"""

def compute_cost(X, y, theta):
    m_y = len(y)
    predictions = X.dot(theta)
    errors = np.subtract(predictions, y)
    sqrErrors = np.square(errors)
    J = 1 / (2 * m_y) * np.sum(sqrErrors)
    return J

def gradient_descent(X, y, theta, alpha, iterations):
    m_y = len(y)
    cost_history = np.zeros(iterations)
    for i in range(iterations):
        predictions = X.dot(theta)
        errors = np.subtract(predictions, y)
        sum_delta = (alpha / m_y) * X.transpose().dot(errors);
        theta = theta - sum_delta;
        cost_history[i] = compute_cost(X, y, theta)
    return theta, cost_history

"""## This block reads the dataset from the csv file and choose the target explanatory variable"""

file_path = '/content/drive/My Drive/Courses/Intro to ML/Lab2/Housing.csv'
df = pd.read_csv(file_path)
split = 0.20 # Split ratio
a = int(df.shape[0]*(1-split))

df_train = df.iloc[0:a,:]
df_valid = df.iloc[a:,:]

y_train = df_train.values[:, 0]
y_valid = df_valid.values[:, 0]

df_train1 = (df_train.iloc[:,[5,6,7,8,9,11]] == "yes").replace(True,1).replace(False,0)
df_train = pd.concat([df_train.iloc[:,[0,1,2,3,4,10,12]], df_train1], axis = 1)
df_valid1 = (df_valid.iloc[:,[5,6,7,8,9,11]] == "yes").replace(True,1).replace(False,0)
df_valid = pd.concat([df_valid.iloc[:,[0,1,2,3,4,10,12]], df_valid1], axis = 1)

"""## Problem I A: Develop a gradient decent training and evaluation code, from scratch, that predicts housing price based on the following input variables:

## Area, bedrooms, bathrooms, stories, parking
"""

df_train.iloc[:,[0,1,2,3,4,5]]

X1_train = df_train.values[:, 1]
X2_train = df_train.values[:, 2]
X3_train = df_train.values[:, 3]
X4_train = df_train.values[:, 4]
X5_train = df_train.values[:, 5]

X1_valid = df_valid.values[:, 1]
X2_valid = df_valid.values[:, 2]
X3_valid = df_valid.values[:, 3]
X4_valid = df_valid.values[:, 4]
X5_valid = df_valid.values[:, 5]

m_train = len(y_train)
m_valid = len(y_valid)
n_train = len(X1_train)
n_valid = len(X1_valid)

X_0_train = np.ones((m_train, 1))
X_1_train = X1_train.reshape(m_train, 1)
X_2_train = X2_train.reshape(m_train, 1)
X_3_train = X3_train.reshape(m_train, 1)
X_4_train = X4_train.reshape(m_train, 1)
X_5_train = X5_train.reshape(m_train, 1)
X_train = np.hstack((X_0_train, X_1_train, X_2_train, X_3_train, X_4_train, X_5_train))


X_0_valid = np.ones((m_valid, 1))
X_1_valid = X1_valid.reshape(m_valid, 1)
X_2_valid = X2_valid.reshape(m_valid, 1)
X_3_valid = X3_valid.reshape(m_valid, 1)
X_4_valid = X4_valid.reshape(m_valid, 1)
X_5_valid = X5_valid.reshape(m_valid, 1)
X_valid = np.hstack((X_0_valid, X_1_valid, X_2_valid, X_3_valid, X_4_valid, X_5_valid))

it = 100 # Maximum iterations
# alpha = 0.000000010 # Learning Rate
alpha = 0.01
# alpha =   0.000000100 # Learning Rate

# theta = np.zeros(6)
# theta = [1,1,1,1,1,1]
theta = [3,1,5,100,2,3.4]

print(f' Maximum iterations: {it}')
print(f'Learning rate is: {alpha}')
print(f'θ is: {theta}')

cost_train = compute_cost(X_train, y_train, theta)
print('The cost of the test dataset for given values of theta_0 and theta_1 =', cost_train)

cost_valid = compute_cost(X_valid, y_valid, theta)
print('The cost of the validation dataset for given values of theta_0 and theta_1 =', cost_valid)

theta, cost_history_train = gradient_descent(X_train, y_train, theta, alpha, it)
print('Final value of theta for test =', theta)

theta, cost_history_valid = gradient_descent(X_valid, y_valid, theta, alpha, it)
print('Final value of theta for validation =', theta)

# theta_valid, cost_history_valid = gradient_descent(X_valid, y_valid, theta_valid, alpha, it)
# print('Final value of theta for validation =', theta_valid)

plt.scatter(X_train[:,1], y_train, color='b', marker= '+', label= 'Training Data')
plt.plot(X_train[:,1],X_train.dot(theta), color='r', label='Linear Regression')
plt.rcParams["figure.figsize"] = (10,6)
plt.xlabel('Features')
plt.ylabel('House Price($)')
plt.title(f'LR, X1, learning rate={alpha}, iteration={it}')
plt.legend()
plt.grid()

plt.scatter(X_valid[:,1], y_valid, color='b', marker= '+', label= 'Training Data')
plt.plot(X_valid[:,1], X_valid.dot(theta), color='r', label='Linear Regression')
plt.rcParams["figure.figsize"] = (10,6)
plt.xlabel('Features')
plt.ylabel('House Price($)')
plt.title(f'LR, X1, learning rate={alpha}, iteration={it}')
plt.legend()
plt.grid()

plt.plot(range(1, it + 1), cost_history_train)
plt.plot(range(1, it + 1), cost_history_valid)

plt.rcParams["figure.figsize"] = (10,6)
plt.grid(1)
plt.xlabel('Number of iterations')
plt.ylabel('Cost (J)')
plt.title(f'Convergence, learning rate={alpha}, iteration={it}')
plt.legend()

"""# Problem II A

## Repeat problem 1 a, this time with input normalization and input standardization as part of your pre-processing logic. You need to perform two separate trainings for standardization and normalization. **In both cases, you do not need to normalize the output**

### Plot the training and validation losses for both training and validation sets based on input standardization and input normalization. Compare your training accuracy between both scaling approaches and the baseline training in problem 1 b. Which input scaling achieves the best training? Explain your results
"""

# scaler = 'normalize'
scaler = 'standard'

df_train = df.iloc[0:a,:]
df_valid = df.iloc[a:,:]
y_train = df_train.values[:, 0]
y_valid = df_valid.values[:, 0]

df_train1 = (df_train.iloc[:,[5,6,7,8,9,11]] == "yes").replace(True,1).replace(False,0)
df_train = pd.concat([df_train.iloc[:,[0,1,2,3,4,10,12]], df_train1], axis = 1)

df_valid1 = (df_valid.iloc[:,[5,6,7,8,9,11]] == "yes").replace(True,1).replace(False,0)
df_valid = pd.concat([df_valid.iloc[:,[0,1,2,3,4,10,12]], df_valid1], axis = 1)

df_train_s = df_train.drop(['price','furnishingstatus'], axis='columns')
df_valid_s = df_valid.drop(['price','furnishingstatus'], axis='columns')

if scaler == 'normalize':
    min_max_scaled= preprocessing.MinMaxScaler()
else:
    min_max_scaled= preprocessing.StandardScaler()

df_train_scaled = min_max_scaled.fit_transform(df_train_s)
df_valid_scaled = min_max_scaled.fit_transform(df_valid_s)
df_train_scaled = pd.DataFrame(df_train_scaled)
df_valid_scaled = pd.DataFrame(df_valid_scaled)
# df_train_scaled

X1_train_scaled = df_train_scaled.values[:, 0]
X2_train_scaled = df_train_scaled.values[:, 1]
X3_train_scaled = df_train_scaled.values[:, 2]
X4_train_scaled = df_train_scaled.values[:, 3]
X5_train_scaled = df_train_scaled.values[:, 4]

X1_valid_scaled = df_valid_scaled.values[:, 0]
X2_valid_scaled = df_valid_scaled.values[:, 1]
X3_valid_scaled = df_valid_scaled.values[:, 2]
X4_valid_scaled = df_valid_scaled.values[:, 3]
X5_valid_scaled = df_valid_scaled.values[:, 4]

m_train = len(y_train)
m_valid = len(y_valid)
n_train = len(X1_train_scaled)
n_valid = len(X1_valid_scaled)

X_0_train_scaled = np.ones((m_train, 1))
X_1_train_scaled = X1_train_scaled.reshape(m_train, 1)
X_2_train_scaled = X2_train_scaled.reshape(m_train, 1)
X_3_train_scaled = X3_train_scaled.reshape(m_train, 1)
X_4_train_scaled = X4_train_scaled.reshape(m_train, 1)


X_0_valid_scaled = np.ones((m_valid, 1))
X_1_valid_scaled = X1_valid_scaled.reshape(m_valid, 1)
X_2_valid_scaled = X2_valid_scaled.reshape(m_valid, 1)
X_3_valid_scaled = X3_valid_scaled.reshape(m_valid, 1)
X_4_valid_scaled = X4_valid_scaled.reshape(m_valid, 1)

X_train_scaled = np.hstack((X_0_train_scaled, X_1_train_scaled, X_2_train_scaled, X_3_train_scaled, X_4_train_scaled))
X_valid_scaled = np.hstack((X_0_valid_scaled, X_1_valid_scaled, X_2_valid_scaled, X_3_valid_scaled, X_4_valid_scaled))

it = 100 # Maximum iterations
alpha = 0.1 # Learning Rate
# alpha = 0.01 # Learning Rate

# theta_scaled = np.zeros(5)
# theta_scaled = [1,1,1,1,1]
theta_scaled = [3,1,5,100,3.4]

print(f' Maximum iterations: {it}')
print(f'Learning rate is: {alpha}')
print(f'θ is: {theta_scaled}')

cost_train_scaled = compute_cost(X_train_scaled, y_train, theta_scaled)
print('The cost of the test dataset for given values of theta_0 and theta_1 =', cost_train_scaled)

cost_valid_scaled = compute_cost(X_valid_scaled, y_valid, theta_scaled)
print('The cost of the validation dataset for given values of theta_0 and theta_1 =', cost_valid_scaled)

theta_scaled, cost_history_train_scaled = gradient_descent(X_train_scaled, y_train, theta_scaled, alpha, it)
print('Final value of theta for test =', theta_scaled)

theta_scaled, cost_history_valid_scaled = gradient_descent(X_valid_scaled, y_valid, theta_scaled, alpha, it)
print('Final value of theta for validation =', theta_scaled)

# plt.scatter(X_train_scaled[:,1], y_train, color='b', marker= '+', label= 'Training Data')
# plt.plot(X_train_scaled[:,1],X_train_scaled.dot(theta_train_scaled), color='r', label='Linear Regression')
# plt.rcParams["figure.figsize"] = (10,6)
# plt.xlabel('Input')
# plt.ylabel('House Price($)')
# plt.title(f'LR, X1, learning rate={alpha}, iteration={it}')
# plt.legend()
# plt.grid()

# plt.scatter(X_valid_scaled[:,1], y_valid, color='b', marker= '+', label= 'Training Data')
# plt.plot(X_valid_scaled[:,1], X_valid_scaled.dot(theta_valid_scaled), color='r', label='Linear Regression')
# plt.rcParams["figure.figsize"] = (10,6)
# plt.xlabel('Features')
# plt.ylabel('House Price($)')
# plt.title(f'LR, X1, learning rate={alpha}, iteration={it}')
# plt.legend()
# plt.grid()

plt.plot(range(1, it + 1), cost_history_train_scaled)
plt.plot(range(1, it + 1), cost_history_valid_scaled)

plt.rcParams["figure.figsize"] = (10,6)
plt.grid(1)
plt.xlabel('Number of iterations')
plt.ylabel('Cost (J)')
plt.title(f'Loss convergence for input={scaler}ization, learning rate={alpha}, iteration={it}')
plt.legend()

"""## Problem I B: Develop a gradient decent training and evaluation code, from scratch, that predicts housing price based on the following input variables

## Area, bedrooms, bathrooms, stories, mainroad, guestroom, basement, hotwaterheating, airconditioning, parking, prefarea
"""

df_test = df.iloc[0:a,:]
df_valid = df.iloc[a:,:]

y_test = df_test.values[:, 0]
y_valid = df_valid.values[:, 0]

df_test1 = (df_test.iloc[:,[5,6,7,8,9,11]] == "yes").replace(True,1).replace(False,0)
df_test = pd.concat([df_test.iloc[:,[0,1,2,3,4,10,12]], df_test1], axis = 1)
df_valid1 = (df_valid.iloc[:,[5,6,7,8,9,11]] == "yes").replace(True,1).replace(False,0)
df_valid = pd.concat([df_valid.iloc[:,[0,1,2,3,4,10,12]], df_valid1], axis = 1)


# df_test.iloc[:,[0,1,2,3,4,5,7,8,9,10,11,12]]
# df_valid.iloc[:,[0,1,2,3,4,10]]
# df_test
df_train

X1_train = df_train.values[:, 1]
X2_train = df_train.values[:, 2]
X3_train = df_train.values[:, 3]
X4_train = df_train.values[:, 4]
X5_train = df_train.values[:, 5]
X6_train = df_train.values[:, 7]
X7_train = df_train.values[:, 8]
X8_train = df_train.values[:, 9]
X9_train = df_train.values[:, 10]
X10_train = df_train.values[:, 11]
X11_train = df_train.values[:, 12]


X1_valid = df_valid.values[:, 1]
X2_valid = df_valid.values[:, 2]
X3_valid = df_valid.values[:, 3]
X4_valid = df_valid.values[:, 4]
X5_valid = df_valid.values[:, 5]
X6_valid = df_valid.values[:, 7]
X7_valid = df_valid.values[:, 8]
X8_valid = df_valid.values[:, 9]
X9_valid = df_valid.values[:, 10]
X10_valid = df_valid.values[:, 11]
X11_valid = df_valid.values[:, 12]

m_train = len(y_train)
m_valid = len(y_valid)
n_train = len(X1_train)
n_valid = len(X1_valid)


X_0_train = np.ones((m_train, 1))
X_1_train = X1_train.reshape(m_train, 1)
X_2_train = X2_train.reshape(m_train, 1)
X_3_train = X3_train.reshape(m_train, 1)
X_4_train = X4_train.reshape(m_train, 1)
X_5_train = X5_train.reshape(m_train, 1)
X_6_train = X6_train.reshape(m_train, 1)
X_7_train = X7_train.reshape(m_train, 1)
X_8_train = X8_train.reshape(m_train, 1)
X_9_train = X9_train.reshape(m_train, 1)
X_10_train = X10_train.reshape(m_train, 1)
X_11_train = X11_train.reshape(m_train, 1)


X_0_valid = np.ones((m_valid, 1))
X_1_valid = X1_valid.reshape(m_valid, 1)
X_2_valid = X2_valid.reshape(m_valid, 1)
X_3_valid = X3_valid.reshape(m_valid, 1)
X_4_valid = X4_valid.reshape(m_valid, 1)
X_5_valid = X5_valid.reshape(m_valid, 1)
X_6_valid = X6_valid.reshape(m_valid, 1)
X_7_valid = X7_valid.reshape(m_valid, 1)
X_8_valid = X8_valid.reshape(m_valid, 1)
X_9_valid = X9_valid.reshape(m_valid, 1)
X_10_valid = X10_valid.reshape(m_valid, 1)
X_11_valid = X11_valid.reshape(m_valid, 1)

X_train = np.hstack((X_0_train, X_1_train, X_2_train, X_3_train, X_4_train, X_5_train, X_6_train, X_7_train, X_8_train, X_9_train, X_10_train, X_11_train))
X_valid = np.hstack((X_0_valid, X_1_valid, X_2_valid, X_3_valid, X_4_valid, X_5_valid, X_6_valid, X_7_valid, X_8_valid, X_9_valid, X_10_valid, X_11_valid))

it = 500 # Maximum iterations
# alpha = 0.000000001 # Learning Rate
alpha = 0.01 # Learning Rate

# theta = np.zeros(5)
# theta = [1,1,1,1,1]
theta = [3,1,5,100,3.4,4.5,8.9,0.2,13,98,34,35.7]

print(f' Maximum iterations: {it}')
print(f'Learning rate is: {alpha}')
print(f'θ is: {theta}')

cost_test = compute_cost(X_train, y_test, theta)
print('The cost of the test dataset for given values of theta_0 and theta_1 =', cost_test)

cost_valid = compute_cost(X_valid, y_valid, theta)
print('The cost of the validation dataset for given values of theta_0 and theta_1 =', cost_valid)

theta, cost_history_train = gradient_descent(X_train, y_test, theta, alpha, it)
print('Final value of theta for test =', theta)

theta, cost_history_valid = gradient_descent(X_valid, y_valid, theta, alpha, it)
print('Final value of theta for validation =', theta)

# plt.scatter(X_train[:,1], y_train, color='b', marker= '+', label= 'Training Data')
# plt.plot(X_train[:,1],X_train.dot(theta), color='r', label='Linear Regression')
# plt.rcParams["figure.figsize"] = (10,6)
# plt.xlabel('Y')
# plt.title(f'LR, X1, learning rate={alpha}, iteration={it}')
# plt.legend()
# plt.grid()

# plt.scatter(X_valid[:,1], y_valid, color='b', marker= '+', label= 'Training Data')
# plt.plot(X_valid[:,1], X_valid.dot(theta), color='r', label='Linear Regression')
# plt.rcParams["figure.figsize"] = (10,6)
# plt.xlabel('Y')
# plt.title(f'LR, X1, learning rate={alpha}, iteration={it}')
# plt.legend()
# plt.grid()

plt.plot(range(1, it + 1), cost_history_train)
plt.plot(range(1, it + 1), cost_history_valid)

plt.rcParams["figure.figsize"] = (10,6)
plt.grid(1)
plt.xlabel('Number of iterations')
plt.ylabel('Cost (J)')
plt.title(f'Convergence, learning rate={alpha}, iteration={it}')
plt.legend()

"""## Problem II B

## Repeat problem 1 b, this time with input normalization and input standardization as part of your pre-processing logic. You need to perform two separate trainings for standardization and normalization. In both cases, you do not need to normalize the output!

### Plot the training and validation losses for both training and validation sets based on input standardization and input normalization. Compare your training accuracy between both scaling approaches and the baseline training in problem 1 b. Which input scaling achieves the best training? Explain your results
"""

scaler = 'normalize'
# scaler = 'standard'

df_train = df.iloc[0:a,:]
df_valid = df.iloc[a:,:]
y_train = df_train.values[:, 0]
y_valid = df_valid.values[:, 0]

df_train1 = (df_train.iloc[:,[5,6,7,8,9,11]] == "yes").replace(True,1).replace(False,0)
df_train = pd.concat([df_train.iloc[:,[0,1,2,3,4,10,12]], df_train1], axis = 1)

df_valid1 = (df_valid.iloc[:,[5,6,7,8,9,11]] == "yes").replace(True,1).replace(False,0)
df_valid = pd.concat([df_valid.iloc[:,[0,1,2,3,4,10,12]], df_valid1], axis = 1)

df_train_s = df_train.drop(['price','furnishingstatus'], axis='columns')
df_valid_s = df_valid.drop(['price','furnishingstatus'], axis='columns')

if scaler == 'normalize':
    min_max_scaled= preprocessing.MinMaxScaler()
else:
    min_max_scaled= preprocessing.StandardScaler()

df_train_scaled = min_max_scaled.fit_transform(df_train_s)
df_valid_scaled = min_max_scaled.fit_transform(df_valid_s)
df_train_scaled = pd.DataFrame(df_train_scaled)
df_valid_scaled = pd.DataFrame(df_valid_scaled)
df_train_scaled

X1_train_scaled = df_train_scaled.values[:, 0]
X2_train_scaled = df_train_scaled.values[:, 1]
X3_train_scaled = df_train_scaled.values[:, 2]
X4_train_scaled = df_train_scaled.values[:, 3]
X5_train_scaled = df_train_scaled.values[:, 4]
X6_train_scaled = df_train_scaled.values[:, 5]
X7_train_scaled = df_train_scaled.values[:, 6]
X8_train_scaled = df_train_scaled.values[:, 7]
X9_train_scaled = df_train_scaled.values[:, 8]
X10_train_scaled = df_train_scaled.values[:, 9]
X11_train_scaled = df_train_scaled.values[:, 10]


X1_valid_scaled = df_valid_scaled.values[:, 0]
X2_valid_scaled = df_valid_scaled.values[:, 1]
X3_valid_scaled = df_valid_scaled.values[:, 2]
X4_valid_scaled = df_valid_scaled.values[:, 3]
X5_valid_scaled = df_valid_scaled.values[:, 4]
X6_valid_scaled = df_valid_scaled.values[:, 5]
X7_valid_scaled = df_valid_scaled.values[:, 6]
X8_valid_scaled = df_valid_scaled.values[:, 7]
X9_valid_scaled = df_valid_scaled.values[:, 8]
X10_valid_scaled = df_valid_scaled.values[:, 9]
X11_valid_scaled = df_valid_scaled.values[:, 10]

m_train_scaled = len(y_train)
m_valid_scaled = len(y_valid)
n_train_scaled = len(X1_train_scaled)
n_valid_scaled = len(X1_valid_scaled)


X_0_train_scaled = np.ones((m_train_scaled, 1))
X_1_train_scaled = X1_train_scaled.reshape(m_train_scaled, 1)
X_2_train_scaled = X2_train_scaled.reshape(m_train_scaled, 1)
X_3_train_scaled = X3_train_scaled.reshape(m_train_scaled, 1)
X_4_train_scaled = X4_train_scaled.reshape(m_train_scaled, 1)
X_5_train_scaled = X5_train_scaled.reshape(m_train_scaled, 1)
X_6_train_scaled = X6_train_scaled.reshape(m_train_scaled, 1)
X_7_train_scaled = X7_train_scaled.reshape(m_train_scaled, 1)
X_8_train_scaled = X8_train_scaled.reshape(m_train_scaled, 1)
X_9_train_scaled = X9_train_scaled.reshape(m_train_scaled, 1)
X_10_train_scaled = X10_train_scaled.reshape(m_train_scaled, 1)
X_11_train_scaled = X11_train_scaled.reshape(m_train_scaled, 1)


X_0_valid_scaled = np.ones((m_valid_scaled, 1))
X_1_valid_scaled = X1_valid_scaled.reshape(m_valid_scaled, 1)
X_2_valid_scaled = X2_valid_scaled.reshape(m_valid_scaled, 1)
X_3_valid_scaled = X3_valid_scaled.reshape(m_valid_scaled, 1)
X_4_valid_scaled = X4_valid_scaled.reshape(m_valid_scaled, 1)
X_5_valid_scaled = X5_valid_scaled.reshape(m_valid_scaled, 1)
X_6_valid_scaled = X6_valid_scaled.reshape(m_valid_scaled, 1)
X_7_valid_scaled = X7_valid_scaled.reshape(m_valid_scaled, 1)
X_8_valid_scaled = X8_valid_scaled.reshape(m_valid_scaled, 1)
X_9_valid_scaled = X9_valid_scaled.reshape(m_valid_scaled, 1)
X_10_valid_scaled = X10_valid_scaled.reshape(m_valid_scaled, 1)
X_11_valid_scaled = X11_valid_scaled.reshape(m_valid_scaled, 1)

X_train_scaled = np.hstack((X_0_train_scaled, X_1_train_scaled, X_2_train_scaled, X_3_train_scaled, X_4_train_scaled, X_5_train_scaled, X_6_train_scaled, X_7_train_scaled, X_8_train_scaled, X_9_train_scaled, X_10_train_scaled, X_11_train_scaled))
X_valid_scaled = np.hstack((X_0_valid_scaled, X_1_valid_scaled, X_2_valid_scaled, X_3_valid_scaled, X_4_valid_scaled, X_5_valid_scaled, X_6_valid_scaled, X_7_valid_scaled, X_8_valid_scaled, X_9_valid_scaled, X_10_valid_scaled, X_11_valid_scaled))

it = 500 # Maximum iterations
# alpha = 0.000000001 # Learning Rate
alpha = 0.01 # Learning Rate

# theta = np.zeros(5)
# theta_scaled = [1,1,1,1,1]
theta_scaled = [3,1,5,100,3.4,4.5,8.9,0.2,13,98,34,35.7]

print(f' Maximum iterations: {it}')
print(f'Learning rate is: {alpha}')
print(f'θ is: {theta_scaled}')

cost_train_scaled = compute_cost(X_train_scaled, y_train, theta_scaled)
print('The cost of the test dataset for given values of theta_0 and theta_1 =', cost_train_scaled)

cost_valid_scaled = compute_cost(X_valid_scaled, y_valid, theta_scaled)
print('The cost of the validation dataset for given values of theta_0 and theta_1 =', cost_valid_scaled)

theta_scaled, cost_history_train_scaled = gradient_descent(X_train_scaled, y_train, theta_scaled, alpha, it)
print('Final value of theta for test =', theta_scaled)

theta_scaled, cost_history_valid_scaled = gradient_descent(X_valid_scaled, y_valid, theta_scaled, alpha, it)
print('Final value of theta for validation =', theta_scaled)

plt.plot(range(1, it + 1), cost_history_train_scaled)
plt.plot(range(1, it + 1), cost_history_valid_scaled)

plt.rcParams["figure.figsize"] = (10,6)
plt.grid(1)
plt.xlabel('Number of iterations')
plt.ylabel('Cost (J)')
plt.title(f'Loss convergence for input={scaler}ization, learning rate={alpha}, iteration={it}')
plt.legend()

"""## Problem III

###  A: Repeat problem 2 a, this time by adding a parameters penalty to your loss function. Note that in this case, you need to modify the gradient decent logic for your training set, but you don’t need to change your loss for the evaluation set.  

### Plot your results (both training and evaluation losses) for the best input scaling approach (standardization or normalization). Explain your results and compare them against problem 2 a.
"""

def compute_cost_reg(X, y, theta, lam):
    m_y = len(y)
    predictions = X.dot(theta)
    errors = np.subtract(predictions, y)
    sqrErrors = np.square(errors)
    J = 1 / (2 * m_y) * np.sum(sqrErrors) + lam / (2* m_y) * np.sum(theta[1:])
    return J

def gradient_descent_reg(X, y, theta, alpha, iterations, lam):
    m_y = len(y)
    cost_history = np.zeros(iterations)
    for i in range(iterations):
        predictions = X.dot(theta)
        errors = np.subtract(predictions, y)
        sum_delta = (alpha / m_y) * X.transpose().dot(errors);
        theta = theta - sum_delta;
        cost_history[i] = compute_cost_reg(X, y, theta, lam)
    return theta, cost_history

# scaler = 'normalize'
scaler = 'standard'

df_train = df.iloc[0:a,:]
df_valid = df.iloc[a:,:]
y_train = df_train.values[:, 0]
y_valid = df_valid.values[:, 0]

df_train1 = (df_train.iloc[:,[5,6,7,8,9,11]] == "yes").replace(True,1).replace(False,0)
df_train = pd.concat([df_train.iloc[:,[0,1,2,3,4,10,12]], df_train1], axis = 1)

df_valid1 = (df_valid.iloc[:,[5,6,7,8,9,11]] == "yes").replace(True,1).replace(False,0)
df_valid = pd.concat([df_valid.iloc[:,[0,1,2,3,4,10,12]], df_valid1], axis = 1)

df_train_s = df_train.drop(['price','furnishingstatus'], axis='columns')
df_valid_s = df_valid.drop(['price','furnishingstatus'], axis='columns')

if scaler == 'normalize':
    min_max_scaled= preprocessing.MinMaxScaler()
else:
    min_max_scaled= preprocessing.StandardScaler()

df_train_scaled = min_max_scaled.fit_transform(df_train_s)
df_valid_scaled = min_max_scaled.fit_transform(df_valid_s)
df_train_scaled = pd.DataFrame(df_train_scaled)
df_valid_scaled = pd.DataFrame(df_valid_scaled)

X1_train_scaled = df_train_scaled.values[:, 0]
X2_train_scaled = df_train_scaled.values[:, 1]
X3_train_scaled = df_train_scaled.values[:, 2]
X4_train_scaled = df_train_scaled.values[:, 3]
X5_train_scaled = df_train_scaled.values[:, 4]

X1_valid_scaled = df_valid_scaled.values[:, 0]
X2_valid_scaled = df_valid_scaled.values[:, 1]
X3_valid_scaled = df_valid_scaled.values[:, 2]
X4_valid_scaled = df_valid_scaled.values[:, 3]
X5_valid_scaled = df_valid_scaled.values[:, 4]

m_train = len(y_train)
m_valid = len(y_valid)
n_train = len(X1_train_scaled)
n_valid = len(X1_valid_scaled)

X_0_train_scaled = np.ones((m_train, 1))
X_1_train_scaled = X1_train_scaled.reshape(m_train, 1)
X_2_train_scaled = X2_train_scaled.reshape(m_train, 1)
X_3_train_scaled = X3_train_scaled.reshape(m_train, 1)
X_4_train_scaled = X4_train_scaled.reshape(m_train, 1)


X_0_valid_scaled = np.ones((m_valid, 1))
X_1_valid_scaled = X1_valid_scaled.reshape(m_valid, 1)
X_2_valid_scaled = X2_valid_scaled.reshape(m_valid, 1)
X_3_valid_scaled = X3_valid_scaled.reshape(m_valid, 1)
X_4_valid_scaled = X4_valid_scaled.reshape(m_valid, 1)

X_train_scaled = np.hstack((X_0_train_scaled, X_1_train_scaled, X_2_train_scaled, X_3_train_scaled, X_4_train_scaled))
X_valid_scaled = np.hstack((X_0_valid_scaled, X_1_valid_scaled, X_2_valid_scaled, X_3_valid_scaled, X_4_valid_scaled))

it = 500 # Maximum iterations
# alpha = 0.1 # Learning Rate
alpha = 0.01 # Learning Rate

# theta_scaled = np.zeros(5)
# theta_scaled = [1,1,1,1,1]
theta_scaled = [3,1,5,100,3.4]

print(f' Maximum iterations: {it}')
print(f'Learning rate is: {alpha}')
print(f'θ is: {theta_scaled}')

# cost_train_scaled = compute_cost(X_train_scaled, y_train, theta_scaled)
cost_train_scaled = compute_cost_reg(X_train_scaled, y_train, theta_scaled, lam=0)
print('The cost of the test dataset for given values of theta_0 and theta_1 =', cost_train_scaled)

cost_valid_scaled = compute_cost(X_valid_scaled, y_valid, theta_scaled)
print('The cost of the validation dataset for given values of theta_0 and theta_1 =', cost_valid_scaled)

# theta_scaled, cost_history_train_scaled = gradient_descent(X_train_scaled, y_train, theta_scaled, alpha, it)
theta_scaled, cost_history_train_scaled = gradient_descent_reg(X_train_scaled, y_train, theta_scaled, alpha, it, lam=0)
print('Final value of theta for test =', theta_scaled)

theta_scaled, cost_history_valid_scaled = gradient_descent(X_valid_scaled, y_valid, theta_scaled, alpha, it)
print('Final value of theta for validation =', theta_scaled)

# plt.scatter(X_train_scaled[:,1], y_train, color='b', marker= '+', label= 'Training Data')
# plt.plot(X_train_scaled[:,1],X_train_scaled.dot(theta_train_scaled), color='r', label='Linear Regression')
# plt.rcParams["figure.figsize"] = (10,6)
# plt.xlabel('Input')
# plt.ylabel('House Price($)')
# plt.title(f'LR, X1, learning rate={alpha}, iteration={it}')
# plt.legend()
# plt.grid()

# plt.scatter(X_valid_scaled[:,1], y_valid, color='b', marker= '+', label= 'Training Data')
# plt.plot(X_valid_scaled[:,1], X_valid_scaled.dot(theta_valid_scaled), color='r', label='Linear Regression')
# plt.rcParams["figure.figsize"] = (10,6)
# plt.xlabel('Features')
# plt.ylabel('House Price($)')
# plt.title(f'LR, X1, learning rate={alpha}, iteration={it}')
# plt.legend()
# plt.grid()

plt.plot(range(1, it + 1), cost_history_train_scaled)
plt.plot(range(1, it + 1), cost_history_valid_scaled)

plt.rcParams["figure.figsize"] = (10,6)
plt.grid(1)
plt.xlabel('Number of iterations')
plt.ylabel('Cost (J)')
plt.title(f'Loss convergence for input={scaler}ization, learning rate={alpha}, iteration={it}')
plt.legend()

"""### B: Repeat problem 2 b, this time by adding a parameters penalty to your loss function. Note that in this case, you need to modify the gradient decent logic for your training set, but you don’t need to change your loss for the evaluation set.

### Plot your results (both training and evaluation losses) for the best input scaling approach (standardization or normalization). Explain your results and compare them against problem 2 a.
"""

scaler = 'normalize'
# scaler = 'standard'


df_train = df.iloc[0:a,:]
df_valid = df.iloc[a:,:]

y_train = df_train.values[:, 0]
y_valid = df_valid.values[:, 0]

df_train1 = (df_train.iloc[:,[5,6,7,8,9,11]] == "yes").replace(True,1).replace(False,0)
df_train = pd.concat([df_train.iloc[:,[0,1,2,3,4,10,12]], df_train1], axis = 1)
df_valid1 = (df_valid.iloc[:,[5,6,7,8,9,11]] == "yes").replace(True,1).replace(False,0)
df_valid = pd.concat([df_valid.iloc[:,[0,1,2,3,4,10,12]], df_valid1], axis = 1)

df_train_s = df_train.drop(['price','furnishingstatus'], axis='columns')
df_valid_s = df_valid.drop(['price','furnishingstatus'], axis='columns')

if scaler == 'normalize':
    min_max= preprocessing.MinMaxScaler()
else:
    min_max= preprocessing.StandardScaler()

df_train_scaled = min_max_scaled.fit_transform(df_train_s)
df_valid_scaled = min_max_scaled.fit_transform(df_valid_s)
df_train_scaled = pd.DataFrame(df_train_scaled)
df_valid_scaled = pd.DataFrame(df_valid_scaled)

X1_train_scaled = df_train_scaled.values[:, 0]
X2_train_scaled = df_train_scaled.values[:, 1]
X3_train_scaled = df_train_scaled.values[:, 2]
X4_train_scaled = df_train_scaled.values[:, 3]
X5_train_scaled = df_train_scaled.values[:, 4]
X6_train_scaled = df_train_scaled.values[:, 5]
X7_train_scaled = df_train_scaled.values[:, 6]
X8_train_scaled = df_train_scaled.values[:, 7]
X9_train_scaled = df_train_scaled.values[:, 8]
X10_train_scaled = df_train_scaled.values[:, 9]
X11_train_scaled = df_train_scaled.values[:, 10]


X1_valid_scaled = df_valid_scaled.values[:, 0]
X2_valid_scaled = df_valid_scaled.values[:, 1]
X3_valid_scaled = df_valid_scaled.values[:, 2]
X4_valid_scaled = df_valid_scaled.values[:, 3]
X5_valid_scaled = df_valid_scaled.values[:, 4]
X6_valid_scaled = df_valid_scaled.values[:, 5]
X7_valid_scaled = df_valid_scaled.values[:, 6]
X8_valid_scaled = df_valid_scaled.values[:, 7]
X9_valid_scaled = df_valid_scaled.values[:, 8]
X10_valid_scaled = df_valid_scaled.values[:, 9]
X11_valid_scaled = df_valid_scaled.values[:, 10]

m_train_scaled = len(y_train)
m_valid_scaled = len(y_valid)
n_train_scaled = len(X1_train_scaled)
n_valid_scaled = len(X1_valid_scaled)


X_0_train_scaled = np.ones((m_train_scaled, 1))
X_1_train_scaled = X1_train_scaled.reshape(m_train_scaled, 1)
X_2_train_scaled = X2_train_scaled.reshape(m_train_scaled, 1)
X_3_train_scaled = X3_train_scaled.reshape(m_train_scaled, 1)
X_4_train_scaled = X4_train_scaled.reshape(m_train_scaled, 1)
X_5_train_scaled = X5_train_scaled.reshape(m_train_scaled, 1)
X_6_train_scaled = X6_train_scaled.reshape(m_train_scaled, 1)
X_7_train_scaled = X7_train_scaled.reshape(m_train_scaled, 1)
X_8_train_scaled = X8_train_scaled.reshape(m_train_scaled, 1)
X_9_train_scaled = X9_train_scaled.reshape(m_train_scaled, 1)
X_10_train_scaled = X10_train_scaled.reshape(m_train_scaled, 1)
X_11_train_scaled = X11_train_scaled.reshape(m_train_scaled, 1)


X_0_valid_scaled = np.ones((m_valid_scaled, 1))
X_1_valid_scaled = X1_valid_scaled.reshape(m_valid_scaled, 1)
X_2_valid_scaled = X2_valid_scaled.reshape(m_valid_scaled, 1)
X_3_valid_scaled = X3_valid_scaled.reshape(m_valid_scaled, 1)
X_4_valid_scaled = X4_valid_scaled.reshape(m_valid_scaled, 1)
X_5_valid_scaled = X5_valid_scaled.reshape(m_valid_scaled, 1)
X_6_valid_scaled = X6_valid_scaled.reshape(m_valid_scaled, 1)
X_7_valid_scaled = X7_valid_scaled.reshape(m_valid_scaled, 1)
X_8_valid_scaled = X8_valid_scaled.reshape(m_valid_scaled, 1)
X_9_valid_scaled = X9_valid_scaled.reshape(m_valid_scaled, 1)
X_10_valid_scaled = X10_valid_scaled.reshape(m_valid_scaled, 1)
X_11_valid_scaled = X11_valid_scaled.reshape(m_valid_scaled, 1)

X_train_scaled = np.hstack((X_0_train_scaled, X_1_train_scaled, X_2_train_scaled, X_3_train_scaled, X_4_train_scaled, X_5_train_scaled, X_6_train_scaled, X_7_train_scaled, X_8_train_scaled, X_9_train_scaled, X_10_train_scaled, X_11_train_scaled))
X_valid_scaled = np.hstack((X_0_valid_scaled, X_1_valid_scaled, X_2_valid_scaled, X_3_valid_scaled, X_4_valid_scaled, X_5_valid_scaled, X_6_valid_scaled, X_7_valid_scaled, X_8_valid_scaled, X_9_valid_scaled, X_10_valid_scaled, X_11_valid_scaled))

it = 500 # Maximum iterations
# alpha = 0.000000001 # Learning Rate
alpha = 0.01 # Learning Rate

# theta = np.zeros(5)
# theta = [1,1,1,1,1]
theta_scaled = [3,1,5,100,3.4,4.5,8.9,0.2,13,98,34,35.7]

print(f' Maximum iterations: {it}')
print(f'Learning rate is: {alpha}')
print(f'θ is: {theta}')

cost_train_scaled = compute_cost_reg(X_train_scaled, y_train, theta_scaled, lam=0)
print('The cost of the test dataset for given values of theta_0 and theta_1 =', cost_train_scaled)

cost_valid_scaled = compute_cost(X_valid_scaled, y_valid, theta_scaled)
print('The cost of the validation dataset for given values of theta_0 and theta_1 =', cost_valid_scaled)

theta_scaled, cost_history_train_scaled = gradient_descent_reg(X_train_scaled, y_train, theta_scaled, alpha, it, lam=0)
print('Final value of theta for test =', theta_scaled)

theta_scaled, cost_history_valid_scaled = gradient_descent(X_valid_scaled, y_valid, theta_scaled, alpha, it)
print('Final value of theta for validation =', theta_scaled)

plt.plot(range(1, it + 1), cost_history_train_scaled)
plt.plot(range(1, it + 1), cost_history_valid_scaled)

plt.rcParams["figure.figsize"] = (10,6)
plt.grid(1)
plt.xlabel('Number of iterations')
plt.ylabel('Cost (J)')
plt.title(f'Loss convergence for input={scaler}ization, learning rate={alpha}, iteration={it}')
plt.legend()
