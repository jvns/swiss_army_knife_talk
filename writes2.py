import os
line = 'a' * 300
filename = '/home/bork/fake.txt'

with open(filename, 'w') as f:
    for i in xrange(400000):
        f.write(line)
    f.flush()
    os.fsync(f.fileno())

