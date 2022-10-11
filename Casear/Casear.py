alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def casear(type_casear, shift_text, shift_amount):
    cipher_text = ""
    if type_casear == "decode" :
        shift_amount *= -1
    
    for i in shift_text :
        position = alphabet.index(i)
        new_position = position + shift_amount
        if new_position > len(alphabet) -1 :
            new_position = new_position % len(alphabet)
        cipher_text += alphabet[new_position]
    
    print(f"{shift_text} is {type_casear}d : {cipher_text}")

casear(direction, text, shift)

#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.