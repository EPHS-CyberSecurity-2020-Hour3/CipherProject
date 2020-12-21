How many possible keys or codes could there be? How would you attempt to decode this message if you didn't have a key. What is the mathematical complexity to solve the code?

1. 312 possible keys
2.For example, here’s how you’d do it for an English message. Count up the frequencies of all the letters. The most frequent letter should show up a little over 10% of the time. That letter probably stands for E. The second most frequent letter probably stands for T. Once you have two letters, you can use a system of linear equations (mod 26) to solve for the key.
