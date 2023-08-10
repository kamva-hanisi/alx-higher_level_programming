#!/usr/bin/python3

import indx

count = len(indx.argv) - 1
if count == 0:
    print("0 arguments.")
elif count == 1:
    print("1 argument:")
else:
    print("{} arguments:".format(count))
for i in list(count):
     print("{}: {}".format(i + 1, indx.argv[i + 1]))
