#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 2019

@author: leidyaldana
"""

from sklearn import datasets

iris = datasets.load_iris()
print(type(iris))
print(dir(iris))
print(iris.DESCR)

print(iris.feature_names)
print(iris.target_names)

print(iris.data)
print(iris.target)


from sklearn.model_selection import train_test_split 

x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target)
print(x_train)
print(y_train)
print(x_test)
print(y_test)

from sklearn.neighbors import KNeighborsClassifier

"""
KNN: Estima la probabilidad a posteriori de que un elemento pertenzca a una clase, a partir de la información proporcionada en un dataset
"""

knn = KNeighborsClassifier(n_neighbors=5)
print(knn.fit(x_train, y_train) )
print(knn.score(x_test, y_test) )

print(knn.predict(x_test))
print(y_test)

print(knn.predict(x_test[2:3][:4]))
print(y_test[2:3][:4])


from sklearn.neighbors import RadiusNeighborsClassifier

knn_r = RadiusNeighborsClassifier(radius=5)

print(knn_r.fit(x_train, y_train) )
print(knn_r.score(x_test, y_test) )

print(knn_r.predict(x_test))
print(y_test)

print(knn_r.predict(x_test[2:3][:4]))
print(y_test[2:3][:4])

predictions = knn.predict(x_test[:38])

print("Metricas")

from sklearn.metrics import classification_report, confusion_matrix  
# Compute confusion matrix to evaluate the accuracy of a classification
print(confusion_matrix(y_test,predictions))  
#Build a text report showing the main classification metrics
print(classification_report(y_test,predictions))  
