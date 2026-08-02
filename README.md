# RSA

Python implementation of RSA

Note for peer reviews: currently the program has the functionality to generate key pairs and encrypt and decrypt messages. You can enter a public key with a plaintext message to encrypt it, and a private key with a ciphertext message to decrypt it. Decryption is currently bugged and only works correctly with short plaintext messages (max 4 characters, for example "abcd")

- [Specifications document](https://github.com/mkankaan/tiralabra-RSA/blob/main/docs/specification.md)
- [Installation (Linux/MacOS)](#installation)
- [Testing](#testing)

**Weekly reports**
- [Week 1](https://github.com/mkankaan/tiralabra-RSA/blob/main/docs/week1.md)
- [Week 2](https://github.com/mkankaan/tiralabra-RSA/blob/main/docs/week2.md)
- [Week 3](https://github.com/mkankaan/tiralabra-RSA/blob/main/docs/week3.md)
- [Week 4](https://github.com/mkankaan/tiralabra-RSA/blob/main/docs/week4.md)


# <a name="installation"></a> Installation (Linux/MacOS)


The project requires Python >= 3.12 and Poetry >= 2.0. Run the following commands in the root of the project folder. Replace "python3" if Python is installed under a different name.

Install dependencies:

```
$ poetry install
```

Start the application:
```
$ poetry run python3 src/index.py
```

# <a name="testing"></a> Testing

Run tests with:

```
$ poetry run pytest
```

View coverage report:
```
$ poetry run coverage report -m
```
