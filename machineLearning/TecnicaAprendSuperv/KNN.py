#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 2019

@author: leidyaldana
"""

from sklearn import datasets

iris = datasets.load_iris()
type(iris)
dir(iris)
iris.DESCR

iris.feature_names
iris.target_names

iris.data
iris.target


from sklearn.model_selection import train_test_split 

x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target)
x_train
y_train
x_test
y_test

from sklearn.neighbors import KNeighborsClassifier

"""
KNN: Estima la probabilidad a posteriori de que un elemento pertenzca a una clase, a partir de la información proporcionada en un dataset
"""

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(x_train, y_train) 
knn.score(x_test, y_test) 

knn.predict(x_test)
y_test

knn.predict(x_test[2:3][:4])
y_test[2:3][:4]


from sklearn.neighbors import RadiusNeighborsClassifier

knn_r = RadiusNeighborsClassifier(radius=5)

knn_r.fit(x_train, y_train) 
knn_r.score(x_test, y_test) 

knn_r.predict(x_test)
y_test

knn_r.predict(x_test[2:3][:4])
y_test[2:3][:4]


