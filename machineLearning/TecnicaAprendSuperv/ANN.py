#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 09:51:50 2019

@author: leidyaldana

Referencia: https://stackabuse.com/introduction-to-neural-networks-with-scikit-learn/
"""
import pandas as pd

# Location of dataset
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

# Assign colum names to the dataset
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'Class']

# Read dataset to pandas dataframe
irisdata = pd.read_csv(url, names=names)  
print(irisdata)
irisdata.head()  
# Assign data from first four columns to X variable
X = irisdata.iloc[:, 0:4]
# Assign data from first fifth columns to y variable
y = irisdata.select_dtypes(include=[object])  
print(y.head()  )
print(y.Class.unique() )
from sklearn import preprocessing  
le = preprocessing.LabelEncoder()

y = y.apply(le.fit_transform)  
print(type(y))
from sklearn.model_selection import train_test_split  
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20)  
from sklearn.preprocessing import StandardScaler  
scaler = StandardScaler()  
print(scaler.fit(X_train))

X_train = scaler.transform(X_train)  
X_test = scaler.transform(X_test)  

from sklearn.neural_network import MLPClassifier  
mlp = MLPClassifier(hidden_layer_sizes=(10, 10, 10), max_iter=1000)  
print(mlp.fit(X_train, y_train.values.ravel())  )

predictions = mlp.predict(X_test)  

from sklearn.metrics import classification_report, confusion_matrix  
# Compute confusion matrix to evaluate the accuracy of a classification
print(confusion_matrix(y_test,predictions))  
#Build a text report showing the main classification metrics
print(classification_report(y_test,predictions))  
