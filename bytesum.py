import sys

filename = sys.argv[1]

with open(filename) as f:
    bytesum = 0
    bytes = f.read()
    for b in bytes:
        bytesum += ord(b)
print bytesum
