import struct

# Open the test files
with open('maxint.uint64', 'rb') as f:
    print(struct.unpack('>Q', f.read())[0])