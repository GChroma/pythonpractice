class UItems:
    def __init__(self, name, amount, stotal):
        self.name = name
        self.amount = amount
        self.stotal = stotal


class CItems:
    def __init__(self, name, price, dprice):
        self.name = name
        self.price = price
        self.dprice = dprice


class CList:
    def __init__(self, list):
        self.list = list

    def total(self):
        sum = 0
        for x in self.list:
            sum += x.stotal
        return sum

    def display(self):
        for x in self.list:
            print("Item: " + str(x.name) + "\nPrice: " + str(x.price) +
                  "\nDiscount price(Zero means no discount): " + str(x.dprice) + "\n")

    def receipt(self):
        receiptstr = ""
        for x in self.list:
           receiptstr += "Name: " + x.name + " Amount: " + str(x.amount) + " Subtotal: $" + str(round(x.stotal, 2)) + "\n"
        return receiptstr

    def getprice(self, iname):
        counter = 0
        for x in self.list:
            if x.name == iname:
                if x.dprice == 0:
                    return float(x.price)
                else:
                    return float(x.dprice)
            counter += 1
            if counter == len(self.list):
                return 0

    def checkthrulist(self, iname):
        counter = 0
        if len(self.list) > 0:
            for x in self.list:
                counter += 1
                if x.name == iname:
                    return counter - 1
                elif counter == len(self.list):
                    return -1
        else:
            return -1

    def listloader(self, iname, iamount, istotal):
        check = CList(self.list).checkthrulist(iname)
        if check >= 0:
            self.list[check].amount += iamount
            self.list[check].stotal += istotal
            self.list[check].stotal == round(self.list[check].stotal, 2)   
        else:
            self.list.append(UItems(iname, iamount, round(istotal, 2)))
            return self.list
        return self.list
    