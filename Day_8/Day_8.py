import collections

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

cypher_alphabet = collections.deque(alphabet)

def encrypt(plain_text, shift_amount):
    cypher_alphabet.rotate(-shift_amount)
    encrypted_text = []
    for letter in plain_text:
        for key in alphabet:
            if letter == key:
                altered_letter = alphabet.index(letter)
                encrypted_text.append(cypher_alphabet[altered_letter])
                
    print(f"The encoded text is {''.join(encrypted_text)}")

  #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  
  #e.g. 
  #cipher_text = "mjqqt"
  #shift = 5
  #plain_text = "hello"
  #print output: "The decoded text is hello"


#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.

def decrypt(plain_text, shift_amount):
    cypher_alphabet.rotate(-shift_amount)
    decrypted_text = []
    for letter in plain_text:
        for key in alphabet:
            if letter == key:
                altered_letter = alphabet.index(letter)
                decrypted_text.append(cypher_alphabet[altered_letter])
                
    print(f"The decoded text is {''.join(decrypted_text)}")
