# Code
Find a website or program that will encode using this technique Demo how it works. Is there any easy "decode" available? #Atbash Cipher #Cipher must alter plaintext into its opposite letter in the alphabet

from tkinter import * import sys import pyperclip

root = Tk() root.title("Atbash Cipher")

Inputframe = Frame(root, width = 500, height = 100) Inputframe.pack(side = BOTTOM)

#frame = Frame(root, width = 100, height = 10, bd = 5) #frame.pack()

ChatFrame = Frame(root, width = 100, height = 1000) ChatFrame.pack(side = TOP)

ChatLabel = Label(ChatFrame, text="Welcome to the Atbash Cipher!") ChatLabel.pack()

textInput = Entry(Inputframe, width = 75, bd = 5) textInput.pack(side = RIGHT)

run = 1

while run == 1: SYMBOLS = "abcdefghijklmnopqrstuvwxyz" CIPHER = "zyxwvutsrqponmlkjihgfedcba" mode = input("Would you like to encrypt or decrypt a message? ") plaintext = input("Enter your message: ") plaintext = plaintext.lower() message = "" for symbol in plaintext: if symbol in SYMBOLS: symbolIndex = SYMBOLS.find(symbol)
