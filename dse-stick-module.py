from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
from datetime import datetime


birksUrl = "https://www.costco.ca/birkenstock-men%E2%80%99s-arizona-oiled-leather-sandal.product.100504650.html"
stickModuleUrl = "https://www.bestbuy.ca/en-ca/product/playstation-5-stick-module-for-dualsense-edge-wireless-controller-black/16571771"
testUrl = "https://www.bestbuy.ca/en-ca/product/playstation-5-dualsense-wireless-controller-midnight-black/17905836"

import smtplib
import ssl
from email.message import EmailMessage
# ------------------------------------------------------------ #
# Email section
def sendEmail():
    context = ssl.create_default_context()
    gmail_user = 'INSERT GMAIL BURNER ACC'
    gmail_password = 'INSERT GMAIL BURNER ACC PWD'

    msg = EmailMessage()
    msg.set_content(stickModuleUrl)
    msg['Subject'] = 'BestBuy Stick Modules In Stock'
    msg['From'] = gmail_user
    msg['To'] = 'INSERT RECIPIENT EMAIL'

    try:
      with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp_server:
        smtp_server.ehlo()
        smtp_server.login(gmail_user, gmail_password)
        smtp_server.send_message(msg)
        smtp_server.quit()
        print ("Email sent successfully!")
    except Exception as ex:
        print ("Something went wrong….",ex)

# ----------------------------- Driver Params ------------------------------------ #
MACPATH = "/opt/homebrew/bin/chromedriver"
cService = webdriver.ChromeService(executable_path = MACPATH)
driver = webdriver.Chrome(service = cService)
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)

# ------------------------------------------------------------------------------- #

url = stickModuleUrl

emailSent = False

def check_exists(driver):
    try:
        addToCart = driver.find_element(By.CLASS_NAME, "addToCartButton")
    except NoSuchElementException:
        return False
    return addToCart.is_enabled()

def notify(msg):
    date = datetime.now().strftime("%d-%b-%Y %H:%M:%S")
    print(msg, "as of", date)

while True:
    driver.get(url)
    if (check_exists(driver)):
        notify("Modules in stock!!!")
        if (emailSent == False):
            sendEmail()
            emailSent = True
    else:
        notify("OOS")
    time.sleep(30)