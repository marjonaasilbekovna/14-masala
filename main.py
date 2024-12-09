N = int(input())
elements = list(map(int, input().split()))

n = 0

for num in elements:
    n ^= num 
print(n)