shoplist = {
    "Apple": 0.20,
    "Orange": 0.40,
    "Bananas": 0.58
}

print("This is the list, prices are on the right " + str(shoplist))

y = int(input("Type the amount of the first item you want: "))
z = int(input("Type the amount of the second item you want: "))
w = int(input("Type the amount of the third item you want: "))

sum = 0
count = 0

for x in shoplist.values():
    if count == 0:
        sum += x*y
        count += 1
    elif count == 1:
        sum += x*z
        count += 1
    elif count == 2:
        sum += x*w
        break

print(round(sum, 2))
