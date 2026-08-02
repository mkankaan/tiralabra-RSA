# RSA

Python implementation of RSA

- [Specifications document](https://github.com/mkankaan/tiralabra-RSA/blob/main/docs/specification.md)
- [Installation (Linux/MacOS)](#installation)
- [How to use the application](#howto)
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

# <a name="howto"></a> How to use the application

In the application menu, select **g** to generate keys, **e** to encrypt or **d** to decrypt text.

- **Generate keys:** Generate a public and private key pair. The public key can be shared with your friends and can be used to encrypt messages that are sent to you, but keep the private key secret. Only your private key can be used to decrypt a message that was encrypted with your public key.
- **Encrypt:** Enter a message you would like to decrypt into ciphertext along with the public key you got in the previous step.
- **Decryption:** Enter the ciphertext you got in the previous step along with the private key that matches the public key that it was encrypted with.

(Note for peer reviews: the application is still under debugging and the keys don't follow a standard RSA key length or format. Decryption is currently a bit bugged and only works correctly with short plaintext messages (max 4 characters, for example "abcd"))

# <a name="testing"></a> Testing

Tests can be run with:

```
$ poetry run pytest
```

View coverage report:
```
$ poetry run coverage report -m
```
