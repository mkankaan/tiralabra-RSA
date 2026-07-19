# Week 2 report

Created a UI module and started outlining the project file structure though it will likely change as the project goes on. Wrote the main program loop which gives the user the option to generate keys, encrypt or decrypt a message. The latter two options don't currently have any functionality.

Started working on key generation and wrote a function which currently returns an integer of a given bit length, which will be needed for generating 1024-bit primes. The next step is to check primality. I started looking into Miller-Rabin pseudocode, which I looked at briefly last week, but this week I got a better understanding of how it works, why it's probabilistic instead of deterministic and how to implement it in code.

Set up Pylint, unit tests and test coverage. Implemented the Sieve of Eratosthenes which was fairly quick to do and wrote unit tests for it. Next week I will continue with Miller-Rabin.

Time spent: 4 hours
