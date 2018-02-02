#/bin/python

from DTree.C45 import generate_C45Tree
import pandas as pd

def train(input_data, target_feature, epsilon):
    feature_set = [x for x in input_data.columns if x != target_feature]
    return generate_C45Tree(input_data, target_feature, feature_set, epsilon)
