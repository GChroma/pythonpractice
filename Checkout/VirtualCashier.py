import Module1

catalog = []
with open("Catalog.txt") as catobj:
    for x in catobj:
        newitems = Module1.CItems(x.split(":")[0], float(x.split(":")[1]), float(x.split(":")[2]))
        catalog.append(newitems)

Module1.CList(catalog).display()
#Take user choices
useritems = []
x = 0
while x != 1:
    uinput = input("Input the item you want and how much of the item you want in this format: item:amount  Type \"Finish\" when you're done \n: ")
    if uinput.lower() == "finish":
        break
    nameitem = str(uinput.split(":")[0])
    amountitem = int(uinput.split(":")[1])
    subtotalitem = Module1.CList(catalog).getprice(nameitem)*amountitem
    useritems = Module1.CList(useritems).listloader(nameitem, amountitem, subtotalitem)

f=open("Receipt.txt", "a+")
f.write(Module1.CList(useritems).receipt())
f.write("total: " + str(round(Module1.CList(useritems).total(), 2)))
f.close()

