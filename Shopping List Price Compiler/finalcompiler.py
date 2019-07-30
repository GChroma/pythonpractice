
y = int(input("Type the amount of the first item you want: "))
z = int(input("Type the amount of the second item you want: "))
w = int(input("Type the amount of the third item you want: "))

totalprice = 0

with open("Shopping List.txt") as sl:
    pri
    for line in sl:
        totalprice += float(line.split(":")[1])

print(round(totalprice, 2))