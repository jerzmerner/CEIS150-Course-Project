# Summary: This module contains the user interface and logic for a console-based version of the stock manager program.
# Author: 1
# Date: 

from datetime import datetime
from stock_class import Stock, DailyData
from utilities import clear_screen
from os import path
import stock_data
from stock_menu import display_stock_chart

#Setup matplotlib for Ubuntu 21.10
#matplotlib.use('Qt5Agg')


# Main Menu
def main_menu(stock_list):
    option = ""
    while option != "0":
        clear_screen()
        print("Stock Analyzer ---")
        print("1 - Manage Stocks (Add, Update, Delete, List)")
        print("2 - Add Daily Stock Data (Date, Price, Volume)")
        print("3 - Show Report")
        print("4 - Show Chart")
        print("5 - Manage Data (Save, Load, Retrieve)")
        print("0 - Exit Program")
        option = input("Enter Menu Option: ")
        while option not in ["1","2","3","4","5","0"]:
            clear_screen()
            print("*** Invalid Option - Try again ***")
            print("Stock Analyzer ---")
            print("1 - Manage Stocks (Add, Update, Delete, List)")
            print("2 - Add Daily Stock Data (Date, Price, Volume)")
            print("3 - Show Report")
            print("4 - Show Chart")
            print("5 - Manage Data (Save, Load, Retrieve)")
            print("0 - Exit Program")
            option = input("Enter Menu Option: ")
        if option == "1":
            manage_stocks(stock_list)
        elif option == "2":
            add_stock_data(stock_list)
        elif option == "3":
            display_report(stock_list)
        elif option == "4":
            display_chart(stock_list)
        elif option == "5":
            manage_data(stock_list)
        else:
            clear_screen()
            print("Goodbye")

# Manage Stocks
def manage_stocks(stock_list):
    option = ""
    while option != "0":
        clear_screen()
        print("Manage Stocks ---")
        print("1 - Add Stock")
        print("2 - Update Shares")
        print("3 - Delete Stock")
        print("4 - List Stocks")
        print("0 - Exit Manage Stocks")
        option = input("Enter Menu Option: ")
        while option not in ["1","2","3","4","0"]:
            clear_screen()
            print("*** Invalid Option - Try again ***")
            print("1 - Add Stock")
            print("2 - Update Shares")
            print("3 - Delete Stock")
            print("4 - List Stocks")
            print("0 - Exit Manage Stocks")
            option = input("Enter Menu Option: ")
        if option == "1":
            add_stock(stock_list)
        elif option == "2":
            update_shares(stock_list)
        elif option == "3":
            delete_stock(stock_list)
        elif option == "4":
            list_stocks(stock_list)
        else:
            print("Returning to Main Menu")

# Add new stock to track
def add_stock(stock_list):
    option = ""
    while option != "0":
        clear_screen()
        print("Add stock ---")
        symbol = str(input("Enter Ticker Symbol: "))
        name = str(input("Enter Company Name: "))
        shares = float(input("Enter Number of Shares: "))
        new_stock = Stock(symbol.upper(), name,shares)
        stock_list.append(new_stock)
        option = input("Stock Added - Enter to Add Another Stock or 0 to Stop: ")

# Buy or Sell Shares Menu
def update_shares(stock_list):
    option = ""
    while option != "0":
        clear_screen()
        print("Update Shares ---")
        print("1 - Buy Shares")
        print("2 - Sell Shares")
        print("0 - Exit Update Shares")
        option = input("Enter Menu Option: ")
        while option not in ["1","2","0"]:
            clear_screen()
            print("*** Invalid Option - Try again ***")
            print("Update Shares ---")
            print("1 - Buy Shares")
            print("2 - Sell Shares")
            print("0 - Exit Update Shares")
            option = input("Enter Menu Option: ")
        if option == "1":
            buy_stock(stock_list)
        elif option == "2":
            sell_stock(stock_list)
        elif option == "0":
            print("Returning to Main Menu")

# Buy Stocks (add to shares)
def buy_stock(stock_list):
    clear_screen()
    print("Buy Shares ----")
    print("Stock List: [", end=" ")
    for stock in stock_list:
        print(stock.symbol, end=" ")
    print("")
    symbol = str(input("Which stock do you want to buy?: "))
    symbol = symbol.upper()
    shares = float(input("How many shares do you want to buy?: "))
    found = False
    for stock in stock_list:
        if stock.symbol == symbol:
            found = True
            Stock.buy(shares)
            print("Bought ", shares, " of ", symbol)
    if found == False:
        print("Error: ", symbol, " not found!")
    _ = input("*** Press Enter to Continue **1*")

# Sell Stocks (subtract from shares)
def sell_stock(stock_list):
    clear_screen()
    print("Sell Shares ----")
    print("Stock List: [", end=" ")
    for stock in stock_list:
        print(stock.symbol, end=" ")
    print("")
    symbol = str(input("Which stock do you want to sell?: "))
    symbol = symbol.upper()
    shares = float(input("How many shares do you want to sell?: "))
    found = False
    for stock in stock_list:
        if stock.symbol == symbol:
            found = True
            Stock.sell(shares)
            print("Sold ", shares, " of ", symbol)
    if found == False:
        print("Error: ", symbol, " not found!")
    _ = input("*** Press Enter to Continue ***")

# Remove stock and all daily data
def delete_stock(stock_list):
    clear_screen()
    print("Delete Stock ----")
    print("Stock List: [", end=" ")
    for stock in stock_list:
        print(stock.symbol, end=" ")
    print("")
    symbol = str(input("Which stock do you want to delete?: "))
    symbol = symbol.upper()
    found = False
    i = 0
    for stock in stock_list:
        if stock.symbol == symbol:
            found = True
            stock_list.pop(i)
            print("Deleted ", symbol)
        i += 1
    if found == False:
        print("Error: ", symbol, " not found!")
    _ = input("*** Press Enter to Continue ***")

# List stocks being tracked
def list_stocks(stock_list):
    clear_screen()
    print("Stock List ----")
    print("SYMBOL          NAME            SHARES")
    print("======================================")
    for stock in stock_list:
        print(stock.symbol," " * (14-len(stock.symbol)),stock.name," " * (14-len(stock.name)),stock.shares)
    _ = input("*** Press Enter to Continue ***")

# Add Daily Stock Data
def add_stock_data(stock_list):
    clear_screen()
    print("Add Daily Stock Data ----")
    print("Stock List: [", end=" ")
    for stock in stock_list:
        print(stock.symbol, end=" ")
    print("]")
    symbol = str(input("Which stock do you want to use?: "))
    symbol = symbol.upper()
    found = False
    for stock in stock_list:
        if stock.symbol == symbol:
            found = True
            current_stock = stock
    if found == True:
        print("Ready to add data for: ", symbol)
        print("Enter Data Separated by Commas - Do Not Use Spaces")
        print("Enter a blank line to quit")
        print("Enter Date,Price,Volume")
        print("Example: 1/16/22,32.5,10055")
        data = input("Enter Date,Price,Volume: ")
        while data != "":
            date, price, volume = data.split(",")
            daily_data = DailyData(datetime.strptime(date,"%m/%d/%y"),float(price),float(volume))
            current_stock.add_data(daily_data)
            data = input("Enter Date,Price,Volume: ")
        print("Data Entry Complete")
    else:
        print("Error: ", symbol, " not found!")      
    _ = input("*** Press Enter to Continue ***")

# Display Report for All Stocks
def display_report(stock_data):
    clear_screen()
    print("Stock Report ----")
    for stock in stock_data:
        print("Report for: ", stock.symbol, " ", stock.name)
        print("Shares: ", stock.shares)
        count = 0
        price_total = 0.00
        volume_total = 0
        lowPrice = 999999.99
        highPrice = 0.00
        lowVolume = 999999999999
        highVolume = 0.00
        startDate = datetime.strptime("12/31/2099","%m/%d/%Y")
        endDate = datetime.strptime("1/1/1900","%m/%d/%Y")
        for daily_data in stock.DataList:
            count += 1
            price_total += daily_data.close
            volume_total += daily_data.volume
            if daily_data.close < lowPrice:
                lowPrice = daily_data.close
            if daily_data.close > highPrice:
                highPrice = daily_data.close
            if daily_data.volume < lowVolume:
                lowVolume = daily_data.volume
            if daily_data.volume > highVolume:
                highVolume = daily_data.volume
            if daily_data.date < startDate:
                startDate = daily_data.date
                startPrice = daily_data.close
            if daily_data.date > endDate:
                endDate = daily_data.date
                endPrice = daily_data.close
            priceChange = endPrice - startPrice
            print(daily_data.date.strftime("%m/%d/%y"),daily_data.close,daily_data.volume)
        if count > 0:
            print("Summary ---", startDate.strftime("%m/%d/%y"), " to ", endDate.strftime("%m/%d/%y"))
            print("Low Price: ${:,.2f}".format(lowPrice))
            print("High Price: ${:,.2f}".format(highPrice))
            print("Average Price: ${:,.2f}".format(price_total / count))
            print("Low Volume: ", lowVolume)
            print("High Volume: ", highVolume)
            print("Average Volume: ", volume_total / count)
            print("Starting Price: ${:,.2f}".format(startPrice))
            print("Ending Price: ${:,.2f}".format(endPrice))
            print("Change in Price: ${:,.2f}".format(priceChange))
            print("Profit/Loss: ${:,.2f}".format(priceChange * stock.shares))
        else:
            print("No Daily History")
        print("")
        print("======================================")
        print("")
    print("Report Complete")
    _ = input("*** Press Enter to Continue ***")

# Display Chart
def display_chart(stock_list):
    clear_screen()
    print("Stock Chart ----")
    print("Stock List: [", end=" ")
    for stock in stock_list:
        print(stock.symbol, end=" ")
    print("]")
    symbol = str(input("Which stock do you want to chart?: "))
    symbol = symbol.upper()
    found = False
    for stock in stock_list:
        if stock.symbol == symbol:
            found = True
    if found == True:
       display_stock_chart(stock_list, symbol)
       print("Plot created for {}".format(symbol))
    else:
        print("Error: ", symbol, " not found!")      
    _ = input("*** Press Enter to Continue ***")
    
                
# Manage Data Menu
def manage_data(stock_list):
    option = ""
    while option != "0":
        clear_screen()
        print("Manage Data ---")
        print("1 - Save Data to Database")
        print("2 - Load Data from Database")
        print("3 - Retrieve Data from Web")
        print("4 - Import from CSV File")
        print("0 - Exit Manage Data")
        option = input("Enter Menu Option: ")
        while option not in ["1","2","3","4","5","0"]:
            clear_screen()
            print("*** Invalid Option - Try again ***")
            print("1 - Save Data to Database")
            print("2 - Load Data from Database")
            print("3 - Retrieve Data from Web")
            print("4 - Import from CSV File")
            print("0 - Exit Manage Data")
            option = input("Enter Menu Option: ")
        if option == "1":
            stock_data.save_stock_data(stock_list)
            print("--- Data Saved to Database ---")
            _ = input("Press Enter to Continue")
        elif option == "2":
            stock_data.load_stock_data(stock_list)
            print("--- Data Loaded from Database ---")
            _ = input("Press Enter to Continue")
        elif option == "3":
            retrieve_from_web(stock_list)
            print("--- Data Retrieved from Yahoo! Finance ---")
            _ = input("Press Enter to Continue")
        elif option == "4":
            import_csv(stock_list)
        else:
            print("Returning to Main Menu")

# Get stock price and volume history from Yahoo! Finance using Web Scraping
def retrieve_from_web(stock_list):
    clear_screen()
    print("*** This Module Under Construction ***")
    _ = input("*** Press Enter to Continue ***")

# Import stock price and volume history from Yahoo! Finance using CSV Import
def import_csv(stock_list):
    clear_screen()
    print("*** This Module Under Construction ***")
    _ = input("*** Press Enter to Continue ***")

# Begin program
def main():
    #check for database, create if not exists
    if path.exists("stocks.db") == False:
        stock_data.create_database()
    stock_list = []
    main_menu(stock_list)

# Program Starts Here
if __name__ == "__main__":
    # execute only if run as a stand-alone script
    main()
