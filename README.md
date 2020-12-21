# CipherProject

# CipherProject


#### Historical context
  When was this cipher used? Who used it?
  The Atbash Cipher goes all the way back to 500 BC, during the age of the Knights Templar, who used it until their downfall in 1300 AD.
#### Mechanics
  How does the cipher work?
  The Atbash Cipher is a 
  Demo an encryption and decryption
  Is it symmetric, does the same process decrypt as encrypt?
#### Mathematical Analysis
  How many possible keys or codes could there be?
  How would you attempt to decode this message if you didn't have a key.
  What is the mathematical complexity to solve the code?
#### Computer code
  Find a website or program that will encode using this technique
  Demo how it works.
  Is there any easy "decode" available?
  #Atbash Cipher
#Cipher must alter plaintext into its opposite letter in the alphabet

from tkinter import *
import sys
import pyperclip

root = Tk()
root.title("Atbash Cipher")

Inputframe = Frame(root, width = 500, height = 100)
Inputframe.pack(side = BOTTOM)

#frame = Frame(root, width = 100, height = 10, bd = 5)
#frame.pack()

ChatFrame = Frame(root, width = 100, height = 1000)
ChatFrame.pack(side = TOP)

ChatLabel = Label(ChatFrame, text="Welcome to the Atbash Cipher!")
ChatLabel.pack()

textInput = Entry(Inputframe, width = 75, bd = 5)
textInput.pack(side = RIGHT)

run = 1

while run == 1:
    SYMBOLS = "abcdefghijklmnopqrstuvwxyz"
    CIPHER =  "zyxwvutsrqponmlkjihgfedcba"
    mode = input("Would you like to encrypt or decrypt a message? ")
    plaintext = input("Enter your message: ")
    plaintext = plaintext.lower()
    message = ""
    for symbol in plaintext:
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)


            if mode == "encrypt":
                message += CIPHER[symbolIndex]
    
            elif mode == "decrypt":
                message += SYMBOL[symbolIndex]
            else:
                sys.exit("You Stupid!")
    pyperclip.copy(message)         
    print("Your new message is " + message)
    answer = input("would you like to run the program again? (yes/no)")
    if answer == "yes":
        pass
    elif answer == "no":
        run = 0
    else:
        print("bruh you really stupid. k i guess i'll shut it off dummy")
        run = 0

    
#### Final analysis
  Why did this stop being a useful code?
  What made it useful when it was being used?
  What are other interesting uses of this code or similar codes?

Your final presentation should be given to the class as a github repo with visuals and supporting information. This is a big assignment so be prepared to answer questions and give a complete picture of the cipher, it's use, and historical context.

### Possible Ciphers:
- Caesar Cipher
- Transposition Cipher
- Substitution Cipher
- Multiplicative Cipher
- Affine Cipher
- Vigenere Cipher
- One-Time Pad
- Polybius Square
- Four Square Cipher
- Rail fence cipher
- Atbash Cipher
- Scytale Cipher
- Bacon's Cipher
- Book Cipher
- Pigpen Cipher
- Playfair Cipher
- M-94 Cipher
- Nihilist Cipher
- Hill Cipher
