A, B = map(int, input().split())  
if A > B:
    natija = ">"
elif A < B:
    natija = "<"
else:
    natija = "="
print(natija)