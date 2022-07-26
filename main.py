import pandas
# with open("morse_code.csv",'w') as file:
data= pandas.read_csv("morse_code.csv")

#TODO 1. Create a dictionary in this format:
morse_dict = {row.letter: row.code for (index, row) in data.iterrows()}
# print(phonetic_dict)

#TODO 2. Create a list of the morse code words from a word that the user inputs.
code = True
def generate_code():
    word = input("Enter a word: ").upper()

    try:
        output_list = [morse_dict[letter] for letter in word]
    except KeyError:
        print("Sorry only letters in the alphabet please")
        generate_code()
    else:
        print(output_list)



generate_code()