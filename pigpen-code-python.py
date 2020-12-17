def main():
    key = {
    "a":"_|",
    "b":"|_|",
    "c":"|_",
    "d":"]",
    "e":"[]",
    "f":"[",
    "g":"-|",
    "h":"|-|",
    "i":"|-",
    "j":"._|",
    "k":"|._|",
    "l":"|._",
    "m":".]",
    "n":"[.]",
    "o":"[.",
    "p":".-|",
    "q":"|.-|",
    "r":"|.-",
    "s":"v",
    "t":">",
    "u":"<",
    "v":"^",
    "w":".v",
    "x":".>",
    "y":".<",
    "z":".^",
    ".":"\n",
    " ":" "
}
    print("Input Message:")
    message = input()
    encr = ""
    for letter in message:
        letter = letter.lower()
        if letter in key:
            encr += key[letter] + " "
    print(encr)
main()
