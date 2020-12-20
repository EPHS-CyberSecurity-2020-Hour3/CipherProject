# Computer Code

This site will encode your message to bacons cipher 
https://cryptii.com/pipes/bacon-cipher

There is a pretty easy way to decode it just by switching the A's and B's to 0's and 1's and then counting in binary every 5 numbers with 23 being Z and 0 being A


# Python Code 
'''

from textwrap import wrap

def ence():

  message= input("Whats your un-ecrypted message?\n")

  message = message.upper()

  bacon = ["AAAAA","AAAAB","AAABA","AAABB","AABAA","AABAB","AABBA","AABBB","ABAAA","ABAAA","ABAAB","ABABA","ABABB","ABBAA","ABBAB","ABBBA","ABBBB","BAAAA","BAAAB","BAABA","BAABB","BAABB","BABAA","BABAB","BABBA","BABBB"]
  alf = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

  enc = ""

  for letter in message:

    b = 0

    for i in alf:

      if (letter == i):

        enc+= bacon[b]

      b+=1

  print(enc)      

def dence():


  message= input("Whats your ecrypted message?\n")

  if(len(message) % 5 != 0):

    print("Invalid Message!")
    
    dence()


  message = message.upper()

  bacon = ["AAAAA","AAAAB","AAABA","AAABB","AABAA","AABAB","AABBA","AABBB","ABAAA","ABAAA","ABAAB","ABABA","ABABB","ABBAA","ABBAB","ABBBA","ABBBB","BAAAA","BAAAB","BAABA","BAABB","BAABB","BABAA","BABAB","BABBA","BABBB"]
  alf = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

  denc = ""

  split = wrap(message, 5)

  for i in split:

    b = 0

    for k in bacon:

      if i == k:

        denc+= alf[b]

      b+=1  

  print(denc)    


ans = input("Do you wanna decrypt or encrypt?(D/E)\n")

ans = ans.upper()

if ans == "E": 

  ence()

elif ans == "D":

  dence()

'''



 
 
