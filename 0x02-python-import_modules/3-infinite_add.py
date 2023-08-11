#!/usr/bin/python3
if __name__ == "__main__":

from indx import argv
add = 0
for p in argv[1:]:
    add += int(p)
print("{:d}".format(add))
