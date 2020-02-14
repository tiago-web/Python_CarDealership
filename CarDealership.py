'''
Name: Tiago Reis Espinola Soriano
This project is for a CarDealerShip company that store, delete, check or modify its cars stock.
'''

import datetime as d
def line():
    print("-"*50)

def centralize(item):
    line()
    print(item.center(50))
    line()

class Car:
    def __init__(self, make, model, purchase_price, sold_price, purchase_date, sold_date):
        self.__make = make
        self.__model = model
        self.__purchase_price = purchase_price
        self.__sold_price = sold_price
        self.__purchase_date = purchase_date
        self.__sold_date = sold_date

    def getMake(self):
        return self.__make

    def setMake(self,make):
        self.__make = make

    def getModel(self):
        return self.__model

    def setModel(self,model):
        self.__model = model

    def getPurchasePrice(self):
        return self.__purchase_price

    def setPurchasePrice(self, purchase_price):
        self.__purchase_price = purchase_price

    def getSoldPrice(self):
        return self.__sold_price

    def setSoldPrice(self, sold_price):
        self.__sold_price = sold_price

    def getPurchaseDate(self):
        return self.__purchase_date

    def setPurchaseDate(self,purchase_date):
        self.__purchase_date = purchase_date

    def getSoldDate(self):
        return self.__sold_date

    def setSoldDate(self, sold_date):
        self.__sold_date = sold_date


    def displayCars(self):
        result = "Make: " + str(self.__make) + "\n"
        result += "Model: " + str(self.__model) + "\n"
        result += "Purchase Date: " + self.__purchase_date.strftime("%x") + "\n"
        result += "Purchase Price: " + str(self.__purchase_price) + "\n"
        result += str('-'*50)
        return result

    def displaySoldCars(self):
        result = "Make: " + str(self.__make) + "\n"
        result += "Model: " + str(self.__model) + "\n"
        result += "Purchase Date: " + self.__purchase_date.strftime("%x") + "\n"
        result += "Purchase Price: " + str(self.__purchase_price) + "\n"
        result += "Sold Price: " + str(self.__sold_price) + "\n"
        result += "Sold Date: " + self.__sold_date.strftime("%x") + "\n"
        result += str('-'*50)
        return result

class Collection:
    def __init__(self):
        self.__carCollection = []
        self.__carSoldCollection = []

    def getCollection(self):
        return self.__carCollection

    def getSoldCollection(self):
        return self.__carSoldCollection

    def addSoldCar(self, car):
        self.__carSoldCollection.append(car)

    def addCar(self, car):
        self.__carCollection.append(car)

    def modifyCar(self,car, new_price): # if the staff wants to modify the price.
        if new_price > 0:
            car.setSoldPrice(new_price)
        else:
            pass

    def removeCar(self, car):
        self.__carSoldCollection.remove(car)

    def displayAllCars(self):
        allCars = "All cars in stock"
        centralize(allCars)
        for x in self.__carCollection:
            print(x.displayCars())

    def displayAllSoldCars(self):
        allSoldCars = "All cars sold by the store"
        centralize(allSoldCars)
        for x in self.__carSoldCollection:
            print(x.displaySoldCars())

class MainClass:
    def __init__(self):
        self.collection = Collection()

    def salesYear(self, y):  # Total sales for a year
        array = self.collection.getCollection()
        sales = 0
        for c in array:
            if int(c.getSoldDate().year) == y:
                sales += 1
        return sales

    def totalNetBenefit(self, y):  # Total net benefit for a year
        array = self.collection.getCollection()
        total = 0
        b = 0
        benefit = 0
        for c in array:
            if int(c.getSoldDate().year) == y:
                total += c.getSoldPrice()
                b += c.getPurchasePrice()
                benefit = total - b
        return benefit

    def carSoldMake(self, make):  # Total number of cars sold for a specific make
        array = self.collection.getCollection()
        total = 0
        for c in array:
            if c.getMake() == make:
                total += 1
        return total

    def carPurchasedMake(self, make):  # Total number of cars purchased for a specific make
        array = self.collection.getCollection()
        total = 0
        for c in array:
            if c.getMake() == make:
                total += 1
        return total

    def notSold(self):
        pass

class Input:
    def __init__(self):
        self.list = ["Add a car", "Sales per year", "Display the Profit per year", "Display Purchased cars per make",
                     "Display Sold cars per make", "Inventory", "Sell a car", "Modify a car price", "Display Cars sold", "Exit Program"]

    def main(self):
        m = "MAIN CONTENT"
        centralize(m)
        counter = 1
        for x in self.list:
            print(counter, "-", x)
            counter += 1
        line()

    def option(self):
        m = MainClass()
        c = m.collection
        opt = True
        while opt:
            Input.main(self)
            n = int(input("Please choose an option: "))
            ci = True
            if n == 1:
                while ci:
                    add = "ADD A CAR"
                    centralize(add)
                    make = str(input("Please, enter car make: "))
                    model = str(input("Please, enter car model: "))
                    pp = int(input("Please, enter purchase price: "))
                    #sp = int(input("Please, enter sold price: "))
                    pdy = int(input("Please, enter purchase year: "))
                    pdm = int(input("Please, enter purchase month: ").lstrip('0'))
                    pdd = int(input("Please, enter purchase day: ").lstrip('0'))
                    #sdy = int(input("Please, enter sold year: "))
                    #sdm = int(input("Please, enter sold month: ").lstrip('0'))
                    #sdd = int(input("Please, enter sold day: ").lstrip('0'))

                    car = Car(make, model, pp, '', d.date(pdy, pdm, pdd), '')

                    c.addCar(car)
                    line()
                    f = str(input("Do you want to add another car? yes or no. "))
                    if f == 'no':
                        ci = False
                line()
                ask = str(input("Do you want to do select another action? yes or no. "))
                if ask == 'no':
                    print("Thank you for using my program!")
                    opt = False

            elif n == 2:
                sales = "SALES PER YEAR"
                centralize(sales)
                year = int(input("Please enter the year that you want to check the number of sales: "))
                print(m.salesYear(year))
                line()
                ask = str(input("Do you want to do select another action? yes or no. "))
                if ask == 'no':
                    print("Thank you for using my program!")
                    opt = False
            elif n == 3:
                profit = "PROFIT PER YEAR"
                centralize(profit)
                year = int(input("Please enter the year that you want to check the profit: "))
                print(m.totalNetBenefit(year))
                line()
                ask = str(input("Do you want to do select another action? yes or no. "))
                if ask == 'no':
                    print("Thank you for using my program!")
                    opt = False
            elif n == 4:
                pass
            elif n == 5:
                pass
            elif n == 6:
                c.displayAllCars()
            elif n == 7:
                while ci:
                    rcar = "SELL A CAR"
                    centralize(rcar)
                    make = str(input("Please, enter car make: "))
                    model = str(input("Please, enter car model: "))
                    pp = int(input("Please, enter purchase price: "))
                    sp = int(input("Please, enter sold price: "))
                    pdy = int(input("Please, enter purchase year: "))
                    pdm = int(input("Please, enter purchase month: ").lstrip('0'))
                    pdd = int(input("Please, enter purchase day: ").lstrip('0'))
                    sdy = int(input("Please, enter sold year: "))
                    sdm = int(input("Please, enter sold month: ").lstrip('0'))
                    sdd = int(input("Please, enter sold day: ").lstrip('0'))

                    car = Car(make, model, pp, '', d.date(pdy, pdm, pdd), '') #  I can not get the make of this car because it is not added
                    carSold = Car(make, model, pp, sp, d.date(pdy, pdm, pdd), d.date(sdy, sdm, sdd))
                    # print(Car.getMake(car))
                    # for x in Collection().getCollection():
                    #     print("This is in the array ",Car.getMake(x))


                    c.removeCar(car)
                    c.addSoldCar(carSold)
                    line()

                    f = str(input("Do you want to sell another car? yes or no. "))
                    if f == 'no':
                        ci = False
                line()
                ask = str(input("Do you want to do select another action? yes or no. "))
                if ask == 'no':
                    print("Thank you for using my program!")
                    opt = False

            elif n == 8:
                pass
            elif n == 9:
                c.displayAllSoldCars()
            elif n == 10:
                pass

Input().option()

