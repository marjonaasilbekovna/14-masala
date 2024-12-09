with open("input.txt", "r") as file:

    N, P = map(int, file.readline().strip().split())

javob = N * P

with open("output.txt", 'w') as file:

    file.write(str(javob))