"""
Detect single-character XOR

One of the 60-character strings in this file has been encrypted by single-character XOR.

Find it.

(Your code from #3 should help.)
"""

from single_byte_xor import *

def get_most_probable_plaintext(ciphertext:str) -> tuple:
    scores = []
    for key in range(32, 127):
        xored = xor_with_byte(ciphertext, key)
        if not printable_bytes(xored):  # filter strings with non-printable chars
            continue
        score = score_english(xored)
        scores.append((key, xored, score))
    scores.sort(key = lambda x: x[2], reverse=True)
    return scores

if __name__ =="__main__":
    _scoreboard = []
    with open ("challenge4-strings.txt", mode='r') as f:
        for cipher in f:
            cipher = cipher.rstrip()
            scores = get_most_probable_plaintext(cipher)
            if not scores:
                continue
            _scoreboard.append(scores[0])
    _scoreboard.sort(key=lambda x: x[2], reverse=True)
    best = _scoreboard[0]
    print(f"Decrypted text: {best[1]}; key:{chr(best[0])}; score:{best[2]}")

            
            
