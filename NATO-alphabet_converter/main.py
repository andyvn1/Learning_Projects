import pandas

#Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
phonetic_alphabet_csv = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_alphabet_dic = {row.letter: row.code for (index, row) in phonetic_alphabet_csv.iterrows()}

#Create a list of the phonetic code words from a word that the user inputs.
pass_exception = False
while not pass_exception:
    answer = input("Enter the word you want to convert.\n--").upper()
    try:
        phonetic_list = [phonetic_alphabet_dic[letter] for letter in answer]
    except KeyError:
        print("Sorry, only letters in the alphabet please")
    else:
        print(phonetic_list)
        pass_exception = True
