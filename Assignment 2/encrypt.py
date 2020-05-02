import sys
from struct import pack, unpack


def F(w):
    return ((w * 31337) ^ (w * 1337 >> 16)) % 2 ** 32


def encrypt(block):
    a, b, c, d = unpack("<4I", block)
    for rno in range(32):
        a, b, c, d = b ^ F(a | F(c ^ F(d)) ^ F(a | c) ^ d), c ^ F(a ^ F(d) ^ (a | d)), d ^ F(a | F(a) ^ a), a ^ 31337
        a, b, c, d = c ^ F(d | F(b ^ F(a)) ^ F(d | b) ^ a), b ^ F(d ^ F(a) ^ (d | a)), a ^ F(d | F(d) ^ d), d ^ 1337
    return pack("<4I", a, b, c, d)



def decrypt(block):
    a, b, c, d = unpack("<4I", block)
    for i in range(32):
        # second step
        original_a = a
        d = d ^ 1337
        a = c ^ F(d | F(d) ^ d)
        b = b ^ F(d ^ F(a) ^ (d | a))
        c = original_a ^ F(d | F(b ^ F(a)) ^ F(d | b) ^ a)
        # first step
        original_a = a
        a = d ^ 31337
        d = c ^ F(a | F(a) ^ a)
        c = b ^ F(a ^ F(d) ^ (a | d))
        b = original_a ^ F(a | F(c ^ F(d)) ^ F(a | c) ^ d)
    return pack("<4I", a, b, c, d)

with open("flag.enc") as fin :
    k=fin.read()
    pt=""
    for i in range(0,len(k),16):
        pt+=decrypt(k[i:i+16])
    print(pt)

with open ("decrypted_text.txt",'w') as fout :
  fout.write(pt)
