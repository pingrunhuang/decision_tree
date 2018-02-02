import pandas as pd
from DTree.common_utils import entropy, info_gain_ratio

# From the output we can see that C45 tree get a better result

def _split_sequencial_data(dataset, feature):
    

def _belong_to_which_class(dataset, target):
    target_values=dataset[target].unique()
    max_records_num = 0
    class_value = None
    for target_value in target_values:
        if dataset[dataset[target]==target_value].size>max_records_num:
            class_value=target_value
    return class_value


def generate_C45Tree(dataset, target_feature, feature_set, epsilon):
    # ID3Tree is a dictionary type with the key is the feature and value is either target value or tree node
    
    if len(dataset[target_feature].unique())==1:
        return {'class':dataset[target_feature].unique()[0]}

    if feature_set is None or len(feature_set)==0:
        return {'class':_belong_to_which_class(dataset, target_feature)}

    feature_max_info_gain=info_gain_ratio(dataset, feature_set[0], target_feature)
    root_feature=feature_set[0]

    # get the root feature
    for feature in feature_set:
        if feature_max_info_gain<info_gain_ratio(dataset, feature, target_feature):
            root_feature=feature
    if info_gain_ratio(dataset, root_feature, target_feature)<epsilon:
        return {'class':_belong_to_which_class(dataset, target_feature)}
    else:
        sub_features = [x for x in feature_set if x != root_feature]
        feature_values = dataset[root_feature].unique()
        sub_datasets = [dataset[dataset[root_feature]==feature_value] for feature_value in feature_values]
        nodes = dict()
        for i,f in enumerate(feature_values):
            nodes[f] = generate_C45Tree(sub_datasets[i], target_feature, sub_features, epsilon)
        return {root_feature:nodes}

