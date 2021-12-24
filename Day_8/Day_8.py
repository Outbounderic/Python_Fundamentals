import collections
from logo import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

cypher_alphabet = collections.deque(alphabet)

def caesar(current_direction, plain_text, shift_amount):
    modified_text = []

    if current_direction == "encode":
        cypher_alphabet.rotate(-shift_amount)
    elif current_direction == "decode":
        cypher_alphabet.rotate(shift_amount)

    for letter in plain_text:
        for key in alphabet:
            if letter == key:
                altered_letter = alphabet.index(letter)
                modified_text.append(cypher_alphabet[altered_letter])
                
    print(f"The {current_direction}d text is {''.join(modified_text)}")

caesar(direction, text, shift)