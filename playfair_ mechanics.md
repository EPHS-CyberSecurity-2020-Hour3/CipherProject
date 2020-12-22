# Playfair Cipher Mechanics
The playfair cipher consists of a 5 by 5 grid which you use to encrypt your message
</br>
Things need to create a encrypted message...
* A key (a combination of letters)
* A 5x5 grid that is created by using the key
* Sort your plain text into groups of pairs while sets of 2 letters
  * Example: "Hide the gold in the tree stump" -> **"HI DE TH EG OL DI NT HE TR EX ES TU MP"**
  * It is "EX" because it splits up the EE
* Configure the grid with the key
  * In this case we will be using **"playfair example"** as the key
  * The grid is show below
</br>

![Example Grid](https://upload.wikimedia.org/wikipedia/commons/e/ef/Playfair_Cipher_building_grid_omitted_letters.png)

* Now that the grid is created, you need to take the pairs of plaintext to encrypt into corresponding cyphertext
  * The first pair that we need to encrypt is "HI"
  > HI forms a rectangle therefore we replace it with BM
  ![Encrypt HI](https://upload.wikimedia.org/wikipedia/commons/4/40/Playfair_Cipher_01_HI_to_BM.png)
  * Next we need to do "DE"
  > The pair DE is in a column, replace it with OD           
  ![Encrypt "DE"](https://upload.wikimedia.org/wikipedia/commons/4/44/Playfair_Cipher_02_DE_to_OD.png)
  * The next pair is "TH"
  > Similar to HI, pair TH forms a rectangle. Therefore, replace it with ZB
  ![Encrypt "HI"](https://upload.wikimedia.org/wikipedia/commons/1/1b/Playfair_Cipher_03_TH_to_ZB.png)
  * The next pair is "EG"
  > The pair EG forms another rectangle, so replace it with XD
  ![Encrypt EG](https://upload.wikimedia.org/wikipedia/commons/f/fb/Playfair_Cipher_04_EG_to_XD.png)
  * "OL" is up next
  > The pair OL forms a rectangle, replace it with NA
  ![Encrypt OL](https://upload.wikimedia.org/wikipedia/commons/7/79/Playfair_Cipher_05_OL_to_NA.png)
  * Follow this same process until EX
  > The pair EX (X inserted to split EE) is in a row, replace it with XM	
  ![Encrypt EX](https://upload.wikimedia.org/wikipedia/commons/2/29/Playfair_Cipher_10_EX_to_XD.png)
 * You now know the basic steps so you can follow this same proccess until you finish the entire cipher.
 </br>
After following these steps you get "BM OD ZB XD NA BE KU DM UI XM MO UV IF" as your encrpyted message!
</br>
The decryption process would be the same as the encryption expect opposite and you would be required to know the correct key
</br>
[Math](https://github.com/EPHS-CyberSecurity-2020-Hour3/CipherProject/blob/playfair_cipher/playfair_mathmatics.md)
