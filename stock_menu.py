# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 22:57:11 2021

@author: D99003734
"""
from datetime import datetime
from stock_class import Stock, DailyData
from account_class import  Traditional, Robo
import matplotlib.pyplot as plt
import json
import csv
from utilities import clear_screen, display_stock_chart



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
    
def investment_type(stock_list):
    print("Investment Account ---")
    balance = float(input("What is your initial balance: "))
    number = input("What is your account number: ")
    acct= input("Do you want a Traditional (t) or Robo (r) account: ")
    if acct.lower() == "r":
        years = float(input("How many years until retirement: "))
        robo_acct = Robo(balance, number, years)
        print("Your investment return is ",robo_acct.investment_return())
        print("\n\n")
    elif acct.lower() == "t":
        trad_acct = Traditional(balance, number)
        temp_list=[]
        print("Choose stocks from the list below: ")
        while True:
            print("Stock List: [",end="")
            for stock in stock_list:
                print(stock.symbol," ",end="")
            print("]")
            symbol = input("Which stock do you want to purchase, 0 to quit: ").upper()
            if symbol =="0":
                break
            shares = float(input("How many shares do you want to buy?: "))
            found = False
            for stock in stock_list:
              if stock.symbol == symbol:
                  found = True
                  current_stock = stock
            if found == True:
                current_stock.buy(shares)
                temp_list.append(current_stock)
                print("Bought ",shares,"of",symbol)
            else:
                print("Symbol Not Found ***")
        trad_acct.add_stock(temp_list)

# Function to create stock chart
def display_stock_chart(stock_list,symbol):
    print("This method is under construction")

# Display Chart
def display_chart(stock_list):
    print("This method is under construction")
  

    
#object encoder and decoder pasted here

def file_processing(stock_list):
    print("This method is under construction")
  
   

                
 # Get price and volume history from Yahoo! Finance using CSV import.
def import_stock_csv(stock_list,symbol,filename):
    print("This method is under construction")
    
   # Display Report 
def display_report(stock_list,symbol):
    clear_screen()
    print("Stock Report ----")
    for stock in stock_list:
        print("Report for: ", stock.symbol, " ", stock.name)
        print("Shares: ", stock.shares)
        count = 0
        price_total = 0
        volume_total = 0
        lowPrice = 999999.99
        highPrice = 0
        lowVolume = 999999999999
        highVolume = 0
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
    
def main_menu(stock_list):
    option = ""
    while True:
        print("Stock Analyzer ---")
        print("1 - Add Stock")
        print("2 - Delete Stock")
        print("3 - List stocks")
        print("4 - Add Daily Stock Data (Date, Price, Volume)")
        print("5 - Show Chart")
        print("6 - Investor Type")
        print("7 - Save/Load Data")
        print("0 - Exit Program")
        option = input("Enter Menu Option: ")
        if option =="0":
            print("Goodbye")
            break
        
        if option == "1":
            add_stock(stock_list)
        elif option == "2":
            delete_stock(stock_list)
        elif option == "3":
            list_stocks(stock_list)
        elif option == "4":
           add_stock_data(stock_list) 
        elif option == "5":
            display_chart(stock_list)
        elif option == "6":
            investment_type(stock_list)
        elif option == "7":
            file_processing(stock_list)
        else:
            
            print("Goodbye")

# Begin program
def main():
    stock_list = []
    main_menu(stock_list)

# Program Starts Here
if __name__ == "__main__":
    # execute only if run as a stand-alone script
    main()