plainText  = "thisisamessage".upper()

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
secondAcrossCard = 0
secondDownCard = 0
cordIndex = 0
for cord in letterCords:
    if cordIndex == len(letterCords)-1:
        continue
    if cordIndex%2 == 1:
        pass
    firstdownCord = cord[0]
    firstacrossCord = cord[1]
    secondAcrossCard = letterCords[cordIndex+1][0]
    secondDownCard = letterCords[cordIndex+1][1]
    if firstAcrossCord == secondAcrossCard:
        firstDownCord = (firstDownCord+1)%4
        secondDownCard = (secondDownCard+1)%4
    
    encryptedCords.append([firstDownCord, firstAcrossCord])
    encryptedCords.append([secondDownCard, secondAcrossCard])
    cordIndex+=1


print(letterCords)
print (encryptedCords)