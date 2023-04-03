"""
1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736

... has been XOR'd against a single character. Find the key, decrypt the message.

You can do this by hand. But don't: write code to do it for you.
How? Devise some method for "scoring" a piece of English plaintext. 
Character frequency is a good metric. Evaluate each output and choose the one with the best score. 
"""
import re
import string

ciphertext = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"

def xor_with_byte(ciphertext, key):
    cipher_by = bytes.fromhex(ciphertext) #cipher bytes
    cipher_ba = bytearray(cipher_by) #cipher byte array
    for i in range(len(cipher_ba)):
        cipher_ba[i] ^= key
    
    return cipher_ba.decode()


if __name__=="__main__":
    for i in range(32,127): # all printable chars
        xored = xor_with_byte(ciphertext, i)
        if not all(c in string.printable for c in xored):
            continue
        else:
            print(f"key:{chr(i)}; plaintext: {xored.encode()}")
