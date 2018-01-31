import unittest
import pandas as pd
from math import log2
from DTree.common_utils import entropy, info_gain, info_gain_ratio
import sys
sys.path.append('../DTree')

class TestUtils(unittest.TestCase):
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

    def test_entropy(self):
        expected_temperature= -(4/14 * (log2(4/14)) + 4/14 * (log2(4/14)) + 6/14 * (log2(6/14)))
        self.assertEqual(entropy(self.df, 'Temperature'), expected_temperature)
    def test_info_gain(self):
        expected_temperature_info_gain = entropy(self.df, 'PlayGolf')-(-4/14*(1/2*log2(1/2)+1/2*log2(1/2)) - 4/14*(3/4*log2(3/4)+1/4*log2(1/4)) - 6/14*(4/6*log2(4/6)+2/6*log2(2/6)))
        self.assertEqual(info_gain(self.df, 'Temperature', 'PlayGolf'), expected_temperature_info_gain)
    
    def test_info_gain_ratio(self):
        expected_temperature_info_gain_ratio = info_gain(self.df, 'Temperature', 'PlayGolf')/-(4/14*log2(4/14)+4/14*log2(4/14)+6/14*log2(6/14))
        self.assertEqual(info_gain_ratio(self.df, 'Temperature', 'PlayGolf'), expected_temperature_info_gain_ratio)

if __name__=='__main__':
    unittest.main()