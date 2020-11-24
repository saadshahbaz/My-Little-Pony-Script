from ast import parse
from os import name
import pandas as pd
import json
import re
import sys
import argparse

from hw3.verbosity import verbosity
from hw3.mentions import mentions
from hw3.follow import follow_on
from hw3.non_dictionary_words import non_dictionary_words
from hw3.jsonfile import jsonconverter


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('src_file', help='The clean data file used for this assignment')
    #for json
    parser.add_argument('-o', help="writing json files as outputs", default='stdout')
    args = parser.parse_args()

    src_file = args.src_file
    optional = args.o


    df = pd.read_csv(src_file)
    verbosity_dict = verbosity(df)
    mention_dict = mentions(df)
    follow_on_comments = follow_on(df)
    new_non_dict = non_dictionary_words(df)

    final_dict = {"verbosity":verbosity_dict, "mentions": mention_dict, "follow_on_comments": follow_on_comments, "non_dictionary_words":new_non_dict}

    jsonconverter(final_dict, optional)
    

if __name__ == "__main__":
    main()





