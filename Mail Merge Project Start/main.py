#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#changing the names from the text file in to a list using the .split(",") method

with open("./Input/Names/invited_names.txt", mode="r") as names:
    list_names = names.read().strip().split()

#Replace the [name] placeholder with the actual name.

for name in list_names:
    with open("./Input/Letters/starting_letter.txt", mode="r") as letter:
        letter_ide = letter.read().replace("[name]", f"{name}")
        with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as complete_letter:
            complete_letter.write(letter_ide)


#Save the letters in the folder "ReadyToSend".

    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp