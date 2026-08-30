# Implementation document

## General structure

The application runs on the command like and has three main features: key generation, encryption and decryption. The application is hardcoded to generate 1024-bit primes, resulting in a standard 2048-bit RSA key. The standard public exponent 65537 is also hardcoded.

Classes:

- **UI** - Handles the main program loop, user inputs and input validation.
- **Key** - Represents both a public and private key. Implemented using Python's built-in NamedTuple data structure, since the class only needs to store data and doesn't have any methods.

Modules:

- **key_generator.py** - Handles the generation of keys, which are returned as a pair of Key objects. Relies on *prime_generator.py* to find primes for the keys. Also contains the modular multiplicative inverse algorithm, which is used to calculate the private exponent.
- **prime_generator.py** - Contains the main loop for generating numbers until a prime is found. Also contains the Sieve of Eratosthenes algorithm, which is called once at the start of the key generation process. The list of small primes is then passed on as an argument throughout the primality checking process to avoid having to generate the list multiple times.
- **miller_rabin.py** - Contains the Miller-Rabin algorithm and a helper function for deconstructing an integer into powers of two.
- **encryption_decryption.py** - Contains the functionality for converting a plaintext message into ciphertext and vice versa.

## Time complexity, Big O analysis

The Sieve of Eratosthenes runs in O(n log (log n)) [(explained here)](https://github.com/mkankaan/tiralabra-RSA/blob/main/docs/week6.md)

The iterative Extended Euclidean algorithm (used to find the modular multiplicative inverse) runs in O(log min(n, m)) time due to the repeated division of the two inputs *n* and *m*, which depends on the smaller one of them. It has the same time complexity as the basic Euclidean algorithm since there are no extra steps.

As for the runtime complexity of Miller-Rabin, I found conflicting information with little explanation. 

The [original paper](https://www.sciencedirect.com/science/article/pii/S0022000076800438) by Gary L. Miller states that his deterministic algorithm runs in O(log⁴ n) time proportional to the bit length of the prime candidate *n*. Michael O. Rabin later modified this algorithm to make it probabilistic (thus faster), resulting in the Miller-Rabin test we have today. In his [paper](https://www.sciencedirect.com/science/article/pii/0022314X80900840?via%3Dihub) Rabin states the runtime to be O(log² n). However, other sources say anywhere between O(log² n) and O(log⁴ n).

The outer loop is repeated *k* times and the inner loop is repeated up to *s* times, where *s* < log n and the constant *k* is the number of witnesses and can be omitted from the runtime analysis.

Generating a random witness *a* is O(1) and doesn't effect the overall runtime.  a<sup>d</sup> (mod n) is O(log d) which is within O(log n). Repeated squaring is O(log² n). This is how we arrive at O(log³ n), repeated *k* times.

Some sources treat *s* as a constant independent from *n*, although it is derived from *n*. This way of thinking would give the runtime O(ks log² n) = O(log² n), which would explain the differing opinions.

## Improvements

The keys don't adhere to a real RSA format (which uses Base64 or other encodings) but instead the keys are long strings with the modulus and exponent parts simply separated by "-". Real RSA keys are shorter in length despite having the same bit length. In my application the keys are quite long and can be annoying and error-prone to copy-paste. Usability could be improved with some kind of login system, where each key is tied to a username. That would remove the hassle of having to manually pass the keys around.

## Use of AI

AI was not used in this project.

## Sources

- [RSA cryptosystem (Wikipedia)](https://en.wikipedia.org/wiki/RSA_cryptosystem)
- [Miller-Rabin primality test (Wikipedia)](https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test)
- [The Use of Miller-Rabin in Testing Prime Numbers in the Rsa Algorithm to Secure Files](https://ioinformatic.org/index.php/JAIEA/article/view/1685/1168)
- [Miller-Rabin Primality Test (YouTube)](https://www.youtube.com/watch?v=qdylJqXCDGs)
- [How to Implement the Miller-Rabin Primality Test (YouTube)](https://www.youtube.com/watch?v=-BWTS_1Nxao)
- [Modular arithmetic (Wikipedia)](https://en.wikipedia.org/wiki/Modular_arithmetic)
- [The Miller-Rabin Test](https://kconrad.math.uconn.edu/blurbs/ugradnumthy/millerrabin.pdf)
- [Modular Multiplicative Inverse](https://www.geeksforgeeks.org/dsa/multiplicative-inverse-under-modulo-m/)
- [GCD, Bezout, and Modular Inverses | The Extended Euclidean Algorithm (YouTube)](https://www.youtube.com/watch?v=YZfPcvbwwvI)
- [Extended Euclidean Algorithm](https://cp-algorithms.com/algebra/extended-euclid-algorithm.html)
- [Modular Multiplicative Inverse](https://www.geeksforgeeks.org/dsa/multiplicative-inverse-under-modulo-m/)
- [Programming With Prime Numbers](https://programmingpraxis.com/wp-content/uploads/2012/09/primenumbers.pdf)

Sources for runtime complexity:

- [Riemann's hypothesis and tests for primality](https://www.sciencedirect.com/science/article/pii/S0022000076800438)
- [Probabilistic algorithm for testing primality](https://www.sciencedirect.com/science/article/pii/0022314X80900840?via%3Dihub)
- [Four primality testing algorithms](https://arxiv.org/pdf/0801.3840)
- [On a Modification of the Agrawal-Biswas Primality Test](https://arxiv.org/pdf/1810.09651)
- [Complexity of exponentiation](https://www.cs.toronto.edu/~guerzhoy/180f16/lectures/W12/lec2/ComplExp.html)
- [Time Complexity of Euclid’s Algorithm](https://www.baeldung.com/cs/euclid-time-complexity)

