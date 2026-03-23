# Caesar Cipher Encoder
# Encodes a user entered string by shifting each letter by a fixed number of positions.
# Preserves original case and non-alphabetic characters (spaces, numbers, punctuation).
# Prompts the user again if input is empty or whitespace only.

def enter_string():
    while True:
        input_string=input("Enter a string to encode: ")
        if input_string.strip():
            return input_string
        print("Input cannot be empty. Please enter a valid string.")
           

def encode_string(input_string, shift=2):
    alphabet="abcdefghijklmnopqrstuvwxyz"
    alpha_list=list(alphabet)
    encoded_string = ""

    for char in input_string:        
         if char.lower() in alpha_list:
             index=alpha_list.index(char.lower())
             encoded_char=alpha_list[(index+shift) %26]
             if char.isupper():
                encoded_char = encoded_char.upper()
             encoded_string+=encoded_char
         else:
             encoded_string+=char
    return encoded_string

if __name__=="__main__":
    input_string=enter_string()
    encoded_string=encode_string(input_string)
    print("Encoded String:",encoded_string)