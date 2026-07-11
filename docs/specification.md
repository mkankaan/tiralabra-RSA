# Requirements specification


This document details the requirements for the Algorithms and Artificial Intelligence course project at Helsinki University.

Degree programme: Bachelor of Science (Tietojenkäsittelytieteen kandidaatti)

## About the project

RSA encryption is based on a key pair with a shared modulus, a product of two prime numbers. The core problem is finding two primes that are sufficiently large so that they cannot be easily factored from their product. Several algorithms exist for finding prime numbers, notably the Miller–Rabin primality test and the Sieve of Eratosthenes, which will be implemented in this project. The difficulty of factoring large numbers is what makes RSA secure. Given the keys, encryption and decryption can be done with simple modular exponentiation.

The project is coded with Python and the documented in English.

I can peer review projects coded with Java, C, C#, Rust, Javacsript and Typescript (and in Finnish).


## Functionality

- **Key generation:** Generates a public key *(n, e)* and a private key *(n, d)* such that *n = p\*q* where *p* and *q* are distinct 2048-bit prime numbers. *e* is a prime number that is not a factor of *lcm(p-1, q-1)* (the least common multiple of *p-1* and *q-1*). Choose *d* such that *d ☰ e mod lcm(p-1, q-1)*. The resulting public and private keys have a length of 2048 bits.
- **Encryption:** Converts a plaintext message into ciphertext with the public key.
- **Decryption:** Converts ciphertext into plaintext with the private key.


## Algorithms

The following algorithms are implemented for finding large prime numbers *p* and *q* in the key generation process:
- **Sieve of Eratosthenes**

For filtering out the first few hundred small primes before passing the prime candidate to the more time-intensive Miller-Rabin
- **Miller-Rabin**

For testing the probability of a large number being prime
- **Extended Euclidean algorithm**

For the modular multiplicative inverse (finding *d* for the private key)
- **Least common multiple**

(More might be added, these were just some of the algorithms I came across in my research.)

## Time complexity

In my research I found that Miller-Rabin runs in polynomial time at worst, making it efficient.

The Sieve of Eratosthenes has a time complexity of O(n log (log n)) when finding all primes up to n. This stems from the fact that we're looping through a list of integers 2...n, and each round the amount of numbers left to be checked is divided by the next prime. The time complexity turns out to be:

n/2 + n/3 + n/5 + n/7 + ... = n(1/2 + 1/3 + 1/5 + 1/7 + ... ) = n log(log n)

where log(log n) is the sum of the reciprocals of primes up to n. This makes the Sieve of Eratosthenes faster than O(n log n) and thus also efficient, granted that we only need to iterate until floor(sqrt(n)) because if a number doesn't have factors greater than its square root then it's certainly prime.

The time complexity of the Extended Euclidean algorithm is similar to the Euclidean algorithm, which is polynomial time.

## Sources

- [RSA cryptosystem (Wikipedia)](https://en.wikipedia.org/wiki/RSA_cryptosystem)
- [Miller-Rabin primality test (Wikipedia)](https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test)
- [The Use of Miller-Rabin in Testing Prime Numbers in the Rsa Algorithm to Secure Files](https://ioinformatic.org/index.php/JAIEA/article/view/1685/1168)
