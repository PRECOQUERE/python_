#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

file_dear = open('day-24-start/Mail Merge Project Start/Input/Names/invited_names.txt')
list_dear = file_dear.readlines()
file_letter = open('day-24-start/Mail Merge Project Start/Input/Letters/starting_letter.txt')
letter = file_letter.read()

for dear in list_dear:
    dear = dear.strip()
    dear_letter = letter.replace('[name]', dear)
    with open(f"day-24-start/Mail Merge Project Start/Output/{dear}.txt", mode='w') as file:
        file.write(dear_letter)

file_dear.close()
file_letter.close()
