# refer to AI
import struct

def left_rotate(n, b):
    return ((n << b) | (n >> (32 - b))) & 0xFFFFFFFF

def sha0(message):
    orig_len_in_bits = (8 * len(message)) & 0xFFFFFFFFFFFFFFFF
    message += b'\x80'
    while (len(message) * 8) % 512 != 448:
        message += b'\x00'
    message += struct.pack('>Q', orig_len_in_bits)

    h0, h1, h2, h3, h4 = (
        0x67452301, 0xEFCDAB89, 0x98BADCFE, 0x10325476, 0xC3D2E1F0
    )

    for i in range(0, len(message), 64):
        w = list(struct.unpack('>16L', message[i:i+64]))
        for t in range(16, 80):
            w.append(left_rotate(w[t-3] ^ w[t-8] ^ w[t-14] ^ w[t-16], 0))

        a, b, c, d, e = h0, h1, h2, h3, h4

        for t in range(80):
            if t < 20:
                f = (b & c) | ((~b) & d)
                k = 0x5A827999
            elif t < 40:
                f = b ^ c ^ d
                k = 0x6ED9EBA1
            elif t < 60:
                f = (b & c) | (b & d) | (c & d)
                k = 0x8F1BBCDC
            else:
                f = b ^ c ^ d
                k = 0xCA62C1D6

            temp = (left_rotate(a, 5) + f + e + k + w[t]) & 0xFFFFFFFF
            e = d
            d = c
            c = left_rotate(b, 30)
            b = a
            a = temp

        h0 = (h0 + a) & 0xFFFFFFFF
        h1 = (h1 + b) & 0xFFFFFFFF
        h2 = (h2 + c) & 0xFFFFFFFF
        h3 = (h3 + d) & 0xFFFFFFFF
        h4 = (h4 + e) & 0xFFFFFFFF
        
    return f'{h0:08x}{h1:08x}{h2:08x}{h3:08x}{h4:08x}'

print(sha0(input().encode()))
