#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
f = 1
n = number
if n < 0:
    n = -n
    f = -1
l = n % 10
if f == -1:
    l = -l
print("Last digit of ", end="")
if l > 5:
    print("{} is {} and is greater than 5".format(n * f, l))
elif l == 0:
    print("{} is 0 and is 0".format(n * f))
else:
    print("{} is {} and is less than 6 and not 0".format(n * f, l))
