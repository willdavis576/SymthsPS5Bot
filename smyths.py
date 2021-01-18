import time
from selenium import webdriver
import sys
import smtplib

from string import Template

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

MY_ADDRESS = ''
PASSWORD = ''

sys.setrecursionlimit(10**6) 

def alert():
    s = smtplib.SMTP(host='smtp-mail.outlook.com', port=587)
    s.starttls()
    s.login(MY_ADDRESS, PASSWORD)

    msg = MIMEMultipart()
    message = "SYMTHS UPDATE"

    msg['From'] = MY_ADDRESS
    msg['To'] = MY_ADDRESS
    msg['Subject'] = "SYMTHS UPDATE"

    msg.attach(MIMEText(message, 'plain'))

    s.send_message(msg)
    del msg

    s.quit()


pos = 1

addToTrolley = '/html/body/div[7]/section/div/div/div[2]/div[1]/div[5]/div/div/div/div[2]/form/button'
cookies = '/html/body/div[4]/div/div/div[1]/div[4]/div[1]/button'


def clickButton(xpath, name):
    try:
        driver.find_element_by_xpath(xpath).click()
        pass
    except Exception:
        print("NAH I can't find that damn button", name)
        time.sleep(0.05)
        clickButton(xpath, name)


def clickButtonAdd(xpath, name):
    try:
        driver.find_element_by_xpath(xpath).click()
        alert()
        pass
    except Exception:
        print("NAH I can't find that damn button", name)
        loadPage()
        time.sleep(0.05)
        clickButtonAdd(xpath, name)


def enterData(field, data):
    try:
        driver.find_element_by_xpath(field).send_keys(data)
        pass
    except Exception:
        time.sleep(0.01)
        enterData(field, data)


def readLabel(xpath, name):
    try:
        labelText = str(driver.find_element_by_xpath(xpath).text)
        return labelText
        pass
    except Exception:
        time.sleep(0.1)
        readLabel(xpath, name)


def loadPage():
    driver.get('https://www.smythstoys.com/uk/en-gb/video-games-and-tablets/playstation-5/playstation-5-consoles/playstation-5-digital-edition-console/p/191430')


driver = webdriver.Chrome( < path to chromedriver > )
loadPage()
clickButton(cookies, "cookies")
clickButtonAdd(addToTrolley, "add to trolley")
