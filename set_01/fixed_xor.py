"""
Fixed XOR

Write a function that takes two equal-length buffers and produces their XOR combination.
If your function works properly, then when you feed it the string:
1c0111001f010100061a024b53535009181c
... after hex decoding, and when XOR'd against:
686974207468652062756c6c277320657965
... should produce:
746865206b696420646f6e277420706c6179
"""

if __name__=="__main__":
    hex1str = "1c0111001f010100061a024b53535009181c"
    hex2str = "686974207468652062756c6c277320657965"

    hex1 = bytes.fromhex(hex1str)
    hex2 = bytes.fromhex(hex2str)

    xor = b""

    for byte1, byte2 in zip(hex1,hex2):
        xor += bytes([byte1 ^ byte2]) #bytes takes an iterable as argument

    print(f'Success:  {xor.hex()=="746865206b696420646f6e277420706c6179"}')