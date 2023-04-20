#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open('day-24-start/Mail Merge Project Start/Input/Letters/starting_letter.txt', mode='r') as letter :
    content_letter = letter.read()
with open('day-24-start/Mail Merge Project Start/Input/Names/invited_names.txt', mode='r') as dear :
    list_dear = dear.readlines()

for dear in list_dear:
    dear = dear.strip()
    dear_letter = content_letter.replace('[name]', dear)
    with open(f'day-24-start/Mail Merge Project Start/Output/ReadyToSend/{dear}.txt', mode='w') as file:
        file.write(dear_letter)
