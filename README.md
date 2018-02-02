# Dataset description
this project's dataset is from this [kaggle competetion](www.kaggle.com/zaurbegiev/my-dataset/data/). You can find some description there. But basically the column is self-explained. 100000 rows of records for training and 10000 rows of records for testing.

# Project description
This is my self implementation of the decision tree. It is originally from [统计学习方法 李航](https://item.jd.com/10975302.html)

To run the unittest:

```
$ export PYTHONPATH=$PYTHONPATH:`pwd`
$ cd test
$ python -m unittest common_func_testing.py
```

# Problems 1

1. the larger the entropy is, the more uncertain a variable is.

# The purpose of the info gain is by knowing the info of a certain feature X, how much uncertainty we can reduce to determine which class Y belongs to.

# Actually the process of generating a decision tree is shinking both columns and rows


# process
```
decision tree --> regression tree (square error minimization) --> classification tree(gini index minimization)
```