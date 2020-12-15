# Playfair Cipher Mechanics
The playfair cipher consists of a 5 by 5 grid which you use to encrypt your message
</br>
Things need to create a encrypted message...
* A key (a combination of letters)
* A 5x5 grid that is created by using the key
* Sort your plain text into groups of pairs while sets of 2 letters
  * Example: "Hide the gold in the tree stump" -> "HI DE TH EG OL DI NT HE TR EX ES TU MP"
* Configure the grid with the key
  * In this case we will be using "playfair example" as the key
  * The grid is show below
</br>

![Example Grid](https://upload.wikimedia.org/wikipedia/commons/e/ef/Playfair_Cipher_building_grid_omitted_letters.png)

* Now that the grid is created, you need to take the pairs of plaintext to encrypt into corresponding cyphertext
  * The first pair that we need to encrypt is "HI"
  > HI forms a rectangle therefore we replace it with BM
  ![Encrypt HI](https://upload.wikimedia.org/wikipedia/commons/4/40/Playfair_Cipher_01_HI_to_BM.png)