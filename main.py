with open('input.txt', 'r') as fayl:
    son = list(map(int, fayl.readline().strip().split()))
son.sort()
min_son = sum(son[:4])
max_son = sum(son[1:])

with open('output.txt', 'w') as file:
    file.write(f"{min_son} {max_son}")