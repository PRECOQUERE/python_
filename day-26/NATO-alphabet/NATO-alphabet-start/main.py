student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
import pandas
data = pandas.read_csv('day-26/NATO-alphabet/NATO-alphabet-start/nato_phonetic_alphabet.csv')
word_dic = {row.letter:row.code for (inx, row) in data.iterrows()}
# print(word_dic)
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
usr_word = input("Enter a word: ").upper()
usr_init = [word_dic[init] for init in usr_word]
print(usr_init)
