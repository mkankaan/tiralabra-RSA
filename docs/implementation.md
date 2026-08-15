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

## Time and space complexity, Big O analysis

(to be added)


## Improvements

The keys don't adhere to a real RSA format (which uses Base64 or other encodings) but instead the keys are large integers with the modulus and exponent simply separated by "-". Real RSA keys are shorter in length, despite having the same bit length. In this application, the keys that the user has to work with are quite long and can be annoying (and error-prone) to copy-paste. Usability could be improved with some kind of login system, where each key is tied to a username. That would remove the hassle of having to manually pass the keys around.

## Sources

to be added

AI was not used in this project.
