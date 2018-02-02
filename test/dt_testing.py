#!/bin/python
#encoding=utf-8

import pandas as pd
import unittest
import sys
from DTree.ID3 import generate_ID3Tree
from DTree.C45 import generate_C45Tree

class TestTreeGen(unittest.TestCase):
    '''
    Day,Temperature,Outlook,Humidity,Windy,PlayGolf
    07-05,hot,sunny,high,false,no
    07-06,hot,sunny,high,true,no
    07-07,hot,overcast,high,false,yes
    07-09,cool,rain,normal,false,yes
    07-10,cool,overcast,normal,true,yes
    07-12,mild,sunny,high,false,no
    07-14,cool,sunny,normal,false,yes
    07-15,mild,rain,normal,false,yes
    07-20,mild,sunny,normal,true,yes
    07-21,mild,overcast,high,true,yes
    07-22,hot,overcast,normal,false,yes
    07-23,mild,sunny,high,true,no
    07-26,cool,sunny,normal,true,no
    07-30,mild,sunny,high,false,yes
    '''
    def setUp(self):
        self.df = pd.read_csv(sys.path[0]+"/sample_data.csv", sep=',')
        self.target = 'PlayGolf'
        self.features = [x for x in self.df.columns if x!=self.target and x!='Day']
    
    def test_generate_ID3Tree(self):
        print('Testing ID3 tree generation')
        print(generate_ID3Tree(self.df, self.target, self.features, 0.1))

    def test_generate_C45Tree(self):
        print('Testing c45 tree generation')
        print(generate_C45Tree(self.df, self.target, self.features, 0.01))

if __name__=='__main__':
    unittest.main()