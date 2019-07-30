import ShoppingCart
shoppinglist = []

with open("Shopping List.txt") as sl:
    for x in sl:
        item = ShoppingCart.Item(x.split(":")[0], float(x.split(":")[1]), float(x.split(":")[2]))
        shoppinglist.append(item)

total = ShoppingCart.ShoppingCart(shoppinglist).total()


f=open("Summary.txt", "a+")
f.write(str(total))
f.close()