import bs4
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

browser = webdriver.Chrome()
browser.get("http://localhost:8000/")
print(browser.title)

try: 
    wait = WebDriverWait (browser, 10)
    elem = wait.until (EC.element_to_be_clickable ((By.PARTIAL_LINK_TEXT, "Tourn")))
    print (elem.text)
    elem.click()
    
    elem = wait.until (EC.element_to_be_clickable ((By.PARTIAL_LINK_TEXT, "Oak")))
    print (elem.text)
    elem.click()
    
    elem = wait.until (EC.presence_of_element_located ((By.TAG_NAME, "h3")))
    print (elem.text)
    
except TimeoutException:
    print ("Locating Links in WGT Website Failed")
    
golf_soup = bs4.BeautifulSoup (browser.page_source, "html.parser")
soup_elems = golf_soup.select ('td a')

total = 0
for el in soup_elems:
    score = el.getText()
    score = int(score)
    total = total + score

avg = total / len(soup_elems)
print("Average Tournament Score: " + str(avg))
    
browser.close()