# RSA
RSA project in python
### Background: 
Public key encryption allows senders and receivers to determine secret keys by transferring information/ messages completely in the open. RSA is the most common public key encryption system. This project demonstrates how RSA works to encrypt and decrypt message using private and public keys. An overview of the entire process as described in the Khan Academy videos available online is as followed.

Bob has a message he converted to a number M. Alice generates her public and private keys as followed. First Alice generates 2 numbers of similar size P1 = 53 and P2 = 59 then multiplies them to get N = 3127. Then Alice calculates Phi(N) as (53-1) * (59-1) = 3016. Next Alice picks a small public exponent E = 3 (must be an odd number that does not share a factor with Phi(N)). Finally, Alice finds the value of her private exponent D = 2 * (3016) + 1/3= 2011. Alice hides everything except the value of N and E as these are her public key (open lock). Alice sends her public key to Bob to lock his message with. Bob locks his message by calculating $M^E$ mod N. Let's call Bob's encrypted message C. Alice decrypts message using her private key D so $C^D$ mod N equals Bob's original message.

### How secure is RSA? Why is it difficult to break codes in RSA? Is my implementation of RSA secure?
Brute force algorithms solve problems in the most straight forward way without regard to the computing resources required. A basic brute force factorization algorithm is the starting point for code breaking as it finds the smallest factor of n when the public key (n, e) is known. This factor, p, is used to calculate another number, q, that when multiplied by p returns n. E, p, and q are then used to generate a private key that can be used to decrypt an encoded message. A brute force algorithm will not work with exceptionally large n’s because the amount of time it takes to run the algorithm grows exponentially as n grows larger. For example, an n which is 200 digits in length will run 10200 steps to generate the smallest factor which will take eons to run.

RSA is very secure if implemented properly. Unlike in this project, RSA would typically use two very large prime numbers each with more than 200 digits. There is no method known to decrypt messages that is not based on finding a factorization of n, or that does not also lead to the factorization of n. Factorization is a difficult problem as opposed to simply finding large prime numbers. The most efficient factorization method requires billions of years to factor a 400-digit integer. This implementation of RSA would not be considered secured because I am not using large n’s. Although some people can crack codes with n’s that are many digits long using other algorithms (not brute force), those people would not be able to crack true RSA encryption without the use of many years and super computers.

### Function Definitions:

* def Convert_Text(_string):
Takes in a simple string such as "hello" and outputs the corresponding standard list of integers (ascii) for each letter in the word hello.

* def Convert_Num(_list):
Takes in a list of integers and outputs the corresponding string (ascii).

* def Convert_Binary_String(_int):
Converts an integer to a string of its binary expansion.

* def FME(b, n, m):
Using the fast modular exponentiation algorithm,the below function should return b**n mod m where b is the base, e is the exponent, and m is the modulus.


* def Euclidean_Alg(a, b):
Calculate the Greatest Common Divisor of a and b. The function must return a single integer 'x' which is
the gcd of a and b.

* def Find_Public_Key_e(p, q):
Function takes 2 prime numbers p and q and returns 2 elements of the primary key n and e. This function will run a loop to find e such that e is relatively prime to (p - 1) (q - 1) and not equal to p or q.

* def Extended_Euclidean_Alg(m, n):
The extended Euclidean algorithm is an extension to the Euclidean algorithm, and computes, in addition to the greatest common divisor (gcd) of integers a and b, also the coefficients of Bézout's identity

* def EEA_mod_inverse(e,n):
The computation of the modular multiplicative inverse is an essential step in the derivation of key-pairs in the RSA public-key encryption method

* def Find_Private_Key_d(e, p, q):
Find the decryption exponent d such that d is the modular inverse of e. This function should return the decryption component d.
    
* def Encode(n, e, message):
The message will be a string of characters. Use the function Convert_Text from and get a list of numbers. Encode each of those numbers using n and e and return the encoded cipher_text.

* def Decode(n, d, cipher_text):
The cipher_text will be a list of integers. First, decrypt each of those integers using n and d. Then use the function Convert_Num, that converts the integers to a string, to recover the original message as a string.  
