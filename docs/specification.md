# Requirements specification

## About the project



## Functionality

- **Key generation:** Generates a public key *(n, e)* and a private key *(n, d)* such that *n = p\*q* where *p* and *q* are distinct 2048-bit prime numbers. *e* is a prime number that is not a factor of *lcm(p-1, q-1)* (the least common multiple of *p-1* and *q-1*). Choose *d* such that *d ☰ e mod lcm(p-1, q-1)*.
- **Encryption:** Converts a plaintext message into ciphertext with the public key using modular exponentiation.
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

(This might change, these were just some of the algorithms I came across in my research.)

## Time/space complexity


## Sources

- [RSA cryptosystem (Wikipedia)](https://en.wikipedia.org/wiki/RSA_cryptosystem)
- [Miller-Rabin primality test (Wikipedia)](https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test)
- [The Use of Miller-Rabin in Testing Prime Numbers in the Rsa Algorithm to Secure Files](https://ioinformatic.org/index.php/JAIEA/article/view/1685/1168)
