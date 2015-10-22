'''
Created on Oct 17, 2015

@author: Trader
'''
from sklearn.datasets import load_iris
from sklearn.cross_validation import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics

#read in iris data, set to X, y
iris = load_iris()
X = iris.data
y = iris.target

#use train test split
X_train, X_test, y_train, y_test = train_test_split(X,y,random_state = 4)

#check classification accuracy of KNN, with K=5
KNN = KNeighborsClassifier(n_neighbors=5)
KNN.fit(X_train,y_train)
y_pred = KNN.predict(X_test)
print metrics.accuracy_score(y_test,y_pred)

#simulate splitting a dataset of 25 observations into 5 folds
from sklearn.cross_validation import KFold
kf = KFold(25,n_folds=5,shuffle=False)

#print the contents of each training and testing set
print '{} {:^61} {}'.format('Iteration','Training Set Observations','Testing Set Observations')
for iteration, data in enumerate(kf,start=1):
    print '{:^9} {} {:^25}'.format(iteration,data[0],data[1])


#APPLY CROSS VALIDATION
from sklearn.cross_validation import cross_val_score

#10-fold cross-validation with K=5 for KNN
knn = KNeighborsClassifier(n_neighbors=5)
scores = cross_val_score(knn,X,y,cv=10,scoring='accuracy')
print scores
print scores.mean()

#search for an optimal value of k for KNN
k_range = range(1,31)
k_scores=[]
for k in k_range:
    knn = KNeighborsClassifier(n_neighbors=k)
    scores = cross_val_score(knn,X,y,cv=10,scoring='accuracy')
    k_scores.append(scores.mean())
print k_scores

#plot using matplotlib
import matplotlib.pyplot as plt
plt.plot(k_range,k_scores)
plt.xlabel('Value of K for KNN')
plt.ylabel('Cross-Validated Accuracy')
#plt.show()

#take k=20 as the best model
#fit model and get score for knn(k=20)
knn = KNeighborsClassifier(n_neighbors=20)
print cross_val_score(knn,X,y,cv=10,scoring='accuracy').mean()

#now try 10-fold cross-validation with logistic regression
from sklearn.linear_model import LogisticRegression
logreg = LogisticRegression()
print cross_val_score(logreg,X,y,cv=10,scoring='accuracy').mean()

#use cross validation with feature selection
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

data  = pd.read_csv('http://www-bcf.usc.edu/~gareth/ISL/Advertising.csv', index_col=0)
feature_cols = ['TV','Radio','Newspaper']
X=data[feature_cols]
y = data.Sales

lm = LinearRegression()
scores = cross_val_score(lm,X,y,cv=10,scoring='mean_squared_error')
print scores

#fix the sign of MSE scores
mse_scores = -scores
print mse_scores

#convert to root mse
rmse_scores = np.sqrt(mse_scores)
print rmse_scores.mean()

feature_cols = ['TV','Radio']
X=data[feature_cols]
print np.sqrt(-cross_val_score(lm,X,y,cv=10,scoring='mean_squared_error')).mean()

 



