#2022/10/11
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
from logo import logo

def casear(type_casear, shift_text, shift_amount):
    cipher_text = ""
    if type_casear == "decode" :
        shift_amount *= -1
    
    for i in shift_text :
        if i in alphabet :
            position = alphabet.index(i)
            new_position = position + shift_amount
            if new_position > len(alphabet) -1 :
                new_position = new_position % len(alphabet)
            cipher_text += alphabet[new_position]
        else:
            cipher_text += i
    
    print(f"{shift_text} is {type_casear}d : {cipher_text}")

print(logo)

on_off = True
while(on_off):
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    casear(direction, text, shift)

    on_off = input("Type 'yes' if you want to go again. Otherwise type 'no'. \n")
    
    if on_off == 'no' :
        on_off = False
        print("Goodbye")
