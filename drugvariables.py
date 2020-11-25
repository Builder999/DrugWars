import random as rand
# drug lists Heroin, cocaine, meth, MDMA, lean, LSD, shrooms
class drugs:
        WeedPrice = 30
        WeedInStore = 1
        HeroinPrice = 100
        HeroinInStore = 1
        CocainePrice = 50
        CocaineInStore = 1
        MethPrice = 75
        MethInStore =  1
        MDMAPrice = 40
        MDMAInStore  = 1
        LeanPrice = 5
        LeanInStore = 1
        LSDPrice = 40
        LSDInStore  = 1
        ShroomsPrice = 20
        ShroomsInStore = 1
        def randomize():
            drugs.WeedPrice = rand.randint(30, 120)
            drugs.WeedInStore = rand.randint(0, 25)
            drugs.HeroinPrice = rand.randint(100, 300)
            drugs.HeroinInStore = rand.randint(0,25)
            drugs.CocainePrice = rand.randint(50,200)
            drugs.CocaineInStore = rand.randint(0, 25)
            drugs.MethPrice = rand.randint(75, 375)
            drugs.MethInStore =  rand.randint(0, 25)
            drugs.MDMAPrice = rand.randint(40, 160)
            drugs.MDMAInStore  = rand.randint(0, 25)
            drugs.LeanPrice = rand.randint(5, 75)
            drugs.LeanInStore = rand.randint(0, 25)
            drugs.LSDPrice = rand.randint(40, 140)
            drugs.LSDInStore  = rand.randint(0, 25)
            drugs.ShroomsPrice = rand.randint(20, 80)
            drugs.ShroomsInStore = rand.randint(0, 25)
class Inventory:
    Money = 400
    Weed = 0
    Heroin = 0
    Cocaine = 0
    Meth = 0
    MDMA = 0
    Lean = 0
    LSD = 0
    Shrooms = 0

def buying(drug):
    print("buying")
    done = False
    while done == False:
        if drug == "1":
            amount = input("How much weed do you want? ")
            try:
                amount = int(amount)
                if amount > drugs.WeedInStore:
                    print("not enough Stock")
                elif (amount * drugs.WeedPrice > Inventory.Money):
                    print("not enough money")
                else:
                    Inventory.Money = Inventory.Money - amount * drugs.WeedPrice
                    Inventory.Weed += amount
                    drugs.WeedInStore = drugs.WeedInStore - amount
                    done = True
            except:
                print("must type number")
        elif drug == "2":
            amount = input("How much Heroin do you want? ")
            try:
                amount = int(amount)
                if amount > drugs.HeroinInStore:
                    print("not enough Stock")
                elif (amount * drugs.HeroinPrice > Inventory.Money):
                    print("not enough money")
                else:
                    Inventory.Money = Inventory.Money - amount * drugs.HeroinPrice
                    drugs.HeroinInStore = drugs.HeroinInStore - amount
                    Inventory.Heroin += amount
                    done = True
            except:
                print("must type number")
        elif drug == "3":
            amount = input("How much Cocaine do you want? ")
            try:
                amount = int(amount)
                if amount > drugs.CocaineInStore:
                    print("not enough Stock")
                elif (amount * drugs.CocainePrice > Inventory.Money):
                    print("not enough money")
                else:
                    Inventory.Money = Inventory.Money - amount * drugs.CocainePrice
                    drugs.CocaineInStore = drugs.CocaineInStore - amount
                    Inventory.Cocaine += amount
                    done = True
            except:
                print("must type number")
        elif drug == "4":
            amount = input("How much Meth do you want? ")
            try:
                amount = int(amount)
                if amount > drugs.MethInStore:
                    print("not enough Stock")
                elif (amount * drugs.MethPrice > Inventory.Money):
                    print("not enough money")
                else:
                    Inventory.Money = Inventory.Money - amount * drugs.MethPrice
                    drugs.MethInStore = drugs.MethInStore - amount
                    Inventory.Meth += amount
                    done = True
            except:
                print("must type number")
        elif drug == "5":

            amount = input("How much MDMA do you want? ")
            try:
                amount = int(amount)
                if amount > drugs.MDMAInStore:
                    print("not enough Stock")
                elif (amount * drugs.MDMAPrice > Inventory.Money):
                    print("not enough money")
                else:
                    Inventory.Money = Inventory.Money - amount * drugs.MDMAPrice
                    drugs.MDMAInStore = drugs.MDMAInStore - amount
                    Inventory.MDMA += amount
                    done = True
            except:
                print("must type number")
        elif drug == "6":

            amount = input("How much Lean do you want? ")
            try:
                amount = int(amount)
                if amount > drugs.LeanInStore:
                    print("not enough Stock")
                elif (amount * drugs.LeanPrice > Inventory.Money):
                    print("not enough money")
                else:
                    Inventory.Money = Inventory.Money - amount * drugs.LeanPrice
                    drugs.LeanInStore = drugs.LeanInStore - amount
                    Inventory.Lean += amount
                    done = True
            except:
                print("must type number")
        elif drug == "7":

            amount = input("How much LSD do you want? ")
            try:
                amount = int(amount)
                if amount > drugs.LSDInStore:
                    print("not enough Stock")
                elif (amount * drugs.LSDPrice > Inventory.Money):
                    print("not enough money")
                else:
                    Inventory.Money = Inventory.Money - amount * drugs.LSDPrice
                    drugs.LSDInStore = drugs.LSDInStore - amount
                    Inventory.LSD += amount
                    done = True
            except:
                print("must type number")
        elif drug == "8":

            amount = input("How much Shrooms do you want? ")
            try:
                amount = int(amount)
                if amount > drugs.ShroomsInStore:
                    print("not enough Stock")
                elif (amount * drugs.ShroomsPrice > Inventory.Money):
                    print("not enough money")
                else:
                    Inventory.Money = Inventory.Money - amount * drugs.ShroomsPrice
                    drugs.ShroomsInStore = drugs.ShroomsInStore - amount
                    Inventory.Shrooms += amount
                    done = True
            except:
                print("must type number")
def selling(drug):
    done = False
    while done == False:
        if drug == "1":
            amount = input("How much weed do you want to sell? ")
            try:
                amount = int(amount)
                if amount > Inventory.Weed:
                    print("Not Enough Weed")
                else:
                    Inventory.Weed = Inventory.Weed - amount
                    Inventory.Money = Inventory.Money + amount * drugs.WeedPrice
                    done = True
            except:
                print("Please input valid number")
        elif drug == "2":
            amount = input("How much Heroin do you want to sell? ")
            try:
                amount = int(amount)
                if amount > Inventory.Heroin:
                    print("Not Enough Heroin")
                else:
                    Inventory.Heroin = Inventory.Heroin - amount
                    Inventory.Money = Inventory.Money + amount * drugs.HeroinPrice
                    done = True
            except:
                print("Please input valid number")
        elif drug == "3":
            amount = input("How much Cocaine do you want to sell? ")
            try:
                amount = int(amount)
                if amount > Inventory.Cocaine:
                    print("Not Enough Cocaine")
                else:
                    Inventory.Cocaine = Inventory.Cocaine - amount
                    Inventory.Money = Inventory.Money + amount * drugs.CocainePrice
                    done = True
            except:
                print("Please input valid number")
        elif drug == "4":
            amount = input("How much Meth do you want to sell? ")
            try:
                amount = int(amount)
                if amount > Inventory.Meth:
                    print("Not Enough Meth")
                else:
                    Inventory.Meth = Inventory.Meth - amount
                    Inventory.Money = Inventory.Money + amount * drugs.MethPrice
                    done = True
            except:
                print("Please input valid number")
        elif drug == "5":
            amount = input("How much MDMA do you want to sell? ")
            try:
                amount = int(amount)
                if amount > Inventory.MDMA:
                    print("Not Enough MDMA")
                else:
                    Inventory.MDMA = Inventory.MDMA - amount
                    Inventory.Money = Inventory.Money + amount * drugs.MDMAPrice
                    done = True
            except:
                print("Please input valid number")
        elif drug == "6":
            amount = input("How much Lean do you want to sell? ")
            try:
                amount = int(amount)
                if amount > Inventory.Lean:
                    print("Not Enough Lean")
                else:
                    Inventory.Lean = Inventory.Lean - amount
                    Inventory.Money = Inventory.Money + amount * drugs.LeanPrice
                    done = True
            except:
                print("Please input valid number")
        elif drug == "7":
            amount = input("How much LSD do you want to sell? ")
            try:
                amount = int(amount)
                if amount > Inventory.LSD:
                    print("Not Enough LSD")
                else:
                    Inventory.LSD = Inventory.LSD - amount
                    Inventory.Money = Inventory.Money + amount * drugs.LSDPrice
                    done = True
            except:
                print("Please input valid number")
        elif drug == "8":
            amount = input("How much Shrooms do you want to sell? ")
            try:
                amount = int(amount)
                if amount > Inventory.Shrooms:
                    print("Not Enough Shrooms")
                else:
                    Inventory.Shrooms = Inventory.Shrooms - amount
                    Inventory.Money = Inventory.Money + amount * drugs.ShroomsPrice
                    done = True
            except:
                print("Please input valid number")
