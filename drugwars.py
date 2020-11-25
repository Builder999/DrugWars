from drugvariables import *
import random as rand
Win = False
def printPrices():
    print("Weed Price:",drugs.WeedPrice,"Available:", drugs.WeedInStore)
    print("Heroin Price:",drugs.HeroinPrice,"Available:", drugs.HeroinInStore)
    print("Cocaine Price:",drugs.CocainePrice,"Available:",drugs.CocaineInStore)
    print("Meth Price:",drugs.MethPrice,"Available:",drugs.MethInStore)
    print("MDMA Price:",drugs.MDMAPrice,"Available:",drugs.MDMAInStore)
    print("Lean Price:",drugs.LeanPrice,"Available:",drugs.LeanInStore)
    print("LSD Price:",drugs.LSDPrice,"Available:",drugs.ShroomsInStore)
    print("Shrooms Price:",drugs.ShroomsPrice,"Available:",drugs.ShroomsInStore)
def menu():
    selection = False
    while selection != True:
        keypressed = str(input("1 to buy, 2 to sell, 3 to display money, 4 to print prices, 5 to print your inventory, 6 to go on to next day: "))
        if keypressed == "1":
            print("Buying Drugs")
            buyingselection = str(input("1 For Weed, 2 for Heroin, 3 for Cocaine, 4 for meth, 5 for MDMA, 6 for Lean, 7 for LSD, 8 for Shrooms: "))
            if (buyingselection not in ["1","2","3","4","5","6","7","8"]):
                pass
            else:
                buying(buyingselection)
        elif keypressed == "2":
            print("Selling drugs")
            sellingselection = str(input("1 For Weed, 2 for Heroin, 3 for Cocaine, 4 for meth, 5 for MDMA, 6 for Lean, 7 for LSD, 8 for Shrooms: "))
            if (sellingselection not in ["1","2","3","4","5","6","7","8"]):
                pass
            else:
                selling(sellingselection)
        elif keypressed == "3":
            print("You have:",Inventory.Money,"Dollars")
        elif keypressed == "4":
            printPrices()
        elif keypressed == "5":
            print("Weed:",Inventory.Weed)
            print("Heroin:",Inventory.Heroin)
            print("Cocaine:",Inventory.Cocaine)
            print("Meth:",Inventory.Meth)
            print("MDMA:",Inventory.MDMA)
            print("Lean:",Inventory.Lean)
            print("LSD:",Inventory.LSD)
            print("Shrooms:",Inventory.Shrooms)
        elif keypressed == "6":
            selection = True




print("Welcome to drug wars! You goal is to become a drug kingpin!")
print("Remember, Buy Low Sell High")
input("Press Enter to continue...")
drugs.randomize()
while Win != True:
    printPrices()
    menu()
    if(Inventory.Money >= 1000000):
            print("You are the ultimate drug kingpin!")
            Win = True
    drugs.randomize()
