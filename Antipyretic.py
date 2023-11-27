import requests
import time
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from requests_html import HTMLSession

timeList = []
actionList = []
damageList = []

def renderPage(URL):
    global driver
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = Chrome(options=options)
    driver.implicitly_wait(5)
    driver.get(URL)
    time.sleep(10)

def parser():
    global content
    i = 0
    content = driver.find_element(By.CSS_SELECTOR, "div[class*='event-view-events-box'")
    content = content.find_element(By.TAG_NAME, "tbody")
    time = content.find_elements(By.CSS_SELECTOR, "td[class*='main-table-number'")
    action = content.find_elements(By.CSS_SELECTOR, "a[class*='school-1024'")
    damage = content.find_elements(By.CSS_SELECTOR, "span[style*='color: #e87b7b'")

    for t in time:
        timeList.append(t.text)
    for a in action:
        actionList.append(a.text)
    for d in damage:
        damageList.append(d.text)
    return

if __name__ == "__main__":
    renderPage("https://www.fflogs.com/reports/QVT2MqxGPrvRbk4J#fight=30&type=damage-done&source=7&view=events")
    parser()
    print(content)
    print(timeList)
    print(actionList)
    print(damageList)