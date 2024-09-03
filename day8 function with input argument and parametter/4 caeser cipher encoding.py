#caesar cipher encoder (shifting alphabet by certain  position)

#old list have problem for zulu
#alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
#             't', 'u', 'v', 'w', 'x', 'y', 'z']

#new list to solve the "zulu's problem"
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
             't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
             't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text, shift_amount):
    cipher_text=""
    for letter in plain_text:
        position=alphabet.index(letter)#to find position of that looped letter from "plan_text" in list "alphabet" we use index()
        new_position= position + shift_amount

        new_letter= alphabet[new_position]#new letter is alphabet at new_position

        cipher_text += new_letter

    print(f"Encrypted message is {cipher_text}")
#if we use plain_text as "zulu" result in list index out of range because for eg. there is nothing after shifting 'z' by 5
# to solve this problem we use new "alphabet list " we use alphabet 2 times in list

def decrypt(cipher_text, shift_amount):
    plane_text=""
    for letter in cipher_text:
        position=alphabet.index(letter)#to find position of that looped letter from "plan_text" in list "alphabet" we use index()
        new_position= position - shift_amount

        new_letter= alphabet[new_position]#new letter is alphabet at new_position

        plane_text += new_letter

    print(f"Decrypted message is {plane_text}")

if direction == "encode":
    encrypt(plain_text=text, shift_amount=shift)
elif direction == "decode":
    decrypt(cipher_text=text, shift_amount=shift)