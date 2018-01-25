#/bin/python
from math import log2, log
import pandas as pd

def entropy(dataset, feature):
    '''
    The time complexity is totally depend on the number of kinds of value in a certain column
    '''
    if type(dataset)!= pd.core.frame.DataFrame:
        raise ValueError("dataset should be a pandas dataframe") 
    if type(feature)!=str:
        raise ValueError("feature should be a feature name of the column")
    x = dataset[feature]
    # when the specified column only have 2 kinds of values
    if len(x.unique()) == 2:
        tag1, tag2 = x.unique()
        p = (x==tag1).sum()/x.count()
        # in both cases the log2(p) or log2(1-p) will raise exception
        if p==1 or p==0:
            return 0
        return -p * log2(p) - (1-p) * log2(1-p)
    else:
        tags = x.unique()
        props = [(x==tag).sum()/x.count() for tag in tags]
        '''
        I was primitively trying to use the reduce syntax
        reduce((lambda x, y: (-x*log(x)-if x!=0 else 0) - (y*log(y) if y!=0 else 0)), props)
        But turns out that the previous result will be stored in the x which will result in negative
        '''
        result = 0
        for p in props:
            if p!=0:
                result+=-p*log(p)
        return result


def info_gain(dataset, feature, target):
    '''
    union propabilities: P(X=xi, Y=yj)=p(i,j)
    conditional entropy: H(Y|X)=sum(pi*H(Y|X=xi))
    In decision tree, information gain=H(D)-H(D|A) 
    where H is entropy and H(D) is the entropy for class D. 
    H(D|A) is the conditional entropy. The result is called mutual information
    '''
    if type(dataset)!= pd.core.frame.DataFrame:
        raise ValueError("dataset should be a pandas dataframe")
    if type(feature)!=str:
        raise ValueError("feature should be a feature name of the column")
    if type(target)!=str:
        raise ValueError("target should be string")
    x=dataset[feature]
    HD=entropy(dataset, target)
    feature_tags = x.unique()
    target_tags = dataset[target].unique()
    
    conditional_entropy=0
    for ti in feature_tags:
        temp_entropy = 0
        di = dataset.loc[dataset[feature]==ti]
        target_dis = [di.loc[di[target]==t] for t in target_tags]
        for d in target_dis:
            temp_entropy+=entropy(d, target)
        conditional_entropy-=temp_entropy*((dataset==ti).sum()/dataset.count())
    return conditional_entropy

def ID3():
    pass

def CART():
    pass

def train():
    pass