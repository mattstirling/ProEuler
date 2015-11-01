'''
Created on Oct 15, 2015

@author: Trader
'''

# import load_iris function from datasets module
from sklearn.datasets import load_iris
iris = load_iris()

#once we confirm data is ready for scikit-learn, use X and y
X = iris.data
y = iris.target

#check shape
print X.shape
print y.shape

#1. import the class you would like to use
from sklearn.neighbors import KNeighborsClassifier

#2. instantiate the estimator, ie. make an instance of the model
knn = KNeighborsClassifier(n_neighbors=5)

#3. Fit the model
knn.fit(X, y)

#4. Predict the response for a new observation
# NB - numpy array is expected, but the below command converts this list into a numpy array
predict_A = knn.predict([3,5,4,2])
print predict_A

X_new = [[3,5,4,2],[5,4,3,2]]
predict_B = knn.predict(X_new)
print predict_B


#now repeat for logistic regression
#1. import the class you would like to use
from sklearn.linear_model import LogisticRegression

#2. instantiate the model using default parameters
logreg = LogisticRegression()

#3. Fit the model
logreg.fit(X, y)

#4. Predict the response for a new observation
# NB - numpy array is expected, but the below command converts this list into a numpy array
predict_C = logreg.predict(X_new)
print predict_C





