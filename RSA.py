def Convert_Text(_string):
    # list to store unicode
    integer_list = []
    
    # for loop that iterates through each character in a string
    # and appends an integer representing the Unicode code point of that character to a list
    for achar in _string:
        integer_list.append(ord(achar))
    return integer_list

def Convert_Num(_list):
    # initialize string
    _string = ''
    
    # for loop takes list of integers and converts them to a string
    for i in _list:
        _string += chr(i)   
    return _string

def Convert_Binary_String(_int):
    # convert integer to binary expansion without 0B prefix
    bits=bin(_int)[2:]
    return bits

def FME(b, n, m): 
    result=1 # initialize result
    square=b # initialize repeated square
    
    while n>0: # loop converts n to binary
        k=n%2 # extracts least significant bit
        if k==1:
            result=(result*square)%m
        square=(square*square)%m # repeatedly squaring
        n>>=1 # added bitwise right shift operator to exit loop
    return result 

def Euclidean_Alg(a, b):
    # Algorithm to compute GCD
    # assume a>=b>=0 
    # ensure algorithm works when negative numbers get passed through
    a=abs(a)
    b=abs(b)
    
    while b>0: 
        k=a%b # calculates remainder
        a=b # updates a
        b=k # updates b
    return a

import random
def Find_Public_Key_e(p, q):
    # calculate phi and n per Khan Academy videos
    phi=(p-1)*(q-1)
    n=p*q
    e=random.randrange(1,100) # randomly generate e between 1 and 100; don't want a negative as e, but also want to keep e small
    gcd_e=Euclidean_Alg(e,phi) # calculate GCD of e and phi to determine if relatively prime
    
    
    # loop will keep going until it finds an e that is relatively prime to phi
    while gcd_e!=1:
        e=random.randrange(1,100) # recalculates e 
        gcd_e=Euclidean_Alg(e,phi) # recalculates GCD of e and phi
    return (e,n)

def Extended_Euclidean_Alg(m, n):
    # initialize variables that will hold benzout coefficient
    s1,t1=1,0
    s2,t2=0,1
    
    # original m and n to remove negatives from return results
    m_orig=m
    n_orig=n
    
    while n>0:
        k=m%n # calculates remainder
        q=m//n # calculates quotient
        m=n # updates n value
        n=k # updates n value
        s1h,t1h=s2,t2 # initializes s1^ and t1^
        s2h,t2h=s1-q*s2,t1-q*t2 # initializes s2^ and t2^
        s1,t1=s1h,t1h # updates s1 and t1
        s2,t2=s2h,t2h # updates s2 and t2
    while s1<0: # if negative add modulo of original m
        s1+=m_orig
    while t1<0: # if negative add modulo of original n
        t1+=n_orig
        t1+=n_orig
    return m, s1, t1 # returns GCD, s1, t1

def EEA_mod_inverse(e,n):
    gcd, s1, t1 = Extended_Euclidean_Alg(e,n) # e is from public key and n = phi which is (p-1) * (q-1)
    return s1 # s1 is the inverse of e

def Find_Private_Key_d(e, p, q):
    # calculate n and phi
    n=p*q 
    phi_n=(p-1)*(q-1)
    
    # calculate d using EEA; note n used in this formula is phi_n and not n
    d=EEA_mod_inverse(e,phi_n)
    return d, n

def Encode(n, e, message):
    cipher_text = [] # initialize cipher text list
    
    text_to_num=Convert_Text(message) # convert message text to numbers
    for num in text_to_num: # loop will iterate through each number and encode it
        encode=FME(num,e,n)
        cipher_text.append(encode) # append encoded message to list
    return cipher_text

def Decode(n, d, cipher_text):
    message = '' # initialize message string
    num_list=[] # initialize number list
    
    # loop interates through every integer in cipher text
    # decrypts each integer using FME
    # appends decrypted message to number list
    # then converts number list to readable message
    for i in range(len(cipher_text)):
        decode=FME(cipher_text[i],d,n)
        num_list.append(decode)
        message=Convert_Num(num_list)
    return message