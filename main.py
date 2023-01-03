import RSA

if __name__ == '__main__':
    print("********************************")
    print("What would you like to do?")
    print("You can:")
    print("********************************")
    print("1. Get private and public keys")
    print("2. Encrypt")
    print("3. Decrypt")
    print("********************************")
    
    user_continue = 1;
    while user_continue == 1:
        task=int(input("Enter number of what you'd like to do "))
        if task==1: # user prompted to enter 2 small prime numbers to generate key pairs
            p = int(input("Enter a small prime number (5,7,13,17,19,etc): "))
            q = int(input("Enter another small prime number (Different from above): "))
            n=p*q
            public_key = RSA.Find_Public_Key_e(p, q)
            print("Your public key (e, n) is  ", public_key)
            e=public_key[0] # pull e from tuple to use in private key calculation
            private_key = RSA.Find_Private_Key_d(e,p, q) 
            print("Your private key is (d, n) ",private_key)
    
        elif task==2: # user is prompted to enter a message and public key
            message = input("Enter a message to encrypt with your public key: ")
            n=int(input("Enter a n: "))
            e=int(input("Enter an e: "))
            encrypted_message= RSA.Encode(n,e,message)
            print("Your encypted message is: ", encrypted_message)
    
        elif task==3: # user is prompted to enter an encrypted message and private key
            encrypted_msg_str = input("Enter an encoded message without brackets: ") # user input is long string
            msg_lst_str=list(encrypted_msg_str.split(",")) # split string into individual elements
            msg_lst_int=[int(i) for i in msg_lst_str] # convert elements from string to integers so Decode function will run properly
            n=int(input("Enter a n: "))
            d=int(input("Enter a d: "))   
            print(RSA.Decode(n,d, msg_lst_int))
        else:
            user_continue == 0
            print("Thank you for using my encrypter/ decrypter tool. Quitting now...")
            exit()