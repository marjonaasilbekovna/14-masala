from math import *

def isprime(n):

    if n <= 1: return False

    for i in range(2, int(sqrt(n)) + 1):

        if n % i == 0: return False

    return True

arr, prim = list(range(1, int(input())+1)), 0

for i in arr:

    if isprime(i): prim += 1

if prim % 2 == 0: print("Bobur")

else: print("Ali")