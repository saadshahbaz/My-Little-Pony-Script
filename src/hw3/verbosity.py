import pandas as pd
import json
import re

def verbosity(df):
    for_verbosity = 0
    verbosity_dict = {"twilight": 0, "applejack": 0, "rarity": 0, "pinkie": 0, "rainbow": 0, "fluttershy": 0}

    d = df.to_dict()
    for column in range(len(d['pony'])):
        if ("Twilight Sparkle" in d['pony'][column] and "and" not in d["pony"][column]):
            if ("Twilight Sparkle" not in d['pony'][column + 1]):
                verbosity_dict["twilight"] += 1
                for_verbosity += 1
            else:
                continue
        if ("Applejack" in d['pony'][column] and "and" not in d["pony"][column]):
            if ("Applejack" not in d['pony'][column + 1]):
                verbosity_dict["applejack"] += 1
                for_verbosity += 1
            else:
                continue
        if ("Rarity" in d['pony'][column] and "and" not in d["pony"][column]):
            if ("Rarity" not in d['pony'][column + 1]):
                verbosity_dict["rarity"] += 1
                for_verbosity += 1
            else:
                continue
        if ("Pinkie Pie" in d['pony'][column] and "and" not in d["pony"][column]):
            if ("Pinkie Pie" not in d['pony'][column + 1]):
                verbosity_dict["pinkie"] += 1
                for_verbosity += 1
            else:
                continue
        if ("Rainbow Dash" in d['pony'][column] and "and" not in d["pony"][column]):
            if ("Rainbow Dash" not in d['pony'][column + 1]):
                verbosity_dict["rainbow"] += 1
                for_verbosity += 1
            else:
                continue
        if ("Fluttershy" in d['pony'][column] and "and" not in d["pony"][column]):
            if ("Fluttershy" not in d['pony'][column + 1]):
                verbosity_dict["fluttershy"] += 1
                for_verbosity += 1
            else:
                continue
    #         else:
    #             verbosity_dict["others"] += 1
    #             for_verbosity+=1

    #     print(verbosity_dict)
    for key in verbosity_dict:
        verbosity_dict[key] = round(verbosity_dict[key] / for_verbosity,2)

    return verbosity_dict