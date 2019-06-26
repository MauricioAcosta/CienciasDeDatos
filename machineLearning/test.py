# -*- coding: utf-8 -*-
"""
Created on Wed May 16 11:14:39 2018

@author: Nelson
"""
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

digits = load_digits()

x_train, x_test, y_train, y_test = train_test_split(digits.data, digits.target)

clf = SVC(gamma=0.001, C=100)

clf.fit(x_train, y_train)

clf.score(x_test, y_test)

clf.predict(digits.data[-1:])

plt.figure(1, figsize=(3, 3))
plt.imshow(digits.images[-1], cmap=plt.cm.gray_r, interpolation='nearest')
plt.show()