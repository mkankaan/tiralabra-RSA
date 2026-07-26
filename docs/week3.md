# Week 3 report

This week I was busy and didn't have a lot of time to work on the project but I started writing the code for Miller-Rabin. Currently the program generates one 1024-bit number and checks if it's divisible by any of the ~500 smallest primes using the sieve. If not, the number is passed to Miller-Rabin. I'm currently working on the witness generation part and that's where I'll continue next week.

What I'm unsure about: In many sources I looked at, they didn't check whether the same witness had already been generated. Since it can potentially be a very large number, the likelihood of getting the same witness more than once is very low. In Python, lookup could be done with set() with an average time complexity of O(1), but I'm still wondering if storing all the previously generated witnesses and checking for duplicates is worth the time and space cost.

Next week I plan to get Miller-Rabin done, write tests for it and start working on key generation if there's time. So far my program generates one prime candidate, so I'll have to see how slow running Miller-Rabin many times for multiple pairs of prime candidates will be and if I have to tweak my code in accordance.

Time spent: 4 hours
