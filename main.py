alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
 
def caesar(input_text, shift_num, mode):
  text_string = ''
  for letter in input_text:
      letter_place=alphabet.index(letter) 
      if mode == "decode":
        shift_num *= -1
      letter_index = letter_place + shift_num
      text_string +=alphabet[letter_index]
  print(f" The {mode} text is: {text_string}")
    
caesar(input_text=text, shift_num=shift, mode=direction)
