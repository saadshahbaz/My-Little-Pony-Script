import json

def jsonconverter(dictt, inputfile):
    final_json = json.dumps(dictt)

    if (inputfile == "stdout"):
        print(final_json)
    else:
        outfile = open(inputfile, "w+")
        outfile.write(json.dumps(dictt))