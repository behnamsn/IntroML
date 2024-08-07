# -*- coding: utf-8 -*-
"""Lab4.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1YcZockSOdQoQLX5KH7rEqxp0529j2xH0

## Lab 4
### Name: Behnam Sobhani Nadri
### Student ID: 801368949

## All libraries that we use in the lab is defined here
"""

import warnings
import pandas as pd
import numpy as np
import seaborn as sb
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
###Use the cancer dataset to build an SVM classifier to classify the type of cancer (Malignant vs. Benign). Use the PCA feature extraction for your training. Perform N number of independent training (N=1, …, K)
"""

file_path='/content/drive/My Drive/Courses/Intro to ML/Lab3/cancer.csv'
df_cancer = pd.read_csv(file_path)

df_cancer1 = (df_cancer.iloc[:,1] == "M").replace(True,1).replace(False,0)
df_cancer = pd.concat([df_cancer.drop(["diagnosis", "Unnamed: 32"],axis=1), df_cancer1], axis = 1)
df_cancer

X = df_cancer.iloc[:,1:31].values
Y = df_cancer.iloc[:,31].values

"""## **1**
### Identify the optimum number of K, principal components that achieve the highest classification accuracy

### Support Vector Machine (SVM) Classifier
"""

K=29
accur = np.zeros((K,2))
prec = np.zeros((K,2))
rec = np.zeros((K,2))
f1 = np.zeros((K,2))

for i in range(K):
    # X = df_cancer.iloc[:,1:31].values
    # Y = df_cancer.iloc[:,31].values
    # print(i)
    decomposer = PCA(n_components=i+1)
    X_r = decomposer.fit(X).transform(X)
    X_train_r, X_test_r, Y_train, Y_test = train_test_split(X_r,Y, test_size=0.25, random_state = 0)
    sc_X = StandardScaler()
    X_train_r = sc_X.fit_transform(X_train_r)
    X_test_r = sc_X.transform(X_test_r)
    classifier = svm.SVC()
    # classifier = LogisticRegression(random_state=0, solver='lbfgs', max_iter=1000)
    classifier.fit(X_train_r, Y_train)
    Y_pred = classifier.predict(X_test_r)
    accur [ i, 0]=i+1
    accur [i,1] = metrics.accuracy_score(Y_test, Y_pred)
    prec [ i, 0]=i+1
    prec [i,1] = metrics.precision_score(Y_test, Y_pred)
    rec [ i, 0]=i+1
    rec [i,1] = metrics.recall_score(Y_test, Y_pred)
    f1 [ i, 0]=i+1
    f1 [i,1] = metrics.f1_score(Y_test, Y_pred)

maximum_accur = max(accur[:,1])
print("Maximum Accuracy is:", maximum_accur)
print("Maximum Accuracy is at K:", accur[accur[:,1] == maximum_accur][0,0])

"""## **2**
### Plot your classification accuracy, precision, and recall over a different number of Ks
"""

plt.plot(accur[:,0],accur[:,1])
plt.rcParams["figure.figsize"] = (10,6)
plt.grid(1)
plt.xlabel('Number of Components (K)')
plt.ylabel('Accuracy')
plt.title('Accuracy vs Number of Components (K) for PCA using SVM')
plt.legend()

plt.plot(prec[:,0],prec[:,1])
plt.rcParams["figure.figsize"] = (10,6)
plt.grid(1)
plt.xlabel('Number of Components (K)')
plt.ylabel('Precision')
plt.title('Precision vs Number of Components (K) for PCA using SVM')
plt.legend()

plt.plot(rec[:,0],rec[:,1])
plt.rcParams["figure.figsize"] = (10,6)
plt.grid(1)
plt.xlabel('Number of Number of Components (K)')
plt.ylabel('Recall')
plt.title('Recall vs Number of Components (K) for PCA using SVM')
plt.legend()

plt.plot(f1[:,0],f1[:,1])
plt.rcParams["figure.figsize"] = (10,6)
plt.grid(1)
plt.xlabel('Number of Number of Components (K)')
plt.ylabel('F1-score')
plt.title('F1-score vs Number of Number of Components (K) for PCA using SVM')
plt.legend()

"""## **3**
### Explore different kernel tricks to capture non-linearities within your data. Plot the results and compare the accuracies for different kernels

"""

K=29
kern='sigmoid'
# kern='poly'
# kern='linear'
# kern='precomputed'
accur = np.zeros((K,2))
prec = np.zeros((K,2))
rec = np.zeros((K,2))
f1 = np.zeros((K,2))

for i in range(K):
    # X = df_cancer.iloc[:,1:31].values
    # Y = df_cancer.iloc[:,31].values
    # print(i)
    decomposer = PCA(n_components=i+1)
    X_r = decomposer.fit(X).transform(X)
    X_train_r, X_test_r, Y_train, Y_test = train_test_split(X_r,Y, test_size=0.25, random_state = 0)
    sc_X = StandardScaler()
    X_train_r = sc_X.fit_transform(X_train_r)
    X_test_r = sc_X.transform(X_test_r)
    classifier = svm.SVC(kernel=kern)
    # classifier = svm.SVC(kernel='linear')
    # classifier = LogisticRegression(random_state=0, solver='lbfgs', max_iter=1000)
    classifier.fit(X_train_r, Y_train)
    Y_pred = classifier.predict(X_test_r)
    accur [ i, 0]=i+1
    accur [i,1] = metrics.accuracy_score(Y_test, Y_pred)
    prec [ i, 0]=i+1
    prec [i,1] = metrics.precision_score(Y_test, Y_pred)
    rec [ i, 0]=i+1
    rec [i,1] = metrics.recall_score(Y_test, Y_pred)
    f1 [ i, 0]=i+1
    f1 [i,1] = metrics.f1_score(Y_test, Y_pred)

maximum_accur = max(accur[:,1])
print("Maximum Accuracy is:", maximum_accur)
print("Maximum Accuracy is at K:", accur[accur[:,1] == maximum_accur][0,0])

plt.plot(accur[:,0],accur[:,1])
plt.rcParams["figure.figsize"] = (10,6)
plt.grid(1)
plt.xlabel('Number of Components (K)')
plt.ylabel('Accuracy')
plt.title(f'Accuracy vs Number of Components (K) for SVC with {kern} kernel')
plt.legend()

plt.plot(prec[:,0],prec[:,1])
plt.rcParams["figure.figsize"] = (10,6)
plt.grid(1)
plt.xlabel('Number of Components (K)')
plt.ylabel('Precision')
plt.title(f'Precision vs Number of Components (K) for SVC with {kern} kernel')
plt.legend()

plt.plot(rec[:,0],rec[:,1])
plt.rcParams["figure.figsize"] = (10,6)
plt.grid(1)
plt.xlabel('Number of Number of Components (K)')
plt.ylabel('Recall')
plt.title('Recall vs Number of Components (K)')
plt.legend()

plt.plot(f1[:,0],f1[:,1])
plt.rcParams["figure.figsize"] = (10,6)
plt.grid(1)
plt.xlabel('Number of Number of Components (K)')
plt.ylabel('F1-score')
plt.title('F1-score vs Number of Number of Components (K)')
plt.legend()

"""## **Problem II**

## Develop an SVR regression model that predicts housing price based on the following input variables:

## Area, bedrooms, bathrooms, stories, mainroad, guestroom, basement, hotwaterheating, airconditioning, parking, prefarea
"""

file_path = '/content/drive/My Drive/Courses/Intro to ML/Lab2/Housing.csv'
df = pd.read_csv(file_path)

scaler = 'normalize'
# scaler = 'standard'
split = 0.20 # Split ratio
a = int(df.shape[0]*(1-split))

df_train = df.iloc[0:a,:]
df_test = df.iloc[a:,:]
y_train = df_train.values[:, 0]
y_test = df_test.values[:, 0]

df_train1 = (df_train.iloc[:,[5,6,7,8,9,11]] == "yes").replace(True,1).replace(False,0)
df_train = pd.concat([df_train.iloc[:,[0,1,2,3,4,10,12]], df_train1], axis = 1)

df_test1 = (df_test.iloc[:,[5,6,7,8,9,11]] == "yes").replace(True,1).replace(False,0)
df_test = pd.concat([df_test.iloc[:,[0,1,2,3,4,10,12]], df_test1], axis = 1)

df_train = df_train.drop(['furnishingstatus'], axis='columns')
df_test = df_test.drop(['furnishingstatus'], axis='columns')

if scaler == 'normalize':
    min_max_scaled= preprocessing.MinMaxScaler()
else:
    min_max_scaled= preprocessing.StandardScaler()

df_train_scaled = min_max_scaled.fit_transform(df_train)
df_test_scaled = min_max_scaled.fit_transform(df_test)
df_train_scaled = pd.DataFrame(df_train_scaled)
df_test_scaled = pd.DataFrame(df_test_scaled)

X_train = df_train.iloc[:,1:11].values
Y_train = df_train.iloc[:,0].values

X_test = df_test.iloc[:,1:11].values
Y_test = df_test.iloc[:,0].values

X_train_scaled = df_train_scaled.iloc[:,1:11].values
Y_train_scaled = df_train_scaled.iloc[:,0].values

X_test_scaled = df_test_scaled.iloc[:,1:11].values
Y_test_scaled = df_test_scaled.iloc[:,0].values

"""## **1 & 4**
## Plot your regression model for SVR similar to the sample code provided on Canvas

## Explore different kernel tricks to capture non-linearities within your data. Plot the results and compare the accuracies for different kernels
"""

rbf_classifier = SVR(kernel='rbf', C=1e3, gamma=0.1)
linear_classifier = SVR(kernel='linear', C=1e3)
poly_classifier = SVR(kernel='poly', C=1e3, degree=2)

Y_rbf_train = rbf_classifier.fit(X_train_scaled,Y_train_scaled).predict(X_train_scaled)
Y_linear_train = linear_classifier.fit(X_train_scaled,Y_train_scaled).predict(X_train_scaled)
Y_poly_train = poly_classifier.fit(X_train_scaled,Y_train_scaled).predict(X_train_scaled)

print("RBF Accuracy on train dataset:", metrics.mean_squared_error(Y_train_scaled, Y_rbf_train))
print("Linear Accuracy on train dataset:", metrics.mean_squared_error(Y_train_scaled, Y_linear_train))
print("Poly Accuracy on train dataset:", metrics.mean_squared_error(Y_train_scaled, Y_poly_train))

Y_rbf_test = rbf_classifier.fit(X_train_scaled,Y_train_scaled).predict(X_test_scaled)
Y_linear_test = linear_classifier.fit(X_train_scaled,Y_train_scaled).predict(X_test_scaled)
Y_poly_test = poly_classifier.fit(X_train_scaled,Y_train_scaled).predict(X_test_scaled)

print("RBF Accuracy on test dataset:", metrics.mean_squared_error(Y_test_scaled, Y_rbf_test))
print("Linear Accuracy on test dataset:", metrics.mean_squared_error(Y_test_scaled, Y_linear_test))
print("Poly Accuracy on test dataset:", metrics.mean_squared_error(Y_test_scaled, Y_poly_test))

plt.scatter(X_train_scaled[:,0], Y_train_scaled,color='k',marker= '.', label='Real Data')
plt.scatter(X_train_scaled[:,0], Y_linear_train,color='b',marker= '.', label='Linear SVR')
plt.scatter(X_train_scaled[:,0],Y_rbf_train, color='r', marker= '.', label='RBF SVR')
plt.scatter(X_train_scaled[:,0],Y_poly_train, color='g', marker= '.',label='Poly SVR')

plt.xlabel('Data')
plt.ylabel('Target')
plt.legend()
plt.grid()

plt.scatter(X_test_scaled[:,0], Y_test_scaled,color='k',marker= '.', label='Real Data')
plt.scatter(X_test_scaled[:,0], Y_linear_test,color='b',marker= '.', label='Linear SVR')
plt.scatter(X_test_scaled[:,0],Y_rbf_test, color='r', marker= '.', label='RBF SVR')
plt.scatter(X_test_scaled[:,0],Y_poly_test, color='g', marker= '.',label='Poly SVR')

plt.xlabel('Data')
plt.ylabel('Target')
plt.legend()
plt.grid()

"""## **2**
## Compare your results against linear regression with regularization loss that you already did in assignment 1

## **3**
## Use the PCA feature extraction for your training. Perform N number of independent training (N=1, …, K). Identify the optimum number of K, principal components that achieve the highest regression accuracy
"""

K=10
mse = np.zeros((K,2))

for i in range(K):
    decomposer = PCA(n_components=i+1)
    X_train_r = decomposer.fit(X_train_scaled).transform(X_train_scaled)
    rbf_classifier = SVR(kernel='rbf',C=1e3, gamma=0.1)
    Y_rbf = rbf_classifier.fit(X_train_r,Y_train_scaled).predict(X_train_r)
    mse [ i, 0]=i+1
    mse [i,1] = metrics.mean_squared_error(Y_train_scaled, Y_rbf)

minimum_mse = min(mse[:,1])
print("Minimum Squared Error (MSE) is:", minimum_mse)
print("Best MSE happens at K:", mse[mse[:,1] == minimum_mse][0,0])

plt.plot(mse[:,0],mse[:,1])
plt.rcParams["figure.figsize"] = (10,6)
plt.grid(1)
plt.xlabel('Number of Components (K)')
plt.ylabel('Minimum Squared Error (MSE)')
plt.title('MSE vs Number of Components (K)')
plt.legend()

i=10
decomposer = PCA(n_components=i)
X_train_r = decomposer.fit(X_train_scaled).transform(X_train_scaled)
sc_X = StandardScaler()
X_train_r = sc_X.fit_transform(X_train_r)
# X_test_r = sc_X.transform(X_test_r)
rbf_classifier = SVR(kernel='rbf',C=1e3, gamma=0.1)
Y_rbf = rbf_classifier.fit(X_train_r,Y_train_scaled).predict(X_train_r)

print("RBF Accuracy:", metrics.mean_squared_error(Y_train_scaled, Y_rbf))