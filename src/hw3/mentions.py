import pandas as pd
import json
import re

def mentions(df):
    d = df.to_dict()
    for_mention = 0
    t1_d = {"applejack": 0, "rarity": 0, "pinkie": 0, "rainbow": 0, "fluttershy": 0}
    a1_d = {"twilight": 0, "rarity": 0, "pinkie": 0, "rainbow": 0, "fluttershy": 0}
    r1_d = {"twilight": 0, "applejack": 0, "pinkie": 0, "rainbow": 0, "fluttershy": 0}
    p1_d = {"twilight": 0, "applejack": 0, "rarity": 0, "rainbow": 0, "fluttershy": 0}
    ra1_d = {"twilight": 0, "applejack": 0, "rarity": 0, "pinkie": 0, "fluttershy": 0}
    f1_d = {"twilight": 0, "applejack": 0, "rarity": 0, "pinkie": 0, "rainbow": 0}

    mention_dict = {"twilight": t1_d, "applejack": a1_d, "rarity": r1_d, "pinkie": p1_d, "rainbow": ra1_d,
                    "fluttershy": f1_d}

    for_mention = 0
    pinkie_mention=0
    apple_jack_mention = 0
    rainbow_mention=0
    rarity_mention=0
    fluttershy_mention=0
    for column in range(len(d['pony'])):
        if (d['pony'][column] == "Twilight Sparkle"):
            if ("Applejack" in d['dialog'][column]):
                mention_dict["twilight"]["applejack"] += d['dialog'][column].count("Applejack")
                for_mention += d['dialog'][column].count("Applejack")
            if ("Pinkie Pie" in d['dialog'][column] or "Pinkie" in d['dialog'][column] or "Pie" in d['dialog'][column]):
                mention_dict["twilight"]["pinkie"] += d['dialog'][column].count("Pinkie")
                for_mention += d['dialog'][column].count("Pinkie")
            if ("Rarity" in d['dialog'][column]):
                mention_dict["twilight"]["rarity"] += d['dialog'][column].count("Rarity")
                for_mention += d['dialog'][column].count("Rarity")
            if ("Rainbow Dash" in d['dialog'][column] or "Dash" in d['dialog'][column] or "Rainbow" in d['dialog'][
                column]):   
                mention_dict["twilight"]["rainbow"] += d['dialog'][column].count("Rainbow")
                for_mention += d['dialog'][column].count("Rainbow")
            if ("Fluttershy" in d['dialog'][column]):
                mention_dict["twilight"]["fluttershy"] += d['dialog'][column].count("Fluttershy")
                for_mention += d['dialog'][column].count("Fluttershy")
            #else:
            # mention_dict["twilight"]["others"] += 1
            #   for_mention+=1

        elif (d['pony'][column] == "Applejack"):
            if ("Twilight Sparkle" in d['dialog'][column] or "Twilight" in d['dialog'][column] or "Sparkle" in
                    d['dialog'][column]):
                mention_dict["applejack"]["twilight"] += d['dialog'][column].count("Twilight")
                apple_jack_mention += d['dialog'][column].count("Twilight")
            if ("Pinkie Pie" in d['dialog'][column] or "Pinkie" in d['dialog'][column] or "Pie" in d['dialog'][column]):
                mention_dict["applejack"]["pinkie"] += d['dialog'][column].count("Pinkie")
                apple_jack_mention += d['dialog'][column].count("Pinkie")
            if ("Rarity" in d['dialog'][column]):
                mention_dict["applejack"]["rarity"] += d['dialog'][column].count("Rarity")
                apple_jack_mention += d['dialog'][column].count("Rarity")
            if ("Rainbow Dash" in d['dialog'][column] or "Dash" in d['dialog'][column] or "Rainbow" in d['dialog'][
                column]):
                mention_dict["applejack"]["rainbow"] += d['dialog'][column].count("Rainbow")
                apple_jack_mention += d['dialog'][column].count("Rainbow")
            if ("Fluttershy" in d['dialog'][column]):
                mention_dict["applejack"]["fluttershy"] += d['dialog'][column].count("Fluttershy")
                apple_jack_mention += d['dialog'][column].count("Fluttershy")
            #else:
                #mention_dict["applejack"]["others"] += 1
            #   for_mention+=1

        if (d['pony'][column]=="Rarity"):
            if ("Applejack" in d['dialog'][column]):
                mention_dict["rarity"]["applejack"] += d['dialog'][column].count("Applejack")
                rarity_mention += d['dialog'][column].count("Applejack")
            if ("Pinkie Pie" in d['dialog'][column] or "Pinkie" in d['dialog'][column] or "Pie" in d['dialog'][column]):
                mention_dict["rarity"]["pinkie"] += d['dialog'][column].count("Pinkie")
                rarity_mention += d['dialog'][column].count("Pinkie")
            if ("Twilight Sparkle" in d['dialog'][column] or "Twilight" in d['dialog'][column] or "Sparkle" in
                d['dialog'][column]):
                mention_dict["rarity"]["twilight"] += d['dialog'][column].count("Twilight")
                rarity_mention += d['dialog'][column].count("Twilight")
            if ("Rainbow Dash" in d['dialog'][column] or "Dash" in d['dialog'][column] or "Rainbow" in d['dialog'][
                column]):
                mention_dict["rarity"]["rainbow"] += d['dialog'][column].count("Rainbow")
                rarity_mention += d['dialog'][column].count("Rainbow")
            if ("Fluttershy" in d['dialog'][column]):
                mention_dict["rarity"]["fluttershy"] += d['dialog'][column].count("Fluttershy")
                rarity_mention += d['dialog'][column].count("Fluttershy")
            #else:
            # mention_dict["rarity"]["others"] += 1
            # for_mention+=1

        if (d['pony'][column]=="Pinkie Pie"):
            if ("Applejack" in d['dialog'][column]):
                mention_dict["pinkie"]["applejack"] += d['dialog'][column].count("Applejack")
                pinkie_mention += d['dialog'][column].count("Applejack")
            if ("Twilight Sparkle" in d['dialog'][column] or "Twilight" in d['dialog'][column] or "Sparkle" in
                d['dialog'][column]):
                mention_dict["pinkie"]["twilight"] += d['dialog'][column].count("Twilight")
                pinkie_mention += d['dialog'][column].count("Twilight")
            if ("Rarity" in d['dialog'][column]):
                mention_dict["pinkie"]["rarity"] += d['dialog'][column].count("Rarity")
                pinkie_mention += d['dialog'][column].count("Rarity")
            if ("Rainbow Dash" in d['dialog'][column] or "Dash" in d['dialog'][column] or "Rainbow" in d['dialog'][
                column]):
                mention_dict["pinkie"]["rainbow"] += d['dialog'][column].count("Rainbow")
                pinkie_mention += d['dialog'][column].count("Rainbow")
            if ("Fluttershy" in d['dialog'][column]):
                mention_dict["pinkie"]["fluttershy"] += d['dialog'][column].count("Fluttershy")
                pinkie_mention += d['dialog'][column].count("Fluttershy")
            #else:
            # mention_dict["pinkie"]["others"] += 1
            #   for_mention+=1

        if (d['pony'][column]=="Rainbow Dash"):
            if ("Applejack" in d['dialog'][column]):
                mention_dict["rainbow"]["applejack"] += d['dialog'][column].count("Applejack")
                rainbow_mention += d['dialog'][column].count("Applejack")
            if ("Pinkie Pie" in d['dialog'][column] or "Pinkie" in d['dialog'][column] or "Pie" in d['dialog'][column]):
                mention_dict["rainbow"]["pinkie"] += (d['dialog'][column].count("Pinkie"))
                rainbow_mention += (d['dialog'][column].count("Pinkie"))
            if ("Rarity" in d['dialog'][column]):
                mention_dict["rainbow"]["rarity"] += d['dialog'][column].count("Rarity")
                rainbow_mention += d['dialog'][column].count("Rarity")
            if ("Twilight Sparkle" in d['dialog'][column] or "Twilight" in d['dialog'][column] or "Sparkle" in
                d['dialog'][column]):
                mention_dict["rainbow"]["twilight"] += d['dialog'][column].count("Twilight")
                rainbow_mention += d['dialog'][column].count("Twilight")
            if ("Fluttershy" in d['dialog'][column]):
                mention_dict["rainbow"]["fluttershy"] += d['dialog'][column].count("Fluttershy")
                rainbow_mention += d['dialog'][column].count("Fluttershy")
            #else:
            #  mention_dict["rainbow"]["others"] += 1
            # for_mention+=1

        if (d['pony'][column]=="Fluttershy"):
            if ("Applejack" in d['dialog'][column]):
                mention_dict["fluttershy"]["applejack"] += d['dialog'][column].count("Applejack")
                fluttershy_mention += d['dialog'][column].count("Applejack")
            if ("Pinkie Pie" in d['dialog'][column] or "Pinkie" in d['dialog'][column] or "Pie" in d['dialog'][column]):
                mention_dict["fluttershy"]["pinkie"] += d['dialog'][column].count("Pinkie")
                fluttershy_mention += d['dialog'][column].count("Pinkie")
            if ("Rarity" in d['dialog'][column]):
                mention_dict["fluttershy"]["rarity"] += d['dialog'][column].count("Rarity")
                fluttershy_mention += d['dialog'][column].count("Rarity")
            if ("Rainbow Dash" in d['dialog'][column] or "Dash" in d['dialog'][column] or "Rainbow" in d['dialog'][
                column]):
                mention_dict["fluttershy"]["rainbow"] += d['dialog'][column].count("Rainbow")
                fluttershy_mention += d['dialog'][column].count("Rainbow")
            if ("Twilight Sparkle" in d['dialog'][column] or "Twilight" in d['dialog'][column] or "Sparkle" in
                d['dialog'][column]):
                mention_dict["fluttershy"]["twilight"] += d['dialog'][column].count("Twilight")
                fluttershy_mention += d['dialog'][column].count("Twilight")
            #else:
            # mention_dict["fluttershy"]["others"] += 1
            # for_mention+=1



    for key in mention_dict:
        for values in mention_dict[key]:
            if(key == "twilight"):
                mention_dict[key][values] = round(mention_dict[key][values] / for_mention,2)
            elif( key == "applejack"):
                mention_dict[key][values] = round(mention_dict[key][values] / apple_jack_mention,2)
            elif( key == "rarity"):
                mention_dict[key][values] = round(mention_dict[key][values] / rarity_mention,2)
            elif( key == "pinkie"):
                mention_dict[key][values] = round(mention_dict[key][values] / pinkie_mention,2)
            elif( key == "rainbow"):
                mention_dict[key][values] = round(mention_dict[key][values] / rainbow_mention,2)
            else:
                mention_dict[key][values] = round(mention_dict[key][values] / fluttershy_mention,2)
    
    return mention_dict