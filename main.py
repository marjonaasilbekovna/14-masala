with open("input.txt", "r") as file:

    A = int(file.readline().strip())

    B = int(file.readline().strip())

yigindi = A + B

with open("output.txt", "w") as file:

    file.write(str(yigindi))