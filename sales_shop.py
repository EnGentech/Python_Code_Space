import os
import sys
import time


class sales_shop:
    lis = ["Meat_pie", "Juice", "Ice_cream", "All"]
    bullet = str([1, 2, 3])
    option = ["Query"]
    sizes = ["Small-size", "Medium-size"]
    picked_size = ""

    def __int__(self):
        self.ss = ""
        self.ms = ""
        self.qty_ms = ""
        self.qty_ss = ""

    def Ice_cream(self):
        self.ss = 500
        self.ms = 1500
        self.qty_ss = 24
        self.qty_ms = 52

    def Meat_pie(self):
        self.ss = 250
        self.ms = 420
        self.qty_ss = 380
        self.qty_ms = 420

    def Juice(self):
        self.ss = 850
        self.ms = 1250
        self.qty_ss = 530
        self.qty_ms = 578

    def Querry(self, prod):
        ju = sales_shop()
        ju.Juice()
        mit = sales_shop()
        mit.Meat_pie()
        ice = sales_shop()
        ice.Ice_cream()

        dic = {"Ice_cream": [ice.qty_ss, ice.qty_ms],
               "Meat_pie": [mit.qty_ss, mit.qty_ms],
               "Juice": [ju.qty_ss, ju.qty_ms]
               }

        if prod == "All":
            for keys, values in dic.items():
                print("{} remains: Small size {}, Medium size {}".format(keys, values[0], values[1]))
            print("")
            print("======= Enter new command =======")
        elif not prod or prod not in dic:
            print("Invalid Query option")
        else:
            for keys, values in dic.items():
                if prod == keys:
                    for i in range(len(values)):
                        while i == 0:
                            print("Small-size remains {}.".format(values[0]))
                            break
                        while i == 1:
                            print("Medium-size remains {}.\n".format(values[1]))
                            print("======= Enter new command =======")
                            break


def rem(inp):
    b = sales_shop()
    b.Querry(inp.capitalize())


def check(*args):
    if args[0].capitalize() in sales_shop().option:
        if len(args) > 1:
            if args[1].capitalize() in sales_shop().lis:
                rem(args[1])
            else:
                loop_product(args[1])
        else:
            print("No product selected")
            new = input("Command$ ")
            new = new.split()
            if len(new) > 1:
                check(new[0], new[1])
            else:
                check(new[0])
    else:
        loop(args[0])


def loop(valid):
    if valid.capitalize() == "Quit":
        sys.exit()
    elif valid.capitalize() not in sales_shop().option:
        print("Invalid Command, try again:")
        new = input("Command$ ")
        new = new.split()
        if new[0].capitalize() == "Quit":
            sys.exit()
        if len(new) > 1:
            check(new[0], new[1])
        else:
            check(new[0])


def loop_product(prd):
    if prd.capitalize() not in sales_shop().lis:
        print("Invalid Product, try again:")
        new = input("Command$ ")
        new = new.split()
        if new[0].capitalize() == "Quit":
            sys.exit()
        if len(new) > 1:
            check(new[0], new[1])
        else:
            check(new[0])


def size():
    print("\n=== Great Choice, Please Select your Size ===\nWe have:")
    cun = 1
    amt = sales_shop()
    if commodity in amt.bullet:
        pos = amt.lis[int(commodity)-1]
    else:
        pos = commodity
    getattr(amt, pos.capitalize())()
    selling_price_ss = getattr(amt, 'ss')
    selling_price_ms = getattr(amt, 'ms')
    prices = [selling_price_ss, selling_price_ms]
    for itms in sales_shop().sizes:
        print("{}. {} @ {} each".format(cun, itms, prices[cun - 1]))
        cun = cun + 1
    store = test()
    return store


def test():
    try:
        siz = int(input("Size$ "))
        if 1 <= siz <= len(sales_shop().sizes):
            return siz
            pass
        elif siz > len(sales_shop().sizes):
            print("Size exceeded, retry")
            test()
    except ValueError:
        print("Only Integers are allowed, retry")
        siz = test()
        return siz


def yes_or_no():
    y_n = input("Option$ ")
    if y_n.capitalize() == "Yes" or y_n.capitalize() == 'No':
        return y_n
    else:
        while True:
            print("\t== Invalid Choice ==")
            chk = yes_or_no()
            return chk


def customer(customer_choice):
    storage_result = size()
    print("\n=== Nice Option ===\nPlease enter your desired Quantity")
    quantity = qty()
    a = sales_shop()
    if customer_choice in a.bullet:
        pos = a.lis[int(customer_choice)-1]
    else:
        pos = customer_choice
    getattr(a, pos.capitalize())()
    ms = getattr(a, 'qty_ms')
    ss = getattr(a, 'qty_ss')
    ss_amount = getattr(a, 'ss')
    ms_amount = getattr(a, 'ms')
    if storage_result == 1:
        xs = ss
        amount_each = ss_amount
        xs_amount = quantity * ss_amount
    else:
        xs = ms
        amount_each = ms_amount
        xs_amount = quantity * ms_amount

    while True:
        if quantity >= xs:
            print("\n=== Sorry We dont have the amount you require, could you please reduce the quantity? ===")
            print("\tWe are left with {} items under this selection...".format(xs))
            print("== Please choose Yes or No ==")
            y_n = yes_or_no()
            if y_n.capitalize() == "Yes":
                customer(customer_choice)
            elif y_n.capitalize() == "No":
                print("\n=== Hope to satisfy you soon ===\n\t\t== Good-Bye ==")
                sys.exit()
        else:
            print("\n== Thank you for your patronage ==")
            print("Each of this product cost: {}".format(amount_each))
            print("== Total Cost: {}".format(xs_amount))
            print("\n== Do you wish to proceed to payment, Enter Yes or No ==")
            proceed = yes_or_no()
            if proceed.capitalize() == "Yes":
                payment()
            elif proceed.capitalize() == "No":
                print("\n== Do you wish to reduce your quantity, Enter yes or no ==")
                reduction = yes_or_no()
                if reduction.capitalize() == "Yes":
                    customer(customer_choice)
                elif reduction.capitalize() == "No":
                    print("\n=== Hope to satisfy you soon ===\n\t\t== Good-Bye ==")
                    sys.exit()


def qty():
    try:
        quantity = int(input("Qty$ "))
        return quantity
    except ValueError:
        print("Only Integers are allowed")
        quantity = qty()
        return quantity


def payment():
    print("\n=== Thank you for choosing EnGentech ===")
    print("Please wait for your receipt")
    print("=== Processing, please wait... ===")
    time.sleep(10)
    print("\n         =======Thank you for your patience=======")
    print("Please proceed to the Carbin for your payment with the receipt ")
    print("== Do you wish to perform additional transaction, select yes or no ==")
    adds = yes_or_no()
    if adds.capitalize() == "Yes":
        shopping()
    else:
        print("===\n Thank you for having me assist you, BYE ===")
        sys.exit()


def shopping():
    print("\n========== Welcome to your Service assistance ==========")
    print("Select 1 if you are a customer, or 2 if you are a seller\t")
    quad = input("Selection$ ")
    if quad == "2":
        print("\nEnter Query to query products or Quit to terminate CLI\ne.g Query Juice\n")

    while True:
        if quad == "1":
            count = 1
            print("\n=== Welcome Customer ===\nOur Products include:")
            for i in sales_shop().lis:
                if i == "All":
                    continue
                print("{}. {}".format(count, i))
                count = count + 1
            global commodity
            commodity = input("Choice$ ")
            while True:
                if commodity.capitalize() in sales_shop().lis or commodity in sales_shop().bullet:
                    customer(commodity)
                else:
                    print("=== Product not available, retry ===")
                    commodity = input("Choice$ ")

        elif quad == "2":
            print("=== Welcome Seller ===")
            command = input("Command$ ")
            arg = command.split(" ")
            if arg[0].capitalize() == "Quit":
                sys.exit()
            elif len(arg) > 1:
                check(arg[0], arg[1])
            else:
                check(arg[0])
        else:
            quad = input("Invalid selection, try again: ")


shopping()