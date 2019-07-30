shoplist = {
    "Apple": 0.20,
    "Orange": 0.40,
    "Bananas": 0.58
}

sum = 0

for x in shoplist.values():
    sum += x

print(round(sum, 3))
