import pandas as pd
import json
import re

def non_dictionary_words(df):
    with open('../data/words_alpha.txt') as file:
        dictionary_set = set(word.strip().lower() for word in file)

    # c = pd.read_csv("words_alpha.txt", sep="\n")

    twilight_sparkle_df = df.loc[(df['pony'] == 'Twilight Sparkle')]
    twilight_list = twilight_sparkle_df.dialog.tolist()

    dict_for_occurence_twilight= {}
    for i in range(len(twilight_list)):
        twilight_list[i]=str(twilight_list[i])
        twilight_list[i] = re.sub(r"[^a-zA-Z\s]", " ", twilight_list[i].strip())
    #    twilight_list[i] = twilight_list[i].split()
        array = twilight_list[i].split()
        for j in range(len(array)):
            if (array[j].lower() in dict_for_occurence_twilight):
                dict_for_occurence_twilight[array[j].lower()] +=1
            else:
                dict_for_occurence_twilight[array[j].lower()] =1

    twilight_not_in_alpha = []       
    for i in dict_for_occurence_twilight:
        if (i not in dictionary_set):
            twilight_not_in_alpha.append(i)   

    twilight_final_dict = {}
    for i in range(len(twilight_not_in_alpha)):
        twilight_final_dict[twilight_not_in_alpha[i]] = dict_for_occurence_twilight[twilight_not_in_alpha[i]]

    twilight_orders = sorted(twilight_final_dict.items(), key=lambda x: x[1], reverse=True)

    twilight_non = []
    for i in twilight_orders[0:5]:
        twilight_non .append(i[0])

    ###apple jack
    applejack_df = df.loc[(df['pony'] == 'Applejack')]
    applejack_list = applejack_df.dialog.tolist()

    dict_for_applejack= {}
    for i in range(len(applejack_list)):
        applejack_list[i]=str(applejack_list[i])
        applejack_list[i] = re.sub(r"[^a-zA-Z\s]", " ", applejack_list[i].strip())
    #    applejack_list[i] = applejack_list[i].split()
        array = applejack_list[i].split()
        for j in range(len(array)):
            if (array[j].lower() in dict_for_applejack):
                dict_for_applejack[array[j].lower()] +=1
            else:
                dict_for_applejack[array[j].lower()] =1

    apple_jack_not_in_alpha = []       
    for i in dict_for_applejack:
        if (i not in dictionary_set):
            apple_jack_not_in_alpha.append(i)   

    final_apple_jack = {}
    for i in range(len(apple_jack_not_in_alpha)):
        final_apple_jack[apple_jack_not_in_alpha[i]] = dict_for_applejack[apple_jack_not_in_alpha[i]]

    apple_orders = sorted(final_apple_jack.items(), key=lambda x: x[1], reverse=True)

    apple_jack_non= []
    for i in apple_orders[0:5]:
        apple_jack_non.append(i[0])

    ##rarity non alpha words

    rarity_df = df.loc[(df['pony'] == 'Rarity')]
    rarity_list = rarity_df.dialog.tolist()

    rarit_dict= {}
    for i in range(len(rarity_list)):
        rarity_list[i]=str(rarity_list[i])
        rarity_list[i] = re.sub(r"[^a-zA-Z\s]", " ", rarity_list[i].strip())
    #    rarity_list[i] = rarity_list[i].split()
        array = rarity_list[i].split()
        for j in range(len(array)):
            if (array[j].lower() in rarit_dict):
                rarit_dict[array[j].lower()] +=1
            else:
                rarit_dict[array[j].lower()] =1

    rarity_not_in_alpha = []       
    for i in rarit_dict:
        if (i not in dictionary_set):
            rarity_not_in_alpha.append(i)   

    rarity_final= {}
    for i in range(len(rarity_not_in_alpha)):
        rarity_final[rarity_not_in_alpha[i]] = rarit_dict[rarity_not_in_alpha[i]]

    rarity_orders = sorted(rarity_final.items(), key=lambda x: x[1], reverse=True)

    rarity_non = []
    for i in rarity_orders[0:5]:
        rarity_non.append(i[0])

    ##fluttershy

    fluttershy_df = df.loc[(df['pony'] == 'Fluttershy')]
    fluttershy_list = fluttershy_df.dialog.tolist()

    fluttershy_dict= {}
    for i in range(len(fluttershy_list)):
        fluttershy_list[i]=str(fluttershy_list[i])
        fluttershy_list[i] = re.sub(r"[^a-zA-Z\s]", " ", fluttershy_list[i].strip())
    #    fluttershy_list[i] = fluttershy_list[i].split()
        array = fluttershy_list[i].split()
        for j in range(len(array)):
            if (array[j].lower() in fluttershy_dict):
                fluttershy_dict[array[j].lower()] +=1
            else:
                fluttershy_dict[array[j].lower()] =1

    fluttershy_not_in_alpha = []       
    for i in fluttershy_dict:
        if (i not in dictionary_set):
            fluttershy_not_in_alpha.append(i)   

    final_fluttershy = {}
    for i in range(len(fluttershy_not_in_alpha)):
        final_fluttershy[fluttershy_not_in_alpha[i]] = fluttershy_dict[fluttershy_not_in_alpha[i]]

    fluttershy_orders = sorted(final_fluttershy.items(), key=lambda z: z[1], reverse=True)

    fluttershy_non = []
    for i in fluttershy_orders[0:5]:
        fluttershy_non.append(i[0])


    ##pinkie pie

    pinkie_pie_df = df.loc[(df['pony'] == 'Pinkie Pie')]
    pinkipie_list = pinkie_pie_df.dialog.tolist()

    pinkiepie_dict= {}
    for i in range(len(pinkipie_list)):
        pinkipie_list[i]=str(pinkipie_list[i])
        pinkipie_list[i] = re.sub(r"[^a-zA-Z\s]", " ", pinkipie_list[i].strip())
    #    pinkipie_list[i] = pinkipie_list[i].split()
        array = pinkipie_list[i].split()
        for j in range(len(array)):
            if (array[j].lower() in pinkiepie_dict):
                pinkiepie_dict[array[j].lower()] +=1
            else:
                pinkiepie_dict[array[j].lower()] =1

    pinkipie_not_alpha = []       
    for i in pinkiepie_dict:
        if (i not in dictionary_set):
            pinkipie_not_alpha.append(i)   

    pinkie_final = {}
    for i in range(len(pinkipie_not_alpha)):
        pinkie_final[pinkipie_not_alpha[i]] = pinkiepie_dict[pinkipie_not_alpha[i]]

    pinkie_orders = sorted(pinkie_final.items(), key=lambda z: z[1], reverse=True)

    pinkie_pie_non = []
    for i in pinkie_orders[0:5]:
        pinkie_pie_non.append(i[0])

    ##Rainbow dash
    rainbow_dash_df = df.loc[(df['pony'] == 'Rainbow Dash')]
    rainbow_list = rainbow_dash_df.dialog.tolist()

    rainbow_dict= {}
    for i in range(len(rainbow_list)):
        rainbow_list[i]=str(rainbow_list[i])
        rainbow_list[i] = re.sub(r"[^a-zA-Z\s]", " ", rainbow_list[i].strip())
    #    rainbow_list[i] = rainbow_list[i].split()
        array = rainbow_list[i].split()
        for j in range(len(array)):
            if (array[j].lower() in rainbow_dict):
                rainbow_dict[array[j].lower()] +=1
            else:
                rainbow_dict[array[j].lower()] =1

    rainbow_no_alpha = []       
    for i in rainbow_dict:
        if (i not in dictionary_set):
            rainbow_no_alpha.append(i)   

    rainbow_final = {}
    for i in range(len(rainbow_no_alpha)):
        rainbow_final[rainbow_no_alpha[i]] = rainbow_dict[rainbow_no_alpha[i]]

    rainbow_orders = sorted(rainbow_final.items(), key=lambda z: z[1], reverse=True)

    rainbow_dash_non = []
    for i in rainbow_orders[0:5]:
        rainbow_dash_non.append(i[0]) 


    ##dictionary of non-alpha
    new_non_dict = {"twilight":twilight_non, "applejack":apple_jack_non, "pinkie": pinkie_pie_non, "rarity": rarity_non, "fluttershy": fluttershy_non, "rainbow": rainbow_dash_non}

    return new_non_dict