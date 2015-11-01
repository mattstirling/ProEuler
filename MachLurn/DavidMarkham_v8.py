'''
Created on Oct 17, 2015

@author: Trader
'''
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cross_validation import cross_val_score
import matplotlib.pyplot as plt

#read in iris data, set to X, y
iris = load_iris()
X = iris.data
y = iris.target

#10-fold cross-validation with K=5 for KNN
knn = KNeighborsClassifier(n_neighbors=5)
scores = cross_val_score(knn,X,y,cv=10,scoring='accuracy')
print scores
print scores.mean()

#search for an optimal value, k, for KNN
k_range = range(1,31)
k_scores=[]
for k in k_range:
    knn = KNeighborsClassifier(n_neighbors=k)
    scores = cross_val_score(knn,X,y,cv=10,scoring='accuracy')
    k_scores.append(scores.mean())

#plot using matplotlib
plt.plot(k_range,k_scores)
plt.xlabel('Value of K for KNN')
plt.ylabel('Cross-Validated Accuracy')
#plt.show()

#conclude that k=20 is an optimal value

#
#
#NOW USE GridSearchCV
from sklearn.grid_search import GridSearchCV
k_range = range(1,31)

#create a parameter grid
param_grid = dict(n_neighbors=k_range)
print param_grid

#instantiate the grid
grid = GridSearchCV(knn,param_grid,cv=10,scoring='accuracy')
grid.fit(X,y)
print grid.grid_scores_

#examine the first tuple
print grid.grid_scores_[0].parameters
print grid.grid_scores_[0].cv_validation_scores
print grid.grid_scores_[0].mean_validation_score

#create a list of the mean scores only
grid_mean_scores = [result.mean_validation_score for result in grid.grid_scores_]
print grid_mean_scores

#plot the results
plt.plot(k_range,grid_mean_scores)
plt.xlabel('Value of K for KNN')
plt.ylabel('Cross-Validated Accuracy')
#plt.show()

#examine the best model
print grid.best_score_
print grid.best_params_
print grid.best_estimator_

#
#
#What about multiple parameters simultaneously?
k_range = range(1,31)
weight_options = ['uniform','distance']

param_grid = dict(n_neighbors=k_range,weights=weight_options)
print param_grid

grid = GridSearchCV(knn,param_grid,cv=10,scoring='accuracy')
grid.fit(X,y)
print grid.grid_scores_
print grid.best_score_
print grid.best_params_

#use the best parameters to make predictions
knn = KNeighborsClassifier(n_neighbors=13,weights='uniform')
knn.fit(X, y)
print knn.predict([3,5,4,2])

#shortcut!
print grid.predict([3,5,4,2])

#
#
# now use RandomizedSearchCV
from sklearn.grid_search import RandomizedSearchCV
param_dist = dict(n_neighbors=k_range,weights=weight_options)
#NOTE - sepcify a continuous distribution for continuous parameters

#n_iter controls the number of searches
rand = RandomizedSearchCV(knn,param_dist,cv=10,scoring='accuracy',n_iter=10,random_state=5)
rand.fit(X, y)
rand.grid_scores_

print rand.best_score_
print rand.best_params_

print 'done this lesson x2'


