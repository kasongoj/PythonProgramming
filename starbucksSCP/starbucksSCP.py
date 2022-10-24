"""
programmer: Joseph Kasongo
Program: Keeping track of starbucks supply chain management
first created: 10/21/2022 08:59 CST
last changed: 10/21/2022 08:59 CST
version: Python 3.10.7
"""

def espresso(quantity, coffee, water):
    """
    :param quantity: number of orders of espresso
    :param coffee: parameter keeping track of total coffee powder
    :param water: parameter keeping track of total water
    :return: updated resources after serving quantity*espresso servings
    """

    coffee = coffee - (quantity*8)
    water = water - (quantity*1.5)

def americano(quantity, size, coffee, water):
    """
    :americano mix: 1 shot of espresso and 3 oz of hot water
    :param quantity: number of orders of americano
    :param size: serving size (tall, grande, venti, trenta)
    :param coffee: parameter keeping track of total coffee powder
    :param water: parameter keeping track of total water
    :return: updated resources after serving quantity*size*americano servings
    """

    coffee = coffee - quantity*((size/4)*1)
    water =  water - quantity*((size/4)*3)

def cappuccino(quantity, size, coffee, milk):
    """
    :cappuccino mix: 2 shots of espresso + 4 oz. milk
    :param quantity: number of orders of americano
    :param size:
    :param coffee:
    :param milk:
    :return:
    """

    coffee = coffee - quantity*((size/6)*2)
    milk = milk - quantity*((size/6)*4)

def mocha(quantity, size, coffee, chocolate, milk, icecream):
    """
    :mocha mix: 1 shot of espresso + 1.5 oz. of chocolate + 2 oz. of milk + 2.5 cm of cream
    :param quantity:
    :param size:
    :param coffee:
    :param chocolate:
    :param milk:
    :return:
    """
    coffee = coffee - quantity*((size/7)*1)
    chocolate = chocolate - quantity*((size/7)*1.5)
    icecream = icecream - quantity*((size/7)*2.5)
    milk = milk - quantity*((size/7)*2)

def irish_coffee(quantity, size, coffee, whiskey, icecream):
    """
    : irish_coffee mix: 1.5 shot of espresso + 1 oz of whiskey + 1 oz of cream
    :param quantity:
    :param size:
    :param coffee:
    :param whiskey:
    :param icecream:
    :return:
    """
    coffee = coffee - quantity*((size/3.5)*1.5)
    whiskey = whiskey - quantity*((size/3.5)*1)
    icecream = icecream - quantity*((size/3.5)*1)

def affagato(quantity, size, coffee, icecream):
    """
    : affagato mix: 1.5 shots of espresso + 1 scoop of vanilla ice cream
    :param quantity:
    :param size:
    :param coffee:
    :param icecream:
    :return:
    """
    coffee = coffee - quantity*((size/2.5)*1.5)
    icecream = icecream - quantity*((size/2.5)*1)

def cafe_au_lait(quantity, size, coffee, milk):
    """
    : cafe_au_lait mix: 3 shots of French press coffee + 5 oz. scalded milk
    :param quantity:
    :param size:
    :param coffee:
    :param milk:
    :return:
    """

    coffee = coffee - quantity*((size/8)*3)
    milk = milk - quantity*((size/8)*5)

print("Program to keep track of starbucks supply chain management")
print("Enter the quantities of the raw materials at the beginning of the day")

# taking the input of the raw materials at the beginning of the page

coffee = float(input("Enter the coffee quantity:\t"))
milk = float(input("Enter the milk quantity:\t"))
water = float(input("Enter the water quantity:\t"))
icecream = float(input("Enter the icecream quantity:\t"))
chocolate = float(input("Enter the chocolate quantity:\t"))
whiskey = float(input("Enter the whiskey quantity:\t"))

# setting different serving size values
tall = 12
grande = 16
venti = 24
trenta = 31

espresso(2, coffee, water)
americano(2, venti, coffee, water)
cappuccino(2, grande, coffee, milk)
mocha(3, trenta, coffee, chocolate, milk, icecream)
irish_coffee(1, tall, coffee, whiskey, icecream)
affagato(4, venti, coffee, icecream)
cafe_au_lait(2, tall, coffee, milk)

print("Remaining supplies")
print("The leftover coffee powder is ", coffee)
print("The remaining water is ", water)

