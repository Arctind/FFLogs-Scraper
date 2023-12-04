import requests
import time
import threading
from PIL import Image, ImageTk
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from requests_html import HTMLSession

timeList = []
actionList = []
playerList = []
mitigationList = ["Reprisal", "Feint", "Addle", "Troubadour", "Tactician", "Shield Samba", "Dismantle", "Heart of Light", "Dark Missionary",
                  "Divine Veil", "Shake it Off", "Mantra", "Magick Barrier"]
personalList = ["Rampart", "Nebula", "Camouflage", "Aurora", "Heart of Corundum", "Dark Mind", "Oblation", "The Blackest Night", "Shadow Wall",
                "Intervention", "Holy Sheltron", "Cover", "Clemency", "Sentinel", "Vengeance", "Thrill of Battle", "Raw Intuition", "Nascent Flash",
                "Equilibrium", "Bloodwhetting", "Riddle of Earth", "Arcane Crest", "Third Eye", "Shade Shift", "Nature's Minne", "Manaward",
                "Curing Waltz", "Radiant Aegis", "Vercure", "Verraise"]
inputURL = "https://www.fflogs.com/reports/QVT2MqxGPrvRbk4J#fight=30&type=damage-done&source=7&view=events"
guiVersion = False

class Player:
    def __init__(self, name, time, action):
        self.name = name
        self.time = time
        self.action = action

#Renders the js code FFLogs and sets driver as an object of FFLogs with js
def renderPage(URL):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = Chrome(options=options)
    driver.implicitly_wait(5)
    driver.get(URL)
    time.sleep(10)
    return driver

#Navigating to the events/casts tab of the log
def navigator(driver):
    return driver

#Filling the list variables with time, action, and damage values
def parser(driver):
    global content
    content = driver.find_element(By.CSS_SELECTOR, "div[class*='dataTables_wrapper dt-jqueryui no-footer'")
    content = content.find_element(By.TAG_NAME, "tbody")
    time = content.find_elements(By.CSS_SELECTOR, "td[class*='main-table-number'")
    action = content.find_elements(By.CSS_SELECTOR, "a[target*='_blank'")

    for t in time:
        timeList.append(t.text)
    for a in action:
        actionList.append(a.text)
    return

def mainText():
    #Gets FFLogs URL
    print("Enter log URL")
    inputURL = input()
    
    #Navigating FFLogs and scraping the battle events
    inputURL = navigator(renderPage(inputURL))
    parser(inputURL)

    print(timeList)
    print(actionList)
    print(len(timeList))
    print(len(actionList))

    i = 0
    for a in actionList:
        if a in mitigationList:
            print(a + " used at " + timeList[i])
        elif a in personalList:
            print(a + " used at " + timeList[i])
        i = i + 1

if __name__ == "__main__":
    mainText()