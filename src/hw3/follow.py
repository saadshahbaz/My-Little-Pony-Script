import pandas as pd
import json
import re

def follow_on(df):
    d = df.to_dict()

    t2_d = {"applejack": 0, "rarity": 0, "pinkie": 0, "rainbow": 0, "fluttershy": 0, "other": 0}
    a2_d = {"twilight": 0, "rarity": 0, "pinkie": 0, "rainbow": 0, "fluttershy": 0, "other": 0}
    r2_d = {"twilight": 0, "applejack": 0, "pinkie": 0, "rainbow": 0, "fluttershy": 0, "other": 0}
    p2_d = {"twilight": 0, "applejack": 0, "rarity": 0, "rainbow": 0, "fluttershy": 0, "other": 0}
    ra2_d = {"twilight": 0, "applejack": 0, "rarity": 0, "pinkie": 0, "fluttershy": 0, "other": 0}
    f2_d = {"twilight": 0, "applejack": 0, "rarity": 0, "pinkie": 0, "rainbow": 0, "other": 0}

    follow_on_comments = {"twilight": t2_d, "applejack": a2_d, "rarity": r2_d, "pinkie": p2_d, "rainbow": ra2_d,
                    "fluttershy": f2_d}
    twilight_countss=0
    applejack_counts=0
    rarity_counts=0
    pinkie_counts=0
    rainbow_counts=0
    fluttershy_counts = 0

    for column in range(len(d['pony'])):
        if ("Twilight" in d['pony'][column] and "and" not in d['pony'][column]):
            if ("Applejack" in d['pony'][column + 1] and "and" not in d['pony'][column+1]):
                follow_on_comments["twilight"]["applejack"] += 1
                twilight_countss += 1
            elif ("Pinkie Pie" in d['pony'][column + 1] and "and" not in d['pony'][column+1] ):
                follow_on_comments["twilight"]["pinkie"] += 1
                twilight_countss += 1
            elif ("Rarity" in d['pony'][column + 1] and "and" not in d['pony'][column+1]):
                follow_on_comments["twilight"]["rarity"] += 1
                twilight_countss += 1
            elif ("Rainbow Dash" in d['pony'][column + 1] and "and" not in d['pony'][column+1]):
                follow_on_comments["twilight"]["rainbow"] += 1
                twilight_countss += 1
            elif ("Fluttershy" in d['pony'][column + 1] and "and" not in d['pony'][column+1] ):
                follow_on_comments["twilight"]["fluttershy"] += 1
                twilight_countss += 1
            else:
                follow_on_comments["twilight"]["other"] += 1
                twilight_countss+=1

        elif ("Applejack" in d['pony'][column] and "and" not in d['pony'][column]):
            if ("Twilight Sparkle" in d['pony'][column + 1] and "and" not in d['pony'][column+1]):
                follow_on_comments["applejack"]["twilight"] += 1
                applejack_counts += 1
            elif ("Pinkie Pie" in d['pony'][column + 1] and "and" not in d['pony'][column+1]):
                follow_on_comments["applejack"]["pinkie"] += 1
                applejack_counts += 1
            elif ("Rarity" in d['pony'][column + 1] and "and" not in d['pony'][column+1]):
                follow_on_comments["applejack"]["rarity"] += 1
                applejack_counts += 1
            elif ("Rainbow Dash" in d['pony'][column + 1] and "and" not in d['pony'][column+1]):
                follow_on_comments["applejack"]["rainbow"] += 1
                applejack_counts += 1
            elif ("Fluttershy" in d['pony'][column + 1] and "and" not in d['pony'][column+1]):
                follow_on_comments["applejack"]["fluttershy"] += 1
                applejack_counts += 1
            else:
                follow_on_comments["applejack"]["other"] += 1
                applejack_counts+=1

        if ("Rarity" in d['pony'][column] and "and" not in d['pony'][column]):
            if ("Applejack" in d['pony'][column + 1] and "and" not in d['pony'][column+1]):
                follow_on_comments["rarity"]["applejack"] += 1
                rarity_counts += 1
            elif ("Pinkie Pie" in d['pony'][column + 1] and "and" not in d['pony'][column+1]):
                follow_on_comments["rarity"]["pinkie"] += 1
                rarity_counts += 1
            elif ("Twilight Sparkle" in d['pony'][column + 1] and "and" not in d['pony'][column+1]):
                follow_on_comments["rarity"]["twilight"] += 1
                rarity_counts += 1
            elif ("Rainbow Dash" in d['pony'][column + 1] and "and" not in d['pony'][column+1]):
                follow_on_comments["rarity"]["rainbow"] += 1
                rarity_counts += 1
            elif ("Fluttershy" in d['pony'][column + 1] and "and" not in d['pony'][column+1]):
                follow_on_comments["rarity"]["fluttershy"] += 1
                rarity_counts += 1
            else:
                follow_on_comments["rarity"]["other"] += 1
                rarity_counts+=1

        if ("Pinkie Pie" in d['pony'][column] and "and" not in d['pony'][column]):
            if ("Applejack" in d['pony'][column + 1] and "and" not in d['pony'][column+1]):
                follow_on_comments["pinkie"]["applejack"] += 1
                pinkie_counts += 1
            elif ("Twilight Sparkle" in d['pony'][column + 1] and "and" not in d['pony'][column+1]):
                follow_on_comments["pinkie"]["twilight"] += 1
                pinkie_counts += 1
            elif ("Rarity" in d['pony'][column + 1] and "and" not in d['pony'][column+1]):
                follow_on_comments["pinkie"]["rarity"] += 1
                pinkie_counts += 1
            elif ("Rainbow Dash" in d['pony'][column + 1] and "and" not in d['pony'][column+1]):
                follow_on_comments["pinkie"]["rainbow"] += 1
                pinkie_counts += 1
            elif ("Fluttershy" in d['pony'][column + 1] and "and" not in d['pony'][column+1]):
                follow_on_comments["pinkie"]["fluttershy"] += 1
                pinkie_counts += 1
            else:
                follow_on_comments["pinkie"]["other"] += 1
                pinkie_counts+=1

        if ("Rainbow Dash" in d['pony'][column] and "and" not in d['pony'][column]):
            if ("Applejack" in d['pony'][column + 1] and "and" not in d['pony'][column+1]):
                follow_on_comments["rainbow"]["applejack"] += 1
                rainbow_counts += 1
            elif ("Pinkie Pie" in d['pony'][column + 1] and "and" not in d['pony'][column+1]):
                follow_on_comments["rainbow"]["pinkie"] += 1
                rainbow_counts += 1
            elif ("Rarity" in d['pony'][column + 1] and "and" not in d['pony'][column+1]):
                follow_on_comments["rainbow"]["rarity"] += 1
                rainbow_counts += 1
            elif ("Twilight Sparkle" in d['pony'][column + 1] and "and" not in d['pony'][column+1]):
                follow_on_comments["rainbow"]["twilight"] += 1
                rainbow_counts += 1
            elif ("Fluttershy" in d['pony'][column + 1] and "and" not in d['pony'][column+1]):
                follow_on_comments["rainbow"]["fluttershy"] += 1
                rainbow_counts += 1
            else:
                follow_on_comments["rainbow"]["other"] += 1
                rainbow_counts+=1

        if ("Fluttershy" in d['pony'][column] and "and" not in d['pony'][column]):  
            if ("Applejack" in d['pony'][column + 1] and "and" not in d['pony'][column+1]):
                follow_on_comments["fluttershy"]["applejack"] += 1
                fluttershy_counts += 1
            elif ("Pinkie Pie" in d['pony'][column + 1] and "and" not in d['pony'][column+1]):
                follow_on_comments["fluttershy"]["pinkie"] += 1
                fluttershy_counts += 1
            elif ("Rarity" in d['pony'][column + 1] and "and" not in d['pony'][column+1]):
                follow_on_comments["fluttershy"]["rarity"] += 1
                fluttershy_counts += 1
            elif ("Rainbow Dash" in d['pony'][column + 1] and "and" not in d['pony'][column+1]):
                follow_on_comments["fluttershy"]["rainbow"] += 1
                fluttershy_counts += 1
            elif ("Twilight Sparkle" in d['pony'][column + 1] and "and" not in d['pony'][column+1]):
                follow_on_comments["fluttershy"]["twilight"] += 1
                fluttershy_counts += 1
            else:
                follow_on_comments["fluttershy"]["other"] += 1
                fluttershy_counts+=1

    # follow_on_comments = {"twilight":0,"applejack":0,"rarity":0,"pinkie":0,"rainbow":0,"fluttershy":0, "other":0}
    for key in follow_on_comments:
        for values in follow_on_comments[key]:
            if(key == "twilight"):
                follow_on_comments[key][values] = round(follow_on_comments[key][values] / twilight_countss,2)
            elif( key == "applejack"):
                follow_on_comments[key][values] = round(follow_on_comments[key][values] / applejack_counts,2)
            elif( key == "rarity"):
                follow_on_comments[key][values] = round(follow_on_comments[key][values] / rarity_counts,2)
            elif( key == "pinkie"):
                follow_on_comments[key][values] = round(follow_on_comments[key][values] / pinkie_counts,2)
            elif( key == "rainbow"):
                follow_on_comments[key][values] = round(follow_on_comments[key][values] / rainbow_counts,2)
            else:
                follow_on_comments[key][values] = round(follow_on_comments[key][values] / fluttershy_counts,2)

    return follow_on_comments