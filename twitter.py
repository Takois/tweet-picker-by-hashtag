from selenium import webdriver
import loginInfo
import time
from selenium.webdriver.common.keys import Keys

browser= webdriver.Firefox()
browser.get("https://twitter.com")

time.sleep(1)

giris_yap = browser.find_element_by_xpath("//*[@id='doc']/div/div[1]/div[1]/div[2]/div[2]/div/a[2]")
giris_yap.click()

time.sleep(1)

username = browser.find_element_by_xpath("//*[@id='page-container']/div/div[1]/form/fieldset/div[1]/input")
password = browser.find_element_by_xpath("//*[@id='page-container']/div/div[1]/form/fieldset/div[2]/input")

username.send_keys(loginInfo.user)
password.send_keys(loginInfo.pw)

time.sleep(1)

login = browser.find_element_by_xpath("//*[@id='page-container']/div/div[1]/form/div[2]/button")
login.click()

time.sleep(5)

searchArea = browser.find_element_by_xpath("//*[@id='react-root']/div/div/div/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div[2]/input")
                                        
searchArea.send_keys("#progrock")
time.sleep(2)
searchArea.send_keys(Keys.ENTER)
time.sleep(2)

elements = []

for j in range (1,10):
    anlik = browser.find_element_by_xpath("//*[@id='react-root']/div/div/div/main/div/div/div/div/div/div[2]/div/div/section/div/div/div/div["+str(j)+"]/div/article/div/div[2]/div[2]/div[2]")
    elements.append(anlik)

for element in elements:
    try:
        element.click()
        time.sleep(2)
    except Exception:
        print("Bir sorun oluştu...")
    
time.sleep(3)
    

browser.close()









