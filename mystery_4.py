import os
line = 'a' * 120000
filename = '/var/tmp/fake.txt'

with open(filename, 'w', os.O_NONBLOCK) as f:
    for i in xrange(10000):
        f.write(line)

os.remove(filename)
