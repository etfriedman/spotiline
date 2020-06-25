#imports
import yfinance as yf

#Types of sites:
# Stock sites (yahoo finance
# add the stocks you want to watch
# - get a graph of investments?
# Movie review sites
# - get avg. review for a certain Movie

#website itself












#stock site (Yahoo API)
stocks = []

def newStock(stockName):
    stock = yf.Ticker(stockName)
    stocks.append(stockName)
def info(stock):
    infoType = input("What would you like to know about " + stock + "?" + "\nprice\nZip\n# Employees")
    if infoType == "price":
        return stock.info['ask']
        #elif:

# APPL = Stock('AAPL')
# APPL.info()
stocks = []

def newStock():
    stockChoice = input("What stock would you like to watch?\n> ")
    if stockChoice in stocks:
        return "You are already watching this stock!"
    else:
        stock = Stock(stockChoice)
        stocks.append(stock)
        print("Now watching your stock")

def checkStock(stock):
    if not stock in stocks:
        return "Please add this stock as a new stock!"
    else:
        stockIndex = stocks.index(stock)
        stock = stock[stockIndex]
        stock.info

while True:
    do = input("What would you like to do:\nCheck stock\nNew Stock\n> ")
    if do == "Check stock":
        print("Avalible Stocks:\n")
        for i in range(len(stocks)):
            print(stocks[i].name)
        checkStock(input("\n>"))

    elif do =="New Stock":
        newStock()
