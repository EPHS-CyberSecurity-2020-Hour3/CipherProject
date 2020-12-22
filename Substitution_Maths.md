# Math
> *The number of keys possible with the substitution cipher is much higher, around 2^88 possible keys. This means we cannot test them all, we have to 'search' for good keys. We will be using a 'hill-climbing' algorithm to find the correct key.*
> The steps are: 
1. Generate a random key, called the 'parent', decipher the ciphertext using this key. 
2. Rate the fitness of the deciphered text, store the result.
3. Change the key slightly (swap two characters in the key at random), measure the fitness of the deciphered text using the new key.
4. If the fitness is higher with the modified key, discard our old parent and store the modified key as the new parent.
5. Go back to 2, unless no improvement in fitness occurred in the last 1000 iterations.
