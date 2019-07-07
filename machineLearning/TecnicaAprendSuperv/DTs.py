#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7  2019

@author: leidyaldana
"""

from sklearn.model_selection import train_test_split

from sklearn.datasets import load_iris
from sklearn import tree
iris = load_iris()

"""
Árboles de decisión:
Clasificación y regresión a partir de un modelo que predice el valor
de una variable objetivo mediante el aprendizaje de reglas simples
inferidas de las características de los datos
"""
x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target)

clf = tree.DecisionTreeClassifier()
#print(clf)
 # samples, features
clf = clf.fit(iris.data, iris.target)
print(clf)

import graphviz 
dot_data = tree.export_graphviz(clf, out_file=None) 
print(dot_data)
graph = graphviz.Source(dot_data) 
print(graph)
graph.render("iris")


dot_data = tree.export_graphviz(clf, out_file=None, 
                         feature_names=iris.feature_names,  
                         class_names=iris.target_names,  
                         filled=True, rounded=True,  
                         special_characters=True)  
print(dot_data)
graph = graphviz.Source(dot_data)  
print(graph)


print("Metricas")
predictions = clf.predict(x_test[:38])

from sklearn.metrics import classification_report, confusion_matrix  
# Compute confusion matrix to evaluate the accuracy of a classification
print(confusion_matrix(y_test,predictions))  
#Build a text report showing the main classification metrics
print(classification_report(y_test,predictions))  
