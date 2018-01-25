import pandas as pd
import numpy as np

dataset = pd.read_csv('./dataset/credit_train.csv')

print(dataset.describe())
# checking the unique value for each column

for column in dataset.columns:
    print(column,':')
    print(dataset[column].unique())

# count the 0 value for each column
columns = dataset.columns
print((dataset[columns]==0).sum())

# count the total NaN value for each column
# sometimes we can even replace the 0 value with this function replace(0, numpy.NaN), the numpy.NaN could be ignore automatically by some framework
print(dataset.isnull().sum())

# strategy 1:dropping the missing NaN 
dataset1 = dataset.dropna()
print(dataset1.isnull().sum())

# strategy 2: impute the missing value, mean for example
dataset2 = dataset.fillna(dataset.mean())
print(dataset2.isnull().sum())
# or use sklearn's imputer class 
from sklearn.preprocessing import Imputer

imputer = Imputer()
values = dataset.values
transformed_values = imputer.fit_transform(values)
print(transformed_values.isnull().sum())

# with LDA Algo 
imputer = Imputer()
values = dataset.values
X = values[:,0:8]
y = values[:,8]
# fill missing values with mean column values
transformed_X = imputer.fit_transform(x)
# evaluate an LDA model on the dataset using k-fold cross validation
model = LinearDiscriminantAnalysis()
kfold = KFold(n_splits=3, random_state=7)
result = cross_val_score(model, transformed_X, y, cv=kfold, scoring='accuracy')
print(result.mean())




