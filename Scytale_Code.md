# Scytale python implementation


```
# scytale.py
# 12-15-20
# Andy Killorin & Amar Dani
# Encyrypts and decrypts scytale messages given a key.

def encrypt(msg, key):
    if key > len(msg):
        return msg
    eMsg = ""
    for i in range(key):
        eMsg += msg[i::key]
    return eMsg

def decrypt(msg, key):
    pass

def main():
    if input("encrypt or decrypt? (e,d) [e]\n> ") == 'd':
        message = input("message to decrypt\n> ")
        key = int(input("encryption key\n> "))
        print(decrypt(message,key))
    else:
        message = input("message to encrypt\n> ")
        key = int(input("encryption key\n> "))
        print(encrypt(message,key))

if __name__ == '__main__':
    main()
```

[Analysis](Scytale_FinalAnalysis.md)
