#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 09:51:50 2019

@author: leidyaldana
"""

from sklearn.datasets import load_iris
from sklearn.neural_network import MLPClassifier
import numpy as np

iris = load_iris()

X = iris.data
y = iris.target
clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(15,), random_state=1)
clf.fit(X,y)   
clf.predict([[2., 2.], [-1., -2.]])
[coef.shape for coef in clf.coefs_]
clf.predict_proba([[2., 2.], [1., 2.]])  
clf.predict([[1., 2.]])
np.ndim([[1., 2., 1., 2.],[1., 2., 1., 2.], [1., 2., 1., 2.],[1., 2., 1., 2.]])