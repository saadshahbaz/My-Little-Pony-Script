# My-Little-Pony-Script

# The goal of this Project is to develop python scripts and code to conduct a complete a data analysis project on a show called My Little Pony.

## Data <br>
[Data used for this project to analyse the scripts of the show](https://www.kaggle.com/liury123/my-little-pony-transcript) <br>
- for this project I used "clean_dialog.csv" <br>

[Data used for this project to analyse the non-dictionary words](https://github.com/dwyl/english-words) <br>
- for this project I used the "words_alpha.txt" file <br>

#### All data should be saved to the "data/" directory 



## Goal <br>
#### Collecting four main components for the project
#### - Verbosity <br>
  - An average of the number of dialogues spoken by a specific pony
#### - Mentions <br>
 - The number of times a specific pony was mentioned by other ponies

#### - Follow_on_comments <br>
- The fraction of times each pony has a line that DIRECTLY follows the others pony’s line

#### - Non_dictionary_words <br>
-  a list of the 5 non-dictionary words used most often by each Pony <br>
for example: “twilight”: [ “huh”, “ugh”, “awwww” , “wheee”, “wha”]

### - Unittests <br>
- Writing unittest spread across verbosity, mentions, follow-on-comments, and nondictionary words to confirm they give out the desired output.

## Language and Libraries used
#### - Python3 <br>
#### - JSON
#### - Pandas <br>
*to install pandas please run: `pip install pandas` in the command line*

## To run the file:
- Import all the data to the data/ directory
- Add the analysis.py file to the script directory
- Add the files test.py, follow.py, jsonfile.py, mentions.py, non_dictionary_words.py and the verbosity.py file to the src/hw3 directory
- Add the analysis_tester.py file to the src/hw3/tests directory

#### From the scripts folder run the following command on the command line
`python3 analysis.py data/clean_dialog.csv -o [optional_json_file_for_output_in_json]`

## Ending Notes
#### All Copyright of the data still belongs to the sites I imported the data from
