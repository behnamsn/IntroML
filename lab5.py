# -*- coding: utf-8 -*-
"""Lab5.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1tGk7WgoAqGB2k0gaiPxK19rXEJiChoaC

## Lab 5
### Name: Behnam Sobhani Nadri
### Student ID: 801368949

## All libraries that we use in the lab is defined here
"""

import warnings
import pandas as pd
import numpy as np
import seaborn as sb
import torch
from google.colab import drive
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from sklearn import svm
from sklearn import preprocessing
from sklearn.svm import SVR
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB

from sklearn.metrics import confusion_matrix
from sklearn import metrics
from sklearn.metrics import mean_squared_error

drive.mount('/content/drive')

"""## **Problem I**
###In our temperature prediction example discussed in class, let’s change our model to a nonlinear system. Consider the following description for our model:

###w2 * t_u ** 2 + w1 * t_u + b

## **Problem I. A**  
###Modify the training loop properly to accommodate this redefinition.
"""

def non_l_model(t_u, params):
    w2, w1, b = params
    return w2 * t_u ** 2+ w1 * t_u + b

def loss_fn(t_p, t_c):
    squared_diffs = (t_p - t_c)**2
    return squared_diffs.mean()

def training_loop(n_epochs, learning_rate, params, t_u, t_c):

    loss_track = np.zeros((n_epochs,1))

    for epoch in range(1, n_epochs+1):
        if params.grad is not None:
              params.grad.zero_()
        # Forward pass: Compute predicted y by passing x to the model
        t_p = non_l_model(t_u, params)
        # t_p=l_model(t_u,params)

        # Compute and print loss
        loss = loss_fn(t_p, t_c)

        # Zero gradients, perform a backward pass, and update the weights.
        loss.backward()

        with torch.no_grad():
            params -= learning_rate * params.grad
            params.grad.zero_()  # Reset gradients for next iteration

        if epoch % 500 == 0:
            print(f'Epoch {epoch}, Loss {loss.item()}')
        loss_track[epoch-1] = loss.item()
    # Final parameters
    # print(f'Final parameters: w2={params[0].item()}, w1={params[1].item()}, b={params[2].item()}')
    return loss_track

t_c = [0.5, 14.0, 15.0, 28.0, 11.0, 8.0, 3.0, -4.0, 6.0, 13.0, 21.0]
t_u = [35.7, 55.9, 58.2, 81.9, 56.3, 48.9, 33.9, 21.8, 48.4, 60.4, 68.4]

t_c = torch.tensor(t_c)
t_u = torch.tensor(t_u)

t_u_min = t_u.min()
t_u_max = t_u.max()

t_un = (t_u - t_u_min) / (t_u_max - t_u_min)
t_un

"""## **Problem I. B**
###Use 5000 epochs for your training. Explore different learning rates from 0.1 to 0.0001 (you need four separate trainings). Report your loss for every 500 epochs per training.




"""

learning_rate = [0.004,0.02,0.08,0.099]
n_epochs = 5000
loss_tr=np.zeros((n_epochs,len(learning_rate)+2))

for i in range(n_epochs):
    loss_tr[i,0]=i+1

i=1
for lr in learning_rate:
      print()
      print (f'Trainings with Learning Rate = {lr}')
      print()
      params = torch.tensor([1.0, 1.0, 0.0],requires_grad=True)
      loss_tr[:,i]= training_loop(n_epochs = 5000,
                        learning_rate = lr,
                        params = torch.tensor([1.0, 1.0, 0.0],requires_grad=True),
                        t_u = t_un,
                        t_c = t_c).squeeze()
      i+=1

plt.plot(loss_tr[:1000,0], loss_tr[:1000,1],label=f'Learning Rate {learning_rate[0]}')
plt.plot(loss_tr[:1000,0], loss_tr[:1000,2],label=f'Learning Rate {learning_rate[1]}')
plt.plot(loss_tr[:1000,0], loss_tr[:1000,3],label=f'Learning Rate {learning_rate[2]}')
plt.plot(loss_tr[:1000,0], loss_tr[:1000,4],label=f'Learning Rate {learning_rate[3]}')

plt.rcParams["figure.figsize"] = (10,6)
plt.grid(1)
plt.xlabel('Number of iterations')
plt.ylabel('Cost (J)')
plt.title(f'Loss convergence')
plt.legend()

"""##**Problem I. C**

###Pick the best non-linear model and compare your final best loss against the linear model that we did during the lecture. For this, visualize the non-linear model against the linear model over the input dataset, as we did during the lecture. Is the actual result better or worse than our baseline linear model?
"""

def l_model(t_u,params):
    w, b = params
    return w * t_u + b

def training_loop(n_epochs, learning_rate, params, t_u, t_c):
    loss_track = np.zeros((n_epochs,1))
    for epoch in range(1, n_epochs+1):
        if params.grad is not None:
              params.grad.zero_()
        # Forward pass: Compute predicted y by passing x to the model
        t_p=l_model(t_u,params)

        # Compute and print loss
        loss = loss_fn(t_p, t_c)

        # Zero gradients, perform a backward pass, and update the weights.
        loss.backward()

        with torch.no_grad():
            params -= learning_rate * params.grad
            params.grad.zero_()  # Reset gradients for next iteration

        # if epoch % 500 == 0:
        #     print(f'Epoch {epoch}, Loss {loss.item()}')
        loss_track[epoch-1] = loss.item()
    # Final parameters
    # print(f'Final parameters: w2={params[0].item()}, w1={params[1].item()}, b={params[2].item()}')
    return loss_track

learning_rate = 1e-2
n_epochs = 5000

params = torch.tensor([1.0, 0.0],requires_grad=True)

loss_tr[:,5] = training_loop(n_epochs = 5000,
                  learning_rate = lr,
                  params = torch.tensor([1.0, 0.0],requires_grad=True),
                  t_u = t_un,
                  t_c = t_c).squeeze()

plt.plot(loss_tr[:1000,0], loss_tr[:1000,4],label='Non-linear Model')
plt.plot(loss_tr[:1000,0], loss_tr[:1000,5],label='Linear Model')

plt.rcParams["figure.figsize"] = (10,6)
plt.grid(1)
plt.xlabel('Number of iterations')
plt.ylabel('Cost (J)')
plt.title(f'Loss convergence')
plt.legend()

"""## **Problem II. A**
### Develop preprocessing and a training loop to train a linear regression model that predicts housing price based on the following input variables:

###area, bedrooms, bathrooms, stories, parking

###For this, you need to use the housing dataset. For training and validation use 80% (training) and 20% (validation) split. Identify the best parameters for your linear regression model, based on the above input variables. In this case, you will have six parameters:




"""

file_path = '/content/drive/My Drive/Courses/Intro to ML/Lab2/Housing.csv'
df_house = pd.read_csv(file_path)
# Select relevant features
features = df_house[['area', 'bedrooms', 'bathrooms', 'stories', 'parking']]
target = df_house['price']

# Convert to torch tensors
features = torch.tensor(features.values, dtype=torch.float32)
target = torch.tensor(target.values, dtype=torch.float32).view(-1, 1)

# Split into training and validation sets (80% training, 20% validation)
X_train, X_val, y_train, y_val = train_test_split(features, target, test_size=0.2, random_state=42)

# Normalize the features
scaler = StandardScaler()
X_train = torch.tensor(scaler.fit_transform(X_train), dtype=torch.float32)
X_val = torch.tensor(scaler.transform(X_val), dtype=torch.float32)

# Normalize the target variable
y_train_mean = y_train.mean()
y_train_std = y_train.std()
y_train = (y_train - y_train_mean) / y_train_std
y_val = (y_val - y_train_mean) / y_train_std

# Linear model
def l_model(X, params):
    return X @ params[:-1] + params[-1]

# Loss function (mean squared error)
def loss_fn(t_p, t_c):
    return ((t_p - t_c) ** 2).mean()

# Training loop
def training_loop(n_epochs, learning_rate, params, X_train, y_train, X_val, y_val):
    loss_track = np.zeros((n_epochs,1))

    for epoch in range(1, n_epochs + 1):
        # Forward pass: Compute predicted y
        t_p = l_model(X_train, params)

        # Compute loss
        loss = loss_fn(t_p, y_train)

        # Zero gradients, perform a backward pass, and update the weights
        loss.backward()

        with torch.no_grad():
            params -= learning_rate * params.grad
            params.grad.zero_()

        # Validation loss
        if epoch % 500 == 0 or epoch == 1:
            with torch.no_grad():
                val_loss = loss_fn(l_model(X_val, params), y_val).item()
                print(f"Epoch {epoch}, Training loss {loss.item():.4f}, Validation loss {val_loss:.4f}")

        loss_track[epoch-1] = loss.item()

    return loss_track

"""## **Problem II. B**
### Use 5000 epochs for your training. Explore different learning rates from 0.1 to 0.0001 (you need four separate trainings). Report your loss and validation accuracy for every 500 epochs per training. Pick the best linear model.
"""

learning_rate = [0.004,0.02,0.08,0.099]
n_epochs = 5000

loss_tr = np.zeros((n_epochs,len(learning_rate)+2))

w=torch.ones(())
b=torch.zeros(())


for i in range(n_epochs):
    loss_tr[i,0]=i+1

i=1
for lr in learning_rate:
      print()
      print (f'Trainings with Learning Rate = {lr}')
      print()
      params = torch.randn((6, 1), requires_grad=True)
      loss_tr[:,i]= training_loop(
              n_epochs=5000,
              learning_rate=lr,
              params=params,
              X_train=X_train,
              y_train=y_train,
              X_val=X_val,
              y_val=y_val).squeeze()
      i+=1

plt.plot(loss_tr[:500,0], loss_tr[:500,1],label=f'Learning Rate {learning_rate[0]}')
plt.plot(loss_tr[:500,0], loss_tr[:500,2],label=f'Learning Rate {learning_rate[1]}')
plt.plot(loss_tr[:500,0], loss_tr[:500,3],label=f'Learning Rate {learning_rate[2]}')
plt.plot(loss_tr[:500,0], loss_tr[:500,4],label=f'Learning Rate {learning_rate[3]}')

plt.rcParams["figure.figsize"] = (10,6)
plt.grid(1)
plt.xlabel('Number of iterations')
plt.ylabel('Cost (J)')
plt.title(f'Loss convergence')
plt.legend()

"""## **Problem II. C**
### Repeat all sections of problem 2, this time use all the input features from the housing price dataset
"""

file_path = '/content/drive/My Drive/Courses/Intro to ML/Lab2/Housing.csv'
df_house = pd.read_csv(file_path)

df_house_1 = (df_house.iloc[:,[4,5,6,7,8,10]] == 'yes').replace(True,1).replace(False,0)
df_house = pd.concat([df_house.iloc[:,[0,1,2,3,4,10,12]], df_house_1], axis = 1)
df_house_2 = pd.DataFrame((df_house.iloc[:,6] == 'furnished').replace(True,1).replace(False,0)).rename(columns={'furnishingstatus':'furnished'})
df_house = pd.concat([df_house, df_house_2], axis = 1)
df_house_3 = pd.DataFrame((df_house.iloc[:,6] == 'unfurnished').replace(True,1).replace(False,0)).rename(columns={'furnishingstatus':'unfurnished'})
df_house = pd.concat([df_house, df_house_3], axis = 1)
df_house_4 = pd.DataFrame((df_house.iloc[:,6] == 'semi-furnished').replace(True,1).replace(False,0)).rename(columns={'furnishingstatus':'semi-furnished'})
df_house = pd.concat([df_house, df_house_4], axis = 1)
df_house = df_house.drop(['furnishingstatus'],axis=1)

df_house

features = df_house.iloc[:,1:]
target = df_house['price']

# Convert to torch tensors
features = torch.tensor(features.values, dtype=torch.float32)
target = torch.tensor(target.values, dtype=torch.float32).view(-1, 1)

# Split into training and validation sets (80% training, 20% validation)
X_train, X_val, y_train, y_val = train_test_split(features, target, test_size=0.2, random_state=42)

# Normalize the features
scaler = StandardScaler()
X_train = torch.tensor(scaler.fit_transform(X_train), dtype=torch.float32)
X_val = torch.tensor(scaler.transform(X_val), dtype=torch.float32)

# Normalize the target variable
y_train_mean = y_train.mean()
y_train_std = y_train.std()
y_train = (y_train - y_train_mean) / y_train_std
y_val = (y_val - y_train_mean) / y_train_std

def l_model(X, params):
    return X @ params[:-1] + params[-1]

def loss_fn(t_p, t_c):
    return ((t_p - t_c) ** 2).mean()

# Training loop
def training_loop(n_epochs, learning_rate, params, X_train, y_train, X_val, y_val):
    loss_track = np.zeros((n_epochs,1))

    for epoch in range(1, n_epochs + 1):
        # Forward pass: Compute predicted y
        t_p = l_model(X_train, params)

        # Compute loss
        loss = loss_fn(t_p, y_train)

        # Zero gradients, perform a backward pass, and update the weights
        loss.backward()

        with torch.no_grad():
            params -= learning_rate * params.grad
            params.grad.zero_()

        # Validation loss
        if epoch % 500 == 0 or epoch == 1:
            with torch.no_grad():
                val_loss = loss_fn(l_model(X_val, params), y_val).item()
                print(f"Epoch {epoch}, Training loss {loss.item():.4f}, Validation loss {val_loss:.4f}")

        loss_track[epoch-1] = loss.item()

    return loss_track

learning_rate = [0.004,0.02,0.08,0.099]
n_epochs = 5000

loss_tr = np.zeros((n_epochs,len(learning_rate)+2))


for i in range(n_epochs):
    loss_tr[i,0]=i+1

i=1
for lr in learning_rate:
      print()
      print (f'Trainings with Learning Rate = {lr}')
      print()
      params = torch.randn((15, 1), requires_grad=True)
      loss_tr[:,i]= training_loop(
              n_epochs=5000,
              learning_rate=lr,
              params=params,
              X_train=X_train,
              y_train=y_train,
              X_val=X_val,
              y_val=y_val).squeeze()
      i+=1

plt.plot(loss_tr[:500,0], loss_tr[:500,1],label=f'Learning Rate {learning_rate[0]}')
plt.plot(loss_tr[:500,0], loss_tr[:500,2],label=f'Learning Rate {learning_rate[1]}')
plt.plot(loss_tr[:500,0], loss_tr[:500,3],label=f'Learning Rate {learning_rate[2]}')
plt.plot(loss_tr[:500,0], loss_tr[:500,4],label=f'Learning Rate {learning_rate[3]}')

plt.rcParams["figure.figsize"] = (10,6)
plt.grid(1)
plt.xlabel('Number of iterations')
plt.ylabel('Cost (J)')
plt.title(f'Loss convergence')
plt.legend()