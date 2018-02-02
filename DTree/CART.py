#!/bin/python
import pandas as pd

# 基尼指数类似熵，值越大表示样本集合的不确定性越大

def gini(dataset, target):
    if type(dataset)!=pd.DataFrame:
        raise ValueError('first argument should be a dataset')
    classes = dataset[target].unique()
    classes_dataset = [dataset[dataset[target]==c] for c in classes]
    return 1-sum([(x.size/dataset.size)**2 for x in classes_dataset)

def gini_based_on_feature(dataset, feature, target):
    if type(dataset)!=pd.DataFrame:
        raise ValueError('first argument should be a dataset')
    classes = dataset[target].unique()
    feature_values = dataset[feature].unique()
    min_gini = (dataset[dataset[feature]==feature_values[0]].size * gini(dataset[dataset[feature]==feature_values[0]], target) + \
        dataset[dataset[feature]!=feature_values[0]].size * gini(dataset[dataset[feature]!=feature_values[0]], target)) 
    split_point = feature_values[0]
    for value in feature_values:
        cur_gini = dataset[dataset[feature]==value].size * gini(dataset[dataset[feature]==value], target) + \
            dataset[dataset[feature]!=value].size * gini(dataset[dataset[feature]!=value], target)
        if min_gini>cur_gini:
            min_gini=cur_gini
            split_point=value
    return min_gini, split_point


def gen_cart(dataset):
    if type(dataset)!=pd.DataFrame:
        raise ValueError('first argument should be a dataset')
    