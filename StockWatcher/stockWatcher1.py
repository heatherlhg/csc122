import sys, time
import requests, bs4
import threading, logging
import smtplib
from random import *

WAIT_INTERVAL = 120
LOG_FILE = 'stockPriceLog1.txt'
SMTP_HOST = 'smtp.gmail.com'
SMTP_TLS_PORT = 587

def main():
    open(LOG_FILE, 'w').close()
    logging.basicConfig(filename=LOG_FILE,
                       level=logging.INFO,
                       format=' %(asctime)s %(message)s ')
    logging.info("StockWatcher - start programs")
    
    if len(sys.argv) >= 2:
        stock_list = sys.argv[1:]
    else:
        stock_list = ["MSFT","GOOG","AAPL","AMZN"]
        print("You did not choose a stock to watch, so we have chosen for you.")
   
    for i in range(len(stock_list)):
        stock = stock_list[i].upper()
        print("Begin watch for " + stock)
        thread = threading.Thread(target = get_quote, 
                                   args = (stock, ))
        thread.start()
    
    time.sleep(5)  # Sleep for threads to print msgs

    input("\nHit CTRL-BREAK to stop recording.\n\n")
    logging.info1("StockWatcher - end program")
    
def get_quote(symbol):
    """
    Get a stock quote for the given stock symbol using
    Python requests and BeautifulSoup modules.
    Determine the availability of webpage
    Request the quote every WAIT_INTERVAL minutes until the  
    user ends the program with CTRL-C
    Compare current quote with previous quote and send
    text when different.
    """ 

    # For Step C: Replace CODE HERE to get the stock
    #     prices from the Yahoo Finance website using 
    #     requests and Beautiful Soup, instead of 
    #     using the hardcoded list

    prices = ['20', '25', '30', '30', '30', '20']
    price = prices[0]
    prev_price = '10'
    
    text = "Start watching " + symbol + ": Price: " + price
    print(text)    
    logging.info(text)
    
    i = 0   # not needed with Steps C and D
    
    # Start watching and continue until CTRL-Break

    while True:

        # Get Price with Steps A and B only
        # Steps C and D use requests and Beautiful Soup 

        price = prices[i%6]
        
        # Send price for symbol to log

        logging.info(symbol + "\t" + price)
        
        i = i + 1   # not needed with Steps C and D
        
        # Check for price difference and send email, 
        # if different
 
        if price != prev_price:
            text = symbol + " now at " + price + \
                   "; was " + prev_price
            print(text)
            send_email(text)
            prev_price = price
        
        time.sleep(WAIT_INTERVAL)

def send_email(msg):
    """
    For now, this program just prints a message
    The code that sends the email is in Step D
    """
         
    print("sendEmail: " + msg)

main()    

    



