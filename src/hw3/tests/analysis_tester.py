import unittest
from ..verbosity import verbosity
from ..follow import follow_on
from ..jsonfile import jsonconverter
from ..mentions import mentions
from ..non_dictionary_words import non_dictionary_words
import pandas as pd


class VerbosityTestCase(unittest.TestCase):
    #check if all ponys are mentioned in speech acts
    def test_one(self):
        x = verbosity(pd.read_csv("../data/clean_dialog.csv"))
        y=list(x.keys())
        self.assertEqual(y, ['twilight', 'applejack', 'rarity', 'pinkie', 'rainbow', 'fluttershy'])

    def test_two(self):
        #if the sum of verbosity equal to 1
        x = verbosity(pd.read_csv("../data/clean_dialog.csv"))
        dict_v = sum(x.values())
        dict_v = round(dict_v)
        self.assertEqual(1,dict_v) 

    def test_three(self):
        #if the sum of mentions[specific pony] is one
        x= mentions(pd.read_csv("../data/clean_dialog.csv"))
        y = x["rainbow"]
        sumofy = sum(y.values())
        sumofy = round(sumofy)
        self.assertEqual(1,sumofy) 

    def test_four(self):
        #if the sum of follow_on_comments[specific pony] equal to one
        x = follow_on(pd.read_csv("../data/clean_dialog.csv"))
        y=x['applejack']
        sumofy = sum(y.values())
        sumofy = round(sumofy)
        self.assertEqual(1,sumofy) 

    def test_five(self):
        #if mentions returns 5 ponys's mention
        x= mentions(pd.read_csv("../data/clean_dialog.csv"))
        y=len(x["fluttershy"])
        self.assertEqual(5,y) 

    def test_six(self):
        #if 5 values are returned
        x = non_dictionary_words(pd.read_csv("../data/clean_dialog.csv"))
        y = len(x['applejack'])
        self.assertEqual(5,y) 

    def test_seven(self):
        #if the values are not in the file
        with open('../data/words_alpha.txt') as file:
            dictionary_set = set(word.strip().lower() for word in file)    
        x = non_dictionary_words(pd.read_csv("../data/clean_dialog.csv"))

        self.assertEqual((x["twilight"][0] in dictionary_set in dictionary_set),False) 

    def test_eight(self):
        #if others is included in follow on comments
        x = follow_on(pd.read_csv("../data/clean_dialog.csv"))
        y = x['applejack']
        keycheck = False
        for key in y:
            if ("other" == key):
                keycheck = True
        self.assertEqual(keycheck,True) 

    def test_nine(self):
        #if the top 5 non-dictionary words are returned for all ponies
        x = non_dictionary_words(pd.read_csv("../data/clean_dialog.csv"))
        y=list(x.keys())
        self.assertEqual(y,['twilight', 'applejack', 'pinkie', 'rarity', 'fluttershy', 'rainbow']) 

    def test_ten(self):
        #if all the values returned are a dictionary
        a = non_dictionary_words(pd.read_csv("../data/clean_dialog.csv"))
        b = follow_on(pd.read_csv("../data/clean_dialog.csv"))
        c = verbosity(pd.read_csv("../data/clean_dialog.csv"))
        d= mentions(pd.read_csv("../data/clean_dialog.csv"))

        x = False
        if (type(a) == dict and type(b)== dict and type(c)== dict and type(d)== dict):
            x=True
        self.assertEqual(x,True)       
