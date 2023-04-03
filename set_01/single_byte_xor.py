"""
1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736

... has been XOR'd against a single character. Find the key, decrypt the message.

You can do this by hand. But don't: write code to do it for you.
How? Devise some method for "scoring" a piece of English plaintext. 
Character frequency is a good metric. Evaluate each output and choose the one with the best score. 
"""
import string
letter_freqs = {'a': 0.08167, 'b': 0.01492, 'c': 0.02782, 'd': 0.04253, 'e': 0.12702, 'f': 0.02228, 'g': 0.02015, 'h': 0.06094, 'i': 0.06966, 'j': 0.00153, 'k': 0.00772, 'l': 0.04025, 'm': 0.02406, 'n': 0.06749, 'o': 0.07507, 'p': 0.01929, 'q': 0.00095, 'r': 0.05987, 's': 0.06327, 't': 0.09056, 'u': 0.02758, 'v': 0.00978, 'w': 0.02360, 'x': 0.00150, 'y': 0.01974, 'z': 0.00074}
ciphertext = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"

def xor_with_byte(ciphertext:str, key:int):
    cipher_bytes = bytes.fromhex(ciphertext) #cipher bytes
    return bytes([b ^ key for b in cipher_bytes])

def score_english(bytes:bytes):
    """
    Scores the given bytes according to letter_freqs
    """
    score = 0
    for byte in bytes:
        score += letter_freqs.get(chr(byte), 0)
    return score
    
allowed_letters = string.ascii_letters + string.digits + string.punctuation + " ";
scoreboard = {}

if __name__=="__main__":
    for i in range(32,127): # all printable chars
        xored = xor_with_byte(ciphertext, i)
        if not all(chr(c) in allowed_letters for c in xored): # filter strings with non-printable chars
            continue
        else:
            score = score_english(xored)
            scoreboard[xored] = (score, i)

scoreboard = sorted(scoreboard.items(), key = lambda x:x[1][0], reverse=True) # sort by score
print(f"Most probable text: {scoreboard[0][0]}. Score: {scoreboard[0][1][0]}. Key: {scoreboard[0][1][1]}")