# Playfair Cipher Code
[Code](https://github.com/EPHS-CyberSecurity-2020-Hour3/CipherProject/blob/playfair_cipher/playfairEncryption.py)
```javascript

plainText  = input("Enter a message to encrypt: ").upper()
cyphertext = ""
key = "toughkey".upper()
grid = [["T","O","U","G","H"],["K","E","Y","A","B"],["C","D","F","I","L"],["M","N","P","Q","R"],["S","V","W","X","Z"]]
line = ""
for row in grid:
    for tempLetter in row:
        line = line + tempLetter + " "
    print(line)
    line = ""

cipherText = ""
pair = ""
finalLetter = ""
index = 0
pairsArray = []
letterCords = []
encryptedPairs = []
encryptedCords = []
for letter in plainText:
    if index%2 == 1:
        pair = plainText[index-1] + letter
        pairsArray.append(pair)
    #print(pair)
    pair = ""
    index+=1
if len(plainText)%2 == 1:
            finalLetter = letter
            #print(letter)
print(f'Plaintext sorted into pairs: {pairsArray}')
down = 0
across = 0
for pair in pairsArray:
    for letter in pair:
        for row in grid:
            for key in row:
                if key == letter:
                    print(f'Letter {letter}: {down} down, {across} across')
                    letterCords.append([down,across])
                across+=1
            down+=1
            across = 0
        down = 0
firstDownCord = 0
firstAcrossCord = 0
secondAcrossCord = 0
secondDownCord = 0
cordIndex = 0
tempVar = ""
for cord in range(0,int(len(letterCords)/2)):
    if cordIndex == len(letterCords)-1:
        continue
    
    firstDownCord = letterCords[cordIndex][0]
    firstAcrossCord = letterCords[cordIndex][1]
    secondAcrossCord = letterCords[cordIndex+1][1]
    secondDownCord = letterCords[cordIndex+1][0]
    if firstAcrossCord == secondAcrossCord:
       firstDownCord = (firstDownCord+1)%5
       secondDownCord = (secondDownCord+1)%5
    elif firstDownCord == secondDownCord:
       firstAcrossCord = (firstAcrossCord+1)%5
       secondAcrossCord = (secondAcrossCord+1)%5
    else:
        tempVar = firstAcrossCord
        firstAcrossCord = secondAcrossCord
        secondAcrossCord = tempVar
    #encryptedCords.append(cordIndex)
    encryptedCords.append([firstDownCord, firstAcrossCord])
    encryptedCords.append([secondDownCord, secondAcrossCord])
    
    cordIndex+=2
for finalPairs in encryptedCords:
    encryptedPairs.append(grid[finalPairs[0]][finalPairs[1]])
letterIndex = 0
for letter in encryptedPairs:
    if letterIndex%2 == 1:
        cipherText = cipherText+letter
    else:
        cipherText = cipherText+" "+letter
    letterIndex += 1

print(letterCords)
print (encryptedCords)
print(encryptedPairs)
print(plainText)
print(cipherText+" "+finalLetter)
```
[Website](https://planetcalc.com/7751/)
