# Week 4 report

This week I looked thoroughly into modular arithmetic since it was all new to me. It helped to think of it like a clock, for example 2 and 14 are equivalent under mod 12. I finished coding the Miller-Rabin algorithm and did a bunch of hand calculations along with debugging to really understand how it works. From the pseudocode concepts like "nontrivial square root of 1 modulo n" were quite obscure to me, but I have since learned that if for example *a* is a nontrivial square root of *n*, that is equivalent to *a*²-1 = *k\*n*, or (*a*+1)(*a*-1) = *k\*n* for some whole number *k*, meaning that *n* shares a factor with (*a*+1) or (*a*-1) and is therefore composite.

I learned that 65537 is safe to use as a public exponent in RSA and it's in fact common practice to do so. From what I understood, it has a handful of properties that make it a good compromise between security and performance, since raising to the power of a larger value would slow calculations.

I also implemented a modular multiplicative inverse function to find the private exponent. I found out that it can be done recursively or iteratively, so I opted for iterative since it's generally faster.

I also implemented very simple key generation and managed to get encryption and decryption working with it (although it's still a bit buggy). Currently my code generates keys as strings where the modulus and exponent are joined with "-". They are also very short in bit length for debugging purposes. This is not the indended final outcome, the next thing to do is to research RSA key formats, generate real >2000-bit keys and test that the code works with large keys as well. I plan to get the project more or less done next week so that there will still be time to clean up the code and tests.

I noticed that the efficiency of my code could probably be improved, since generating two 1024-bit primes had a noticeable delay. My code had a few bugs that I discussed with the course instructors and I believe I managed to mostly fix them, so I'm looking forward to receiving feedback on the current state of my code.

Time spent: 16 hours
