def reverse_hash(h, k):
    # reverse block processing for each block
    for i in range(len(h)-2, -1, -1):
        # reverse final step of block processing
        temp2 = h[i+1]
        temp1 = h[i]
        for j in range(63, -1, -1):
            s0 = rightrotate(temp1, 2) ^ rightrotate(temp1, 13) ^ rightrotate(temp1, 22)
            s1 = rightrotate(temp2, 6) ^ rightrotate(temp2, 11) ^ rightrotate(temp2, 25)
            maj = (temp1 & temp2) ^ (temp1 & h[i+2]) ^ (temp2 & h[i+2])
            t2 = s0 + maj
            ch = (temp1 & temp2) ^ ((~temp1) & h[i+2])
            t1 = h[i] + s1 + ch + k[j] + t2
            temp2 = temp1
            temp1 = t1
        h[i] = temp1
    # output final hash value
    return h[0]

def rightrotate(x, n):
    return (x >> n) | (x << (32 - n))

def unpad_message(message):
    # get length of original message from end of padded message
    length = int(''.join(str(x) for x in message[-64:]), 2)
    # remove length and single '1' bit from end of padded message
    message = message[:-65] + [1]
    # remove any additional zero bits from end of padded message
    while len(message) % 512 != 448:
        message.append(0)
    # add length to end of padded message
    message += [int(b) for b in bin(length)[2:].zfill(64)]
    return message

def reverse_sha256(message):
    # unpad padded message to get original message
    message = unpad_message(message)
    # split message into 512-bit blocks
    blocks = [message[i:i+512] for i in range(0, len(message), 512)]
    # initialize hash values to final hash value
h = [int(v, 16) for v in '6a09e667f3bcc908' 'bb67ae8584caa73b' '3c6ef372fe94f82b' 'a54ff53a5f1d36f1' '510e527fade682d1' '9b05688c2b3e6c1f' '1f83d9abfb41bd6b' '5be0cd19137e2179']
    # reverse hash for each block
for block in reversed(blocks):
        # split block into 32-bit words
        words = [int(''.join(str(x) for x in block[i:i+32]), 2) for i in range(0, len(block), 32)]
        # reverse the word order
        words = list(reversed(words))
        # extend words to 64 words
        for i in range(16, 64):
            s0 = rightrotate(words[i-15], 7) ^ rightrotate(words[i-15], 18) ^ (words[i-15] >> 3)
            s1 = rightrotate(words[i-2], 17) ^ rightrotate(words[i-2], 19) ^ (words[i-2] >> 10)
            words.append((words[i-16] + s0 + words[i-7] + s1) % (2**32))
        # initialize hash values for this block
        a, b, c, d, e, f, g, h = h
        # reverse hash for this block
for i in range(64):
            s1 = rightrotate(e, 6) ^ rightrotate(e, 11) ^ rightrotate(e, 25)
            ch = (e & f) ^ ((~e) & g)
            t1 = (h + s1 + ch + k[i] + words[i]) % (2**32)
            s0 = rightrotate(a, 2) ^ rightrotate(a, 13) ^ rightrotate(a, 22)
            maj = (a & b) ^ (a & c) ^ (b & c)
            t2 = (s0 + maj) % (2**32)
            h = g
            g = f
            f = e
            e = (d + t1) % (2**32)
            d = c
            c = b
            b = a
            a = (t1 + t2) % (2**32)
        # update hash values for next block
h = (h + g) % (2**32)
g = (g + f) % (2**32)
f = (f + e) % (2**32)
e = (e + d) % (2**32)
d = (d + c) % (2**32)
c = (c + b) % (2**32)
b = (b + a) % (2**32)
a = (a + h) % (2**32)
    # concatenate hash values to get final hash
final_hash = hex(a)[2:].zfill(8) + hex(b)[2:].zfill(8) + hex(c)[2:].zfill(8) + hex(d)[2:].zfill(8) + hex(e)[2:].zfill(8) + hex(f)[2:].zfill(8) + hex(g)[2:].zfill(8) + hex(h)[2:].zfill(8)
def reverse_sha512(message):
    # unpad padded message to get original message
    message = unpad_message(message)
    # split message into 512-bit blocks
    blocks = [message[i:i+512] for i in range(0, len(message), 512)]
    # initialize hash values to final hash value
    h = [int(v, 16) for v in ['6a09e667f3bcc908', 'bb67ae8584caa73b', '3c6ef372fe94f82b', 'a54ff53a5f1d36f1', '510e527fade682d1', '9b05688c2b3e6c1f', '1f83d9abfb41bd6b', '5be0cd19137e2179']]
    # reverse hash for each block
    for block in reversed(blocks):
        # split block into 64 64-bit words
        words = [int(''.join(str(x) for x in block[i:i+64]), 2) for i in range(0, len(block), 64)]
        # reverse the word order
        words = list(reversed(words))
        # extend words to 80 words
        for i in range(16, 80):
            s0 = rightrotate(words[i-15], 1) ^ rightrotate(words[i-15], 8) ^ (words[i-15] >> 7)
            s1 = rightrotate(words[i-2], 19) ^ rightrotate(words[i-2], 61) ^ (words[i-2] >> 6)
            words.append((words[i-16] + s0 + words[i-7] + s1) % (2**64))
        # initialize hash values for this block
        a, b, c, d, e, f, g, h = h
        # reverse hash for this block
        for i in range(80):
            s1 = rightrotate(e, 14) ^ rightrotate(e, 18) ^ rightrotate(e, 41)
            ch = (e & f) ^ ((~e) & g)
            t1 = (h + s1 + ch + k[i] + words[i]) % (2**64)
            s0 = rightrotate(a, 28) ^ rightrotate(a, 34) ^ rightrotate(a, 39)
            maj = (a & b) ^ (a & c) ^ (b & c)
            t2 = (s0 + maj) % (2**64)
            h = g
            g = f
            f = e
            e = (d + t1) % (2**64)
            d = c
            c = b
            b = a
            a = (t1 + t2) % (2**64)
        # update hash values for next block
        h = (h + g) % (2**64)
        g = (g + f) % (2**64)
        f = (f + e) % (2**64)
        e = (e + d) % (2**64)
        d = (d + c) % (2**64)
        c = (c + b) % (2**64)
        b = (b + a) % (2**64)
        a = (a + h) % (2**64)
    # concatenate the final hash values
message_digest = bin(a)[2:].zfill(64)


