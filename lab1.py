# -*- coding: utf-8 -*-
"""Lab1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1sGglFV9S4P2uh4WgoL1OrYoLy0Ws_4fX

## Lab 1
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

"""## Parameters are set here"""

ev=3
it = 1500;
alpha = 0.05;
# alpha = 0.03;
# alpha = 0.08;
theta = np.zeros(2)
print(f'Explanatory varibale is: X{ev}')
print(f'Iterations are: {it}')
print(f'Learning rate is: {alpha}')
print(f'θ is: {theta}')

"""## Cost function and the Gradient Descent Algorithm are defined here"""

def compute_cost(X, y, theta):
 predictions = X.dot(theta)
 errors = np.subtract(predictions, y)
 sqrErrors = np.square(errors)
 J = 1 / (2 * m) * np.sum(sqrErrors)
 return J

def gradient_descent(X, y, theta, alpha, iterations):
    cost_history = np.zeros(iterations)
    for i in range(iterations):
        predictions = X.dot(theta)
        errors = np.subtract(predictions, y)
        sum_delta = (alpha / m) * X.transpose().dot(errors);
        theta = theta - sum_delta;
        cost_history[i] = compute_cost(X, y, theta)
    return theta, cost_history

"""## This block reads the dataset from the csv file and choose the target explanatory variable"""

df=pd.read_csv("HW1.csv")
y = df.values[:, 3]

"""# Problem I

## Task 1 and 2: Report the linear model you found for each explanatory variable and Plot the final regression model and loss over the iteration per each explanatory variable

### Explanatory Varibale X1
"""

X = df.values[:, 0]

m = len(y)
n = len(X)

X_0 = np.ones((m, 1))
X_1 = X.reshape(m, 1)
X = np.hstack((X_0, X_1))

cost = compute_cost(X, y, theta)
print('The cost for given values of theta_0 and theta_1 =', cost)

theta, cost_history = gradient_descent(X, y, theta, alpha, it)
print('Final value of theta =', theta)
print('cost_history =', cost_history)

s=(X.dot(theta)[0]-X.dot(theta)[1])/(X[0,1]-X[1,1])
y_i=X.dot(theta)[0]- s*(X[0,1])
print(f'Slope is:{s}')
print(f'Y intercept is:{y_i}')
print(f'Model is:Y = {s} * X + {y_i}')

plt.scatter(X[:,1], y, color='b', marker= '+', label= 'Training Data')
plt.plot(X[:,1],X.dot(theta), color='r', label='Linear Regression')
plt.rcParams["figure.figsize"] = (10,6)
plt.xlabel('Y')
plt.ylabel(f'X{ev}')
plt.title(f'LR, X1, learning rate={alpha}, iteration={it}')
plt.legend()

"""### Explanatory Varibale X2"""

X = df.values[:, 1]

m = len(y)
n = len(X)

X_0 = np.ones((m, 1))
X_1 = X.reshape(m, 1)
X = np.hstack((X_0, X_1))

cost = compute_cost(X, y, theta)
print('The cost for given values of theta_0 and theta_1 =', cost)

theta, cost_history = gradient_descent(X, y, theta, alpha, it)
print('Final value of theta =', theta)
print('cost_history =', cost_history)

s=(X.dot(theta)[0]-X.dot(theta)[1])/(X[0,1]-X[1,1])
y_i=X.dot(theta)[0]- s*(X[0,1])
print(f'Slope is:{s}')
print(f'Y intercept is:{y_i}')
print(f'Model is:Y = {s} * X + {y_i}')

plt.scatter(X[:,1], y, color='b', marker= '+', label= 'Training Data')
plt.plot(X[:,1],X.dot(theta), color='r', label='Linear Regression')
plt.rcParams["figure.figsize"] = (10,6)
plt.xlabel('Y')
plt.ylabel('X2')
plt.title(f'LR, X2, learning rate={alpha}, iteration={it}')
plt.legend()

"""### Explanatory Varibale X3"""

X = df.values[:, 2]

m = len(y)
n = len(X)

X_0 = np.ones((m, 1))
X_1 = X.reshape(m, 1)
X = np.hstack((X_0, X_1))

cost = compute_cost(X, y, theta)
print('The cost for given values of theta_0 and theta_1 =', cost)

theta, cost_history = gradient_descent(X, y, theta, alpha, it)
print('Final value of theta =', theta)
print('cost_history =', cost_history)

s=(X.dot(theta)[0]-X.dot(theta)[1])/(X[0,1]-X[1,1])
y_i=X.dot(theta)[0]- s*(X[0,1])
print(f'Slope is:{s}')
print(f'Y intercept is:{y_i}')
print(f'Model is:Y = {s} * X + {y_i}')

plt.scatter(X[:,1], y, color='b', marker= '+', label= 'Training Data')
plt.plot(X[:,1],X.dot(theta), color='r', label='Linear Regression')
plt.rcParams["figure.figsize"] = (10,6)
plt.xlabel('Y')
plt.ylabel('X3')
plt.title(f'LR, X3, learning rate={alpha}, iteration={it}')
plt.legend()

"""## Task 3: Which explanatory variable has the lower loss (cost) for explaining the output (Y)?
### Based on the cost function plot X1 has the lowest cost among all explanatory variables
"""

for ev in {1,2,3}:
    theta = np.zeros(2)
    if  ev == 1:
        X = df.values[:, 0]
    elif ev == 2:
        X = df.values[:, 1]
    elif ev == 3:
        X = df.values[:, 2]
    X_0 = np.ones((m, 1))
    X_1 = X.reshape(m, 1)
    X = np.hstack((X_0, X_1))
    theta, cost_history = gradient_descent(X, y, theta, alpha, it)
    plt.plot(range(1, it + 1),cost_history, label=f'X{ev}')

plt.rcParams["figure.figsize"] = (10,6)
plt.grid(1)
plt.xlabel('Number of iterations')
plt.ylabel('Cost (J)')
plt.title(f'Convergence, learning rate={alpha}, iteration={it}')
plt.legend()

"""### Task 4: Based on your training observations, describe the impact of the different learning rates on the final loss and number of training iterations

### Answer: Increasing the learning rate will decrease the cost function

### Explanatory Varibale X1
"""

X = df.values[:, 0]

m = len(y)
n = len(X)

X_0 = np.ones((m, 1))
X_1 = X.reshape(m, 1)
X = np.hstack((X_0, X_1))


print('The cost for given values of theta_0 and theta_1 =', cost)

for alpha in {0.02,0.04,0.06,0.08,0.1}:
    theta = np.zeros(2)
    cost = compute_cost(X, y, theta)
    theta, cost_history = gradient_descent(X, y, theta, alpha, it)
    plt.plot(range(1, it + 1),cost_history, label=f'Learning rate {alpha}')

    plt.rcParams["figure.figsize"] = (10,6)
    plt.grid(1)
    plt.xlabel('Number of iterations')
    plt.ylabel('Cost (J)')
    plt.title(f'Convergence, X1, iteration={it}')
    plt.legend()

"""### Explanatory Varibale X2"""

X = df.values[:, 1]

m = len(y)
n = len(X)

X_0 = np.ones((m, 1))
X_1 = X.reshape(m, 1)
X = np.hstack((X_0, X_1))

for alpha in {0.02,0.04,0.06,0.08,0.1}:
    theta = np.zeros(2)
    cost = compute_cost(X, y, theta)
    theta, cost_history = gradient_descent(X, y, theta, alpha, it)
    plt.plot(range(1, it + 1),cost_history, label=f'Learning rate {alpha}')

    plt.rcParams["figure.figsize"] = (10,6)
    plt.grid(1)
    plt.xlabel('Number of iterations')
    plt.ylabel('Cost (J)')
    plt.title(f'Convergence, X1, iteration={it}')
    plt.legend()

"""### Explanatory Variable X3"""

X = df.values[:, 2]

m = len(y)
n = len(X)

X_0 = np.ones((m, 1))
X_1 = X.reshape(m, 1)
X = np.hstack((X_0, X_1))

for alpha in {0.02,0.04,0.06,0.08,0.1}:
    theta = np.zeros(2)
    cost = compute_cost(X, y, theta)
    theta, cost_history = gradient_descent(X, y, theta, alpha, it)
    plt.plot(range(1, it + 1),cost_history, label=f'Learning rate {alpha}')

    plt.rcParams["figure.figsize"] = (10,6)
    plt.grid(1)
    plt.xlabel('Number of iterations')
    plt.ylabel('Cost (J)')
    plt.title(f'Convergence, X1, iteration={it}')
    plt.legend()

"""# Problem II

## Task 1

#### All explanatory varibales merges into one column and the output (y) will replicate in the same column for three times to create one inout (X) and one output(y)
"""

X1 = df.values[:, 0]
X2 = df.values[:, 1]
X3 = df.values[:, 2]
X=np.append(X1,X2)
X=np.append(X,X3)

y= np.append(y,y)
y1 = df.values[:, 3]
y=np.append(y,y1)

m = len(y)
n = len(X)

X_0 = np.ones((m, 1))
X_1 = X.reshape(m, 1)
X = np.hstack((X_0, X_1))

cost = compute_cost(X, y, theta)
print('The cost for given values of theta_0 and theta_1 =', cost)

theta, cost_history = gradient_descent(X, y, theta, alpha, it)
print('Final value of theta =', theta)
print('cost_history =', cost_history)

s=(X.dot(theta)[0]-X.dot(theta)[1])/(X[0,1]-X[1,1])
y_i=X.dot(theta)[0]- s*(X[0,1])
print(f'Slope is:{s}')
print(f'Y intercept is:{y_i}')
print(f'Model is:Y = {s} * X + {y_i}')

plt.scatter(X[:,1], y, color='b', marker= '+', label= 'Training Data')
plt.plot(X[:,1],X.dot(theta), color='r', label='Linear Regression')
plt.rcParams["figure.figsize"] = (10,6)
plt.xlabel('Y')
plt.ylabel('X')
plt.title(f'LR, learning rate={alpha}, iteration={it}')
plt.legend()

"""## Task 2: Plot loss over the iteration"""

theta = np.zeros(2)
theta, cost_history = gradient_descent(X, y, theta, alpha, it)
plt.plot(range(1, it + 1),cost_history)

plt.rcParams["figure.figsize"] = (10,6)
plt.grid(1)
plt.xlabel('Number of iterations')
plt.ylabel('Cost (J)')
plt.title(f'Convergence, learning rate={alpha}, iteration={it}')
plt.legend()

"""## Task 3: Based on your training observations, describe the impact of the different learning rates on the final loss and number of training iterations."""

for alpha in {0.02,0.04,0.06,0.08,0.1}:
    theta = np.zeros(2)
    cost = compute_cost(X, y, theta)
    theta, cost_history = gradient_descent(X, y, theta, alpha, it)
    plt.plot(range(1, it + 1),cost_history, label=f'Learning rate {alpha}')

    plt.rcParams["figure.figsize"] = (10,6)
    plt.grid(1)
    plt.xlabel('Number of iterations')
    plt.ylabel('Cost (J)')
    plt.title(f'Convergence, iteration={it}')
    plt.legend()

"""## Task 4: Predict the value of y for new (X1, X2, X3) values (1, 1, 1), for (2, 0, 4), and for (3, 2, 1)"""

A1=[1,1,1]
A2=[2,0,4]
A3=[3,2,1]

i=0
for j in A1:
    A1[i]=s*j
    i+=1
print(f'Estimation for [1,1,1] is: {A1}')

i=0
for j in A2:
    A2[i]=s*j
    i+=1
print(f'Estimation for [1,1,1] is: {A2}')

i=0
for j in A3:
    A3[i]=s*j
    i+=1
print(f'Estimation for [1,1,1] is: {A3}')