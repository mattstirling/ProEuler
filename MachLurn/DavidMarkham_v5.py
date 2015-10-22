'''
Created on Oct 15, 2015

@author: Trader
'''
from sklearn.datasets import load_iris
iris = load_iris()

#create X (features) and y (response)
X = iris.data
y = iris.target

#check shape
print X.shape
print y.shape

# First try with a Logistic Regression model
# import the class
from sklearn.linear_model import LogisticRegression

#instantiate the model using default parameters
logreg = LogisticRegression()

#Fit the model
logreg.fit(X, y)

#Predict the response for a new observation
y_pred_A = logreg.predict(X)
print len(y_pred_A)

#NEW - determine classification accuracy
from sklearn import metrics
print metrics.accuracy_score(y,y_pred_A)

#Now try with KNN, K=5
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X, y)
y_pred_B = knn.predict(X)
print metrics.accuracy_score(y,y_pred_B)

#Now try with KNN, K=1
knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X, y)
y_pred_C = knn.predict(X)
print metrics.accuracy_score(y,y_pred_C)

#now try train/test split evaluation
#1. Split the data
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.4,random_state=4)
#random_state allows us to set the seed for the random split of the data

print X_train.shape
print X_test.shape

print y_train.shape
print y_test.shape

#2 fit & test our models
logreg.fit(X_train, y_train)
y_pred_A = logreg.predict(X_test)
print metrics.accuracy_score(y_test,y_pred_A)

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)
y_pred_B = knn.predict(X_test)
print metrics.accuracy_score(y_test,y_pred_B)

knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train, y_train)
y_pred_C = knn.predict(X_test)
print metrics.accuracy_score(y_test,y_pred_C)

#now look for an optimal value k
k_range = range(1,26)
scores = []
for k in k_range:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    scores.append(metrics.accuracy_score(y_test,y_pred))

import matplotlib.pyplot as plt
plt.plot(k_range, scores)
plt.xlabel('Value of K for KNN')
plt.ylabel('Testing Accuracy')
plt.show()

#now make a prediction using k=11
knn = KNeighborsClassifier(n_neighbors=11)
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)
print knn.predict([3,5,4,2])
 

