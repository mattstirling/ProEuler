'''
Created on Oct 13, 2015

@author: Trader
'''
# import load_iris function from datasets module
from sklearn.datasets import load_iris

iris = load_iris()


# 4 data requirements for scikit-learn

# 1. Features and Response are separate objects
# already done for us: iris.data and iris.target

# 2. Features and Response are numeric
print iris.data
print iris.target
print iris.feature_names
print iris.target_names

# 3. Features and Response are NumPy Arrays
print type(iris.data)
print type(iris.target)

#4. Features and Response should have specific shapes
print iris.data.shape
print iris.target.shape

#done, okay now use X and y
X = iris.data
y = iris.target

'''
#an aside, a good quick visualization
import seaborn as sns
data = sns.load_dataset('iris')
g = sns.pairplot(data, hue="species")
sns.plt.show()

# g = sns.PairGrid(data)
#g.map(plt.scatter);
'''
