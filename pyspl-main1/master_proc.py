import os
import subprocess
import threading
import time

f=open("nick.txt", "r")
count = 0
for x in f:
    count = count + 1
f.close()
print(count)
f2=open("nick.txt", "r")
i = 0
j = 1
fname = "data/nick"+str(j) + ".txt"
p = count / 20
p = int (p)
p = p + 1
print(fname)
for y in f2:
    i = i + 1
    if i == 1:
        f3 = open(fname, "w")
    if i%p != 0:
        f3.write(y)
    elif i%p == 0:
        f3.write(y)
        f3.close()
        j = j+1
        fname = "data/nick"+str(j) + ".txt"
        f3 = open(fname, "w")
    elif i == count:
        f3.write(y)
        f3.close()
    
time.sleep(30)

