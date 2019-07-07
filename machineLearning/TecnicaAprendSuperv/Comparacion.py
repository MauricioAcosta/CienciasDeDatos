from sklearn import datasets

iris = datasets.load_iris()

from sklearn.model_selection import train_test_split 

x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target)

# KNN
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(x_train, y_train)
predictions = knn.predict(x_test[:38])

print("Metricas KNN")

from sklearn.metrics import classification_report, confusion_matrix  
# Compute confusion matrix to evaluate the accuracy of a classification
print(confusion_matrix(y_test,predictions))  
#Build a text report showing the main classification metrics
mKnn=classification_report(y_test,predictions)
print(mKnn)

# SVM
from sklearn.svm import SVC
print("Metricas SVM")
clf = SVC(gamma=0.001, C=100)
clf.fit(x_train, y_train)
predictions = clf.predict(x_test[:38])
# Compute confusion matrix to evaluate the accuracy of a classification
print(confusion_matrix(y_test,predictions))  
#Build a text report showing the main classification metrics
print(classification_report(y_test,predictions))  

# DTs
from sklearn import tree
print("Metricas DTS")
clf = tree.DecisionTreeClassifier()
clf = clf.fit(iris.data, iris.target)
predictions = clf.predict(x_test[:38])
# Compute confusion matrix to evaluate the accuracy of a classification
print(confusion_matrix(y_test,predictions))  
#Build a text report showing the main classification metrics
print(classification_report(y_test,predictions))  


# ANN
from sklearn.neural_network import MLPClassifier  
mlp = MLPClassifier(hidden_layer_sizes=(10, 10, 10), max_iter=1000)  
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size = 0.20)  
mlp.fit(x_train, y_train.values.ravel()) 
predictions = mlp.predict(x_test)  
print("Metricas ANN")
from sklearn.metrics import classification_report, confusion_matrix  
# Compute confusion matrix to evaluate the accuracy of a classification
print(confusion_matrix(y_test,predictions))  
#Build a text report showing the main classification metrics
print(classification_report(y_test,predictions))  
