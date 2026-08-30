# User guide

## <a name="installation"></a> Installation (Linus/MacOS/Windows)


The project requires Python >= 3.12 and [Poetry](https://python-poetry.org/) >= 2.0. Run the following commands in the root of the project folder. Replace "python3" if Python is installed under a different name.

Install dependencies:

```
poetry install
```

Start the application:
```
poetry run python3 src/index.py
```

## <a name="usage"></a> How to run the application

Select **g** to generate keys, **e** to encrypt or **d** to decrypt text.

- **Generate keys:** Generate a pair of 2048-bit RSA keys. The public key can be shared with your friends and can be used to encrypt messages that are sent to you, but keep the private key secret. Only your private key can be used to decrypt a message that was encrypted with your public key.
- **Encryption:**

  *Inputs:*
  - ***Public key:*** A public key you received in the first step. Enter the public key of the person you want to send a message to. Must be in the format *"%i-%i"* where *%i* is an integer.
  - ***Message:*** A plaintext message to be encrypted. If the message is too long (determined by the key length), the user will be prompted to enter a shorter message.
- **Decryption:**

    *Inputs:*
    - ***Private key:*** A private key you received in the first step. Enter the private key of the person who will receive the message. Must be in the format *"%i-%i"*.
    - ***Ciphertext:*** Enter the ciphertext you got in the previous step. Must not contain spaces or any non-numerical characters.



## <a name="testing"></a> Running tests

Tests can be run with:

```
poetry run pytest
```

View coverage report:
```
poetry run coverage report -m
```
