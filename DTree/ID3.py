import tqdm
import pandas as pd
from common_utils import entropy, info_gain, info_gain_ratio

class ID3Tree(object):
    def __init__(self, value, next_features):
        self.value = value
        self.next = next_features
    
def gen_tree(dataset, target_feature, epsilon):
    if type(dataset) is not pd.DataFrame:
        raise ValueError("Dataset should be of dataframe type")

    if dataset[target_feature].unique()==1:
        return ID3Tree(target_feature, None)

    features=dataset.columns
    

