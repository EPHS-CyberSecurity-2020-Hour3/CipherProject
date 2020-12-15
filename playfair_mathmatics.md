# Playfair Cipher Mathematic Analysis
Because this cipher uses a 5x5 grid it take much more cipher text to be able to use frequency analysis
> 25*25=625 possible alphebets to look through rather than the 25 possible single letter alphebets
Also the data ends up being more secure becaue it is encrypted in pairs
* Another way to decrypt the data could be to look for common words that would be in the message
* For example, if it was a message to Joe. The hacker could look for the term Dear Joe in the letter. This starts to reveal more of the cipher text and could help you resolve the message. [Example](https://perseengage.files.wordpress.com/2014/05/playfaircipher-prataps1.pdf)
</br>
If I were to try and break the code knowing about the mathematic analysis behind the cipher, I would try brute force common terms that could possibly be inside the code. If I get any matches, I would slowly uncover common terms and use advanced frequency analysis to reveal the key used. Another important thing to note would be to try and find different cribs that reoccur within the ciper text and use the distance between them to try and uncover the length of the key used.
[Source](http://practicalcryptography.com/ciphers/playfair-cipher/)