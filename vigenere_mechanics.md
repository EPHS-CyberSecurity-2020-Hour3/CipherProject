# Vingenere mechanics
>Vigenère uses an independent key to encrypt each character of plaintext until the end of the key is reached. Then the key is reused for the next block of plaintext characters 

## Example
> Here is how the cipher works in a more detailed example: First decide on the key which will repeat itself over and over again. Here, we are going to use COVER = COVERCOVERCOVER... Then, the letter of the cipher can be found at the intersection of the column headed by the plaintext letter and the row indexed by the key letter. To show what I mean, here is the graph:
[Vigenere](file:///var/folders/jg/nk8j95cd1810vy4cskd6c6gw0000gp/T/TemporaryItems/(A%20Document%20Being%20Saved%20By%20screencaptureui%205)/Screen%20Shot%202020-12-15%20at%2018.37.18.png)
>  To decrypt this cipher, the plaintext letter can be determined by looking at the head of the column determined by the intersection of the diagonal containing the cipher letter and the row containing the key letter.
