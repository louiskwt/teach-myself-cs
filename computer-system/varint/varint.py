import struct


def encode(n):
    """
    - while n > 0:
        take lowest order 7 bits (little endian)
        add the correct most significant bit: 1 unless final 7 bit
        push to some sequence of bytes
        reduce n
    return byte sequence 
    """
    out = []
    while n > 0:
        part = n % 128 # TODO use bitmask
        # TODO add msb
        out.append(part)
        n >>= 7
    return bytes(out)

# Open the test files
with open('150.uint64', 'rb') as f:
    n = struct.unpack('>Q', f.read())[0]
    print(encode(n))