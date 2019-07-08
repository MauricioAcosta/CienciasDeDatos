from sklearn import datasets
import numpy as np
iris = datasets.load_iris()

# Import pandas library 
import pandas as pd 
from sklearn.model_selection import train_test_split 

x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target)

# ================================================================================== KNN
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(x_train, y_train)
predictions = knn.predict(x_test[:38])

print("Metricas KNN")

from sklearn.metrics import classification_report, confusion_matrix  
#Build a text report showing the main classification metrics
mKnn=classification_report(y_test,predictions, target_names=iris.target_names)

print(mKnn)

mKnn= mKnn.split()
mKnn.insert(0, " ") 
print(type(mKnn) )
print("\n")
mKnn
print("\n")
matrizKnn=[mKnn[i:i+5] for i in range(0, int(len(mKnn)/2), 5)]
matrizKnn
print(np.shape(matrizKnn)) 
type(matrizKnn)
 
# Create the pandas DataFrame 
dfKnn = pd.DataFrame(matrizKnn) 
# print dataframe. 
dfKnn
# ================================================================================== SVM

from sklearn.svm import SVC
print("Metricas SVM")
clf = SVC(gamma=0.001, C=100)
clf.fit(x_train, y_train)
predictions = clf.predict(x_test[:38])
#Build a text report showing the main classification metrics
mSvm=classification_report(y_test,predictions, target_names=iris.target_names)

print(mSvm)

mSvm= mSvm.split()
mSvm.insert(0, " ") 
print(type(mSvm) )
print("\n")
mSvm
print("\n")
matrizSvm=[mSvm[i:i+5] for i in range(0, int(len(mSvm)/2), 5) ]
matrizSvm

#print(np.shape(matrizSvm)) 

# Create the pandas DataFrame 
dfSvm = pd.DataFrame(data=matrizSvm) 
# print dataframe. 
type(dfSvm)

dfSvm = pd.DataFrame(np.array(matrizSvm),
              columns=[' ', 'precision', 'recall', 'f1-score', 'support'])
dfSvm.reset_index(drop=True, inplace=True)
type(dfSvm)
dfSvm.columns
"""
import matplotlib.pyplot as plt
import pandas as pd
dfSvm.plot(kind='bar',x='precision',y='recall')
plt.show()
"""