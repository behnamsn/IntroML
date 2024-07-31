# -*- coding: utf-8 -*-
"""Lab3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1aAxQTVFaLe998yXuw1dqUyKZzd4oMzWk

## Lab 3
### Name: Behnam Sobhani Nadri
### Student ID: 801368949

## All libraries that we use in the lab is defined here
"""

import warnings
import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt
from google.colab import drive
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.decomposition import PCA
from sklearn.metrics import confusion_matrix
from sklearn import metrics
import seaborn as sns
from matplotlib.colors import ListedColormap
drive.mount('/content/drive')

"""## Problem I
###Using the diabetes dataset, build a logistic regression binary classifier for positive diabetes. Please use 80% and 20% split between training and evaluation (test). Make sure to perform proper scaling and standardization before your training. Draw your training results, including loss and classification accuracy over iterations. Also, report your results, including accuracy, precision, and recall, FI score. At the end, plot the confusion matrix representing your binary classifier.
"""

file_path='/content/drive/My Drive/Courses/Intro to ML/Lab3/diabetes.csv'
df_diabet = pd.read_csv(file_path)
df_diabet

# X = df_diabet.iloc[:,[1,2]].values
# X = df_diabet.iloc[:,[1,4]].values
X = df_diabet.iloc[:,[1,5]].values
# X = df_diabet.iloc[:,[1,6]].values
# X = df_diabet.iloc[:,[1,7]].values
# X = df_diabet.iloc[:,[5,6]].values
X = df_diabet.iloc[:,0:7].values
Y = df_diabet.iloc[:,8].values

"""### Scaling and Standarization"""

X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.25, random_state = 0)
# X_train.shape
# X_test.shape

sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
# X_train.shape
# X_test.shape

"""### Logitic Regression Classifier"""

# classifier = LogisticRegression(random_state=0, solver='liblinear')
classifier = LogisticRegression(random_state=0, solver='lbfgs', penalty=None, max_iter=500)
# classifier = LogisticRegression(random_state=0, solver='liblinear', max_iter=500)
classifier.fit(X_train, Y_train)
Y_pred = classifier.predict(X_test)
# Y_pred
# cnf_matrix = confusion_matrix (Y_test, Y_pred)
cnf_matrix = confusion_matrix (Y_test, Y_pred,normalize='true')
cnf_matrix

"""### Accuracy, Precision, Recall and F1-Score"""

print("Accuracy:", metrics.accuracy_score(Y_test, Y_pred))
print("Precision:", metrics.precision_score(Y_test,Y_pred))
print("Recall:", metrics.recall_score(Y_test,Y_pred))
print("F1-score:", metrics.f1_score(Y_test,Y_pred))

"""### Confusion Matrix"""

# class_names=[0,1]
# fig, x = plt.subplots()
# tick_marks=np.arange(len(class_names))
# plt.xticks(tick_marks,class_names)
# plt.yticks(tick_marks,class_names)
# sns.heatmap(pd.DataFrame(cnf_matrix), annot=True , cmap="tab10", fmt='g')
# plt.tight_layout()
# plt.title("Confusion Matrix", y=1.1)
# plt.xlabel("Predicted Label")
# plt.ylabel("Actual Label")

from sklearn.metrics import ConfusionMatrixDisplay
titles_options = [
        ("Confusion matrix, without normalization", None),
        ("Normalized confusion matrix", "true"),
    ]
for title, normalize in titles_options:
    disp = ConfusionMatrixDisplay.from_estimator(
    classifier,
    X_test,
    Y_test,
    display_labels=classifier.classes_,
    cmap=plt.cm.Blues,
    normalize=normalize
  )
    disp.ax_.set_title(title)
    print(title)
    print(disp.confusion_matrix)

    # plt.savefig(f'fig/conf_matrix_{classifier}')

# warnings.filterwarnings('ignore')
# X_set, Y_set = X_test, Y_test
# X1, X2  = np.meshgrid(np.arange(start = X_set[:, 0].min() - 1, stop = X_set[:, 0].max() + 1, step = 0.01),
#                      np.arange(start = X_set[:, 1].min() - 1, stop = X_set[:, 1].max() + 1, step = 0.01))
# plt.contourf(X1, X2, classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
#              alpha = 0.75, cmap = ListedColormap(('grey', 'white')))
# plt.xlim(X1.min(), X1.max())
# plt.ylim(X2.min(), X2.max())
# for i, j in enumerate(np.unique(Y_set)):
#     plt.scatter(X_set[Y_set == j, 0], X_set[Y_set == j, 1],
#                 c = ListedColormap(('blue', 'magenta'))(i), label = j)
# plt.title('Logistic Regression (Test set)')
# plt.xlabel('Age')
# plt.ylabel('Estimated Salary')
# plt.legend()
# plt.show()

"""## Problem II A
### Use the cancer dataset to build a logistic regression model to classify the type of cancer (Malignant vs. benign). First, create a logistic regression that takes all 30 input features for classification. Please use 80% and 20% split between training and evaluation (test). Make sure to perform proper scaling and standardization before your training. Draw your training results, including loss and classification accuracy over iterations. Also, report your results, including accuracy, precision, recall and F1 score. At the end, plot the confusion matrix representing your binary classifier.
"""

file_path='/content/drive/My Drive/Courses/Intro to ML/Lab3/cancer.csv'
df_cancer = pd.read_csv(file_path)

df_cancer1 = (df_cancer.iloc[:,1] == "M").replace(True,1).replace(False,0)
df_cancer = pd.concat([df_cancer.drop(["diagnosis", "Unnamed: 32"],axis=1), df_cancer1], axis = 1)
df_cancer

X = df_cancer.iloc[:,1:31].values
Y = df_cancer.iloc[:,31].values

"""### Scaling and Standarization"""

X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.25, random_state = 0)

sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)

"""### Logitic Regression Classifier"""

# classifier = LogisticRegression(random_state=0, solver='liblinear')
classifier = LogisticRegression(random_state=0, solver='lbfgs', penalty=None, max_iter=500)
# classifier = LogisticRegression(random_state=0, solver='liblinear', max_iter=500)
classifier.fit(X_train, Y_train)
Y_pred = classifier.predict(X_test)

cnf_matrix = confusion_matrix (Y_test, Y_pred,normalize='true')
cnf_matrix

"""### Accuracy, Precision, Recall and F1-Score"""

print("Accuracy:", metrics.accuracy_score(Y_test, Y_pred))
print("Precision:", metrics.precision_score(Y_test,Y_pred))
print("Recall:", metrics.recall_score(Y_test,Y_pred))
print("F1-score:", metrics.f1_score(Y_test,Y_pred))

"""### Confusion Matrix"""

from sklearn.metrics import ConfusionMatrixDisplay
titles_options = [
        ("Confusion matrix, without normalization", None),
        ("Normalized confusion matrix", "true"),
    ]
for title, normalize in titles_options:
    disp = ConfusionMatrixDisplay.from_estimator(
    classifier,
    X_test,
    Y_test,
    display_labels=classifier.classes_,
    cmap=plt.cm.Blues,
    normalize=normalize
  )
    disp.ax_.set_title(title)
    print(title)
    print(disp.confusion_matrix)

    # plt.savefig(f'fig/conf_matrix_{classifier}')

"""## Problem II B
### How about adding a weight penalty here, considering the number of parameters. Add the weight penalty and repeat the training and report the results.

### Logitic Regression Classifier
"""

classifier = LogisticRegression(random_state=0, solver='liblinear', penalty='l2', max_iter=500)
# classifier = LogisticRegression(random_state=0, solver='liblinear', max_iter=500)
# classifier = LogisticRegression(random_state=0, penalty='l2')
classifier.fit(X_train, Y_train)
Y_pred = classifier.predict(X_test)

cnf_matrix = confusion_matrix (Y_test, Y_pred,normalize='true')
cnf_matrix

"""### Accuracy, Precision, Recall and F1-Score"""

print("Accuracy:", metrics.accuracy_score(Y_test, Y_pred))
print("Precision:", metrics.precision_score(Y_test,Y_pred))
print("Recall:", metrics.recall_score(Y_test,Y_pred))
print("F1-score:", metrics.f1_score(Y_test,Y_pred))

"""### Confusion Matrix"""

from sklearn.metrics import ConfusionMatrixDisplay
titles_options = [
        ("Confusion matrix, without normalization", None),
        ("Normalized confusion matrix", "true"),
    ]
for title, normalize in titles_options:
    disp = ConfusionMatrixDisplay.from_estimator(
    classifier,
    X_test,
    Y_test,
    display_labels=classifier.classes_,
    cmap=plt.cm.Blues,
    normalize=normalize
  )
    disp.ax_.set_title(title)
    print(title)
    print(disp.confusion_matrix)

    # plt.savefig(f'fig/conf_matrix_{classifier}')

"""## Problem III
### Use the cancer dataset to build a naive Bayesian model to classify the type of cancer (Malignant vs. benign). Use 80% and 20% split between training and evaluation (test). Plot your classification accuracy, precision, recall, and F1 score. Explain and elaborate on your results. Can you compare your results against the logistic regression classifier you did in Problem 2.

### Naive Bayes Classifier
"""

classifier = GaussianNB()
classifier.fit(X_train, Y_train)
Y_pred = classifier.predict(X_test)

cnf_matrix = confusion_matrix (Y_test, Y_pred,normalize='true')
cnf_matrix

"""### Accuracy, Precision, Recall and F1-Score"""

print("Accuracy:", metrics.accuracy_score(Y_test, Y_pred))
print("Precision:", metrics.precision_score(Y_test,Y_pred))
print("Recall:", metrics.recall_score(Y_test,Y_pred))
print("F1-score:", metrics.f1_score(Y_test,Y_pred))

"""### Confusion Matrix"""

from sklearn.metrics import ConfusionMatrixDisplay
titles_options = [
        ("Confusion matrix, without normalization", None),
        ("Normalized confusion matrix", "true"),
    ]
for title, normalize in titles_options:
    disp = ConfusionMatrixDisplay.from_estimator(
    classifier,
    X_test,
    Y_test,
    display_labels=classifier.classes_,
    cmap=plt.cm.Blues,
    normalize=normalize
  )
    disp.ax_.set_title(title)
    print(title)
    print(disp.confusion_matrix)

    # plt.savefig(f'fig/conf_matrix_{classifier}')

"""## Problem IV
### Use the cancer dataset to build a logistic regression model to classify the type of cancer (Malignant vs. benign). Use the PCA feature extraction for your training. Perform N number of independent training (N=1, …, K). Identify the optimum number of K, principal components that achieve the highest classification accuracy. Plot your classification accuracy, precision, recall, and F1 score over a different number of Ks. Explain and elaborate on your results and compare it against problems 2 and 3.
"""

file_path='/content/drive/My Drive/Courses/Intro to ML/Lab3/cancer.csv'
df_cancer = pd.read_csv(file_path)

df_cancer1 = (df_cancer.iloc[:,1] == "M").replace(True,1).replace(False,0)
df_cancer = pd.concat([df_cancer.drop(["diagnosis", "Unnamed: 32"],axis=1), df_cancer1], axis = 1)
df_cancer

X = df_cancer.iloc[:,1:31].values
Y = df_cancer.iloc[:,31].values

"""### Logitic Regression Classifier"""

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
    classifier = LogisticRegression(random_state=0, solver='lbfgs', max_iter=1000)
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
plt.title('Accuracy vs Number of Components')
plt.legend()

plt.plot(prec[:,0],prec[:,1])
plt.rcParams["figure.figsize"] = (10,6)
plt.grid(1)
plt.xlabel('Number of Components (K)')
plt.ylabel('Precision')
plt.title('Precision vs Number of Components (K)')
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

"""## Problem V
### Can you repeat problem 4? This time, replace the Bayes classifier with logistic regression. Report your results (classification accuracy, precision, recall and F1 score). Compare your results against problems 2, 3 and 4.

### Logitic Regression Classifier
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
    classifier = GaussianNB()
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
plt.title('Accuracy vs Number of Components')
plt.legend()

plt.plot(prec[:,0],prec[:,1])
plt.rcParams["figure.figsize"] = (10,6)
plt.grid(1)
plt.xlabel('Number of Components (K)')
plt.ylabel('Precision')
plt.title('Precision vs Number of Components (K)')
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