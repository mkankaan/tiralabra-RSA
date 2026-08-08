# Week 5 report

This week I finished implementing the encryption and decryption, so the application is now pretty much done with only minor tweaks left. I received good suggestions for improvements and tools to use in the peer review. Especially parameterized tests and a parameter-based CLI seemed like good ideas. I might not rewrite the entire UI but I'll definitely keep that in mind for future projects. I have never worked on an actual software project that carried out large enough operations that performance was an issue, so this has been an interesting learning experience. I had habitually written the code with general good practices in mind (split the code into small easily testable functions that do only one thing) but it turns out that function calls are slow, which also applies to recursion. So I was advised to remove small functions and for example write the entire Miller-Rabin as one function.

I had written some unit tests earlier but had been holding off on thorough testing before the testing lecture, where I got advice on what kinds of tests would be necessary for my project. For example the is_prime() function relies on sieve_of_eratosthenes() (indirectly) and calls miller_rabin() (sometimes) so writing near-identical unit tests for is_prime() and miller_rabin() would have been redundant.

Initially I would have wanted the keys to be in an actual RSA format (PEM, DER etc.) instead of a monstrous integer but I couldn't find any instructions on how to actually do the encoding or any libraries to handle specifically that. Instead all the libraries I found had the formatting built into the key generation itself, which wasn't what I was looking for, since the task was to generate the keys myself. I experimented with Base64 (which is what I think PEM uses) but it didn't make the keys any shorter, so I decided to keep them as is. It's a bit annoying for the user to copy-paste but I think for the purposes of this project it will have to do.

I started writing the testing and implementation documents. The code needs to be commented in docstring, so that will be left for next week, as well as finishing other documentation.

I would like to ask if the tests are sufficient for the course requirements?

Time spent: 12 hours