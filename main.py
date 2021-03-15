from art import logo
from replit import clear
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']                                                                                                        
def caesar(input_text, shift_num, mode):
  text_string = ''
  if mode == "decode":
    shift_num *= -1
  for letter in input_text:
    if letter.isalpha():
      letter_place=alphabet.index(letter) 
      letter_index = letter_place + shift_num
      text_string +=alphabet[letter_index]
    else:
      text_string +=letter
  print(f"The {mode} text is: {text_string}")
 

are_you_done = False
while not are_you_done:
  are_you_done = False
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  if shift > 26:
    shift = shift % 26  

  caesar(input_text=text, shift_num=shift, mode=direction)

  done = input( "Are you done? yes or no \n").lower()
  if done == "yes":
      are_you_done= True
      print("Thanks for using my app" )
      

