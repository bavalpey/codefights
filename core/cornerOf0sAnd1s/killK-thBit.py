"""
In order to stop the Mad Coder evil genius you need to decipher the encrypted message he sent to his minions.
The message contains several numbers that, when typed into a supercomputer, will launch a missile into the
sky blocking out the sun, and making all the people on Earth grumpy and sad.

You figured out that some numbers have a modified single digit in their binary representation. More specifically,
in the given number n the kth bit from the right was initially set to 0, but its current value might be different.
It's now up to you to write a function that will change the kth bit of n back to 0.

Example

For n = 37 and k = 3, the output should be
killKthBit(n, k) = 33.

3710 = 1001012 ~> 1000012 = 3310.

For n = 37 and k = 4, the output should be
killKthBit(n, k) = 37.

The 4th bit is 0 already (looks like the Mad Coder forgot to encrypt this number), so the answer is still 37.
"""
def killKthBit(n, k):
    return int(bin((n ^ (1 << k-1)) & n),2)
