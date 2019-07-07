#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 2019

@author: leidyaldana
"""

#import matplotlib.pyplot as plt
#from sklearn.datasets import load_digits
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

digits = load_iris()

x_train, x_test, y_train, y_test = train_test_split(digits.data, digits.target)

"""
SVM: Clasificación y regresión mediante hiperplanos que separan datos de entrada
"""

clf = SVC(gamma=0.001, C=100)

print(clf.fit(x_train, y_train))

print(clf.score(x_test, y_test))

print(clf.predict(digits.data[-1:]))

#plt.figure(1, figsize=(3, 3))
#plt.imshow(digits.images[-1], cmap=plt.cm.gray_r, interpolation='nearest')
#plt.show()

print(clf.predict([[-0.8, -1, 1, 2]]))

print("Metricas")
predictions = clf.predict(x_test[:38])

from sklearn.metrics import classification_report, confusion_matrix  
# Compute confusion matrix to evaluate the accuracy of a classification
print(confusion_matrix(y_test,predictions))  
#Build a text report showing the main classification metrics
print(classification_report(y_test,predictions))  
