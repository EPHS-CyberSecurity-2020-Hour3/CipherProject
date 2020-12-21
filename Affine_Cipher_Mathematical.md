How many possible keys or codes could there be? How would you attempt to decode this message if you didn't have a key. What is the mathematical complexity to solve the code?

1. 312 possible keys
2.For example, here’s how you’d do it for an English message. Count up the frequencies of all the letters. The most frequent letter should show up a little over 10% of the time. That letter probably stands for E. The second most frequent letter probably stands for T. Once you have two letters, you can use a system of linear equations (mod 26) to solve for the key.

The Cypher is Created by making number letters

So A is 0 and B is 1 and so on until Z is 25

Example 

encryption of the plaintext “sail” using an affine cipher with encryption key (3,7)
produces ciphertext “JHFO” this way:

s −→ 18 −→ 3 · 18 + 7 ≡ 9 (mod 26) −→ J

a −→ 0 −→ 3 · 0 + 7 ≡ 7 (mod 26) −→ H

i −→ 8 −→ 3 · 8 + 7 ≡ 5 (mod 26) −→ F

l −→ 11 −→ 3 · 11 + 7 ≡ 14 (mod 26) −→ O
