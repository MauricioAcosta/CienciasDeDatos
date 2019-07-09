from sklearn import datasets
import numpy as np
iris = datasets.load_iris()
import matplotlib.pyplot as plt
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
ultimKnn = mKnn[34:]
print("\n")
matrizKnn=[mKnn[i:i+5] for i in range(0, int(len(mKnn)/2), 5)]
matrizKnn
print(np.shape(matrizKnn)) 
type(matrizKnn)
 
# Create the pandas DataFrame 
dfKnn = pd.DataFrame(matrizKnn) 
# print dataframe. 
dfKnn
ultimKnn=mKnn[34:]
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

#matrizSvm=[mSvm[i:i+5] for i in range(0, int(len(mSvm)), 5) ]
#matrizSvm = np.array(matrizSvm)
#matrizSvm
#print(np.shape(matrizSvm)) 
ultimSvm=mSvm[34:]
ultimSvm
# Create the pandas DataFrame 
#dfSvm = pd.DataFrame(data=matrizSvm) 
# print dataframe. 
#dfSvm

#dfSvm = pd.DataFrame(np.array(matrizSvm),
 #             columns=[' ', 'precision', 'recall', 'f1-score', 'support'])
#dfSvm.reset_index(drop=True, inplace=True)
#type(dfSvm)
#dfSvm.columns
# ================================================================================== DTS
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
mDTs=classification_report(y_test,predictions, target_names=iris.target_names)
type(mDTs)

mDTs= mDTs.split()
mDTs.insert(0, " ") 
print(type(mDTs) )
print("\n")
mDTs

ultimDTs = mDTs[34:]
ultimDTs

# ================================================================================== ANN


# ANN
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
dataANN = classification_report(y_test,predictions)
ultiANN = dataANN[345:-1]

ultiANN=ultiANN.split()
ultiANN

ultimKnn.insert(0,'KNN')
ultimSvm.insert(0,'SVM')
ultimDTs.insert(0,'DTS')
ultiANN.insert(0,'ANN')
datosFinales = np.array([['','Precision','Recall','f1Score','support'], ultimKnn, ultimSvm, ultimDTs, ultiANN ])
dataframeFinal=pd.DataFrame(data=datosFinales[1:,1:], index=datosFinales[1:,0], columns=datosFinales[0,1:])


dataframeFinal=dataframeFinal.astype(float)
dataframeFinal




#tabla de comparaci[on de resultados]
data = datosFinales[1:,1:].astype(float)
data=data[:,:-1]
columns = ('Precision','Recall','f1-score')
listarow=[]
for i in reversed(datosFinales[1:,0]):
    listarow.append(i)

rows = listarow
# Get some pastel shades for the colors
colors = plt.cm.BuPu(np.linspace(0.1, 0.7, len(rows)))
n_rows = len(data)

index = np.arange(len(columns)) + 0.3
bar_width = 0.4
index
# Initialize the vertical-offset for the stacked bar chart.
y_offset = np.zeros(len(columns))

# Plot bars and create text labels for the table
cell_text = []
for row in range(n_rows):
    print('row: ',row)
    plt.bar(index, data[row], bar_width, bottom=y_offset, color=colors[row])
    y_offset =y_offset + data[row]
    cell_text.append(['%1.2f' % (x) for x in y_offset])
# Reverse colors and text labels to display the last value at the top.
    
colors = colors[::-1]
cell_text.reverse()
print(cell_text)
# Add a table at the bottom of the axes
the_table = plt.table(cellText=cell_text,
                      rowLabels=rows,
                      rowColours=colors,
                      colLabels=columns,
                      loc='bottom')

# Adjust layout to make room for the table:
#plt.subplots_adjust(left=0.2, bottom=0.2)

#plt.yticks(values * value_increment, ['%d' % val for val in values])
plt.xticks([])
plt.ylabel("Tecnicas empleadas")
plt.title('Reporte de clasificación')
plt.show()
dataframeFinal