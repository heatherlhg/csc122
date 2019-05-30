import sys, time
import requests, bs4
import threading, logging
import smtplib
from random import *

WAIT_INTERVAL = 120
LOG_FILE = 'stockPriceLog3.txt'
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
    
    resp = requests.get('https://finance.yahoo.com/quote/'+ symbol)
    stocks = bs4.BeautifulSoup(resp.text,"html.parser")
    price_elem = stocks.find(class_='Trsdu(0.3s)')
    
    if price_elem is not None:

        # Price retrieval statements
        price = price_elem.getText()
        price = price.replace(',','')
        price = float(price.strip())

        # Set up previous price for checking 
        # whether or not to send text
        prev_price = price + random()
        
    else:
        print("Symbol " + symbol + " not found.")
        sys.exit()

    
    text = "Start watching " + symbol + ": Price: " + str(price)
    print(text)
    logging.info(text)

    while True:
        try: 
            resp = requests.get('https://finance.yahoo.com/quote/'+ symbol)
            stocks = bs4.BeautifulSoup(resp.text,"html.parser")
            price_elem = stocks.find(class_='Trsdu(0.3s)')

            # Price retrieval statements
            price = price_elem.getText()
            price = price.replace(',','')
            price = float(price.strip())

            logging.info(symbol + "\t" + str(price))

            if price != prev_price:
                text = symbol + " now at " + str(price) + " was at " + str(prev_price)
                print(text)
                send_email(text)
                prev_price = price

            time.sleep(WAIT_INTERVAL)

        except Exception:   
            text = "Connection Problem with " + symbol
            print(text)
            time.sleep(WAIT_INTERVAL)

def send_email(msg):
    # Get an SMTP object for sending the email
    smtp_obj = smtplib.SMTP(SMTP_HOST, SMTP_TLS_PORT)

    # Identify yourself to an ESMTP server using EHLO
    smtp_obj.ehlo()

    # Put the SMTP connection in
    # TLS (Transport Layer Security) mode.

    smtp_obj.starttls()

    # Login using my fake Augie Rush email account.
    # Note that gmail may only allow one email, because it 
    # now verifies devices where logins come from
    # In that case you may need your own gmail account     

    smtp_obj.login('augierush@gmail.com', 'centralpark')

    # Send the email     
    # Change the receiving email to go to yourself 
    smtp_obj.sendmail('augierush@gmail.com', 
                       'hlgates@my.waketech.edu',
                       'Subject: StockWatcher update \n' + msg)

    # Leave the connection     

    smtp_obj.quit()
    print ("sendEmail: " + msg)


main() 