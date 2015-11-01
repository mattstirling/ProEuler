'''
Created on Oct 17, 2015

@author: Trader
'''
import pandas as pd
import numpy as np

#read in the data
data  = pd.read_csv('http://www-bcf.usc.edu/~gareth/ISL/Advertising.csv', index_col=0)

#display the first 5 rows
print data.head()

#display the last 5 rows
print data.tail()

#display the shape of the data
print data.shape

#conventional way to import seaborn
#import seaborn as sns
#sns.pairplot(data,x_vars=['TV','Radio','Newspaper'],y_vars='Sales', aspect = 0.7, kind = 'reg')
#sns.plt.show()

#creata a Python list of feature names
feature_cols = ['TV','Radio','Newspaper']

#use this list to collect a subset of the original DataFrame
X=data[feature_cols]
#X=data[['TV','Radio','Newspaper']]

#print the first 5 rows
print X.head()

y = data['Sales']

print y.head()

from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,random_state=1)
#default test size is .25

from sklearn.linear_model import LinearRegression

#instantiate
linreg = LinearRegression()

#fit
linreg.fit(X_train,y_train)

#look at paramenters
print linreg.intercept_
print linreg.coef_
print zip(feature_cols,linreg.coef_)

#predict?
y_pred = linreg.predict(X_test)

#calculate MAE using scikit-learn
from sklearn import metrics
print metrics.mean_absolute_error(y_test,y_pred)
print np.sqrt(metrics.mean_squared_error(y_test,y_pred))

#now redo without the Newspaper feature
feature_cols = ['TV','Radio']
X = data[feature_cols]
y = data['Sales']
X_train, X_test,y_train,y_test = train_test_split(X,y,random_state=1)
linreg.fit(X_train,y_train)
y_pred = linreg.predict(X_test)
print np.sqrt(metrics.mean_squared_error(y_test,y_pred))

