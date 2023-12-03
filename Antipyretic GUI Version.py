import requests
import time
import threading
from tkinter import *
from PIL import Image, ImageTk
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from requests_html import HTMLSession

timeList = []
actionList = []
damageList = []
mitigationList = ["Reprisal", "Feint", "Addle", "Troubadour", "Tactician", "Shield Samba", "Dismantle", "Heart of Light", "Dark Missionary",
                  "Divine Veil", "Shake it Off", "Mantra", "Magick Barrier"]
personalList = ["Rampart", "Nebula", "Camouflage", "Aurora", "Heart of Corundum", "Dark Mind", "Oblation", "The Blackest Night", "Shadow Wall",
                "Intervention", "Holy Sheltron", "Cover", "Clemency", "Sentinel", "Vengeance", "Thrill of Battle", "Raw Intuition", "Nascent Flash",
                "Equilibrium", "Bloodwhetting", "Riddle of Earth", "Arcane Crest", "Third Eye", "Shade Shift", "Nature's Minne", "Manaward",
                "Curing Waltz", "Radiant Aegis", "Vercure", "Verraise"]
input = "https://www.fflogs.com/reports/QVT2MqxGPrvRbk4J#fight=30&type=damage-done&source=7&view=events"

#Initializing a window
master = Tk()
master.geometry("960x580")
master.resizable(False, False)
master.title("Antipyretic")
canvas = Canvas(master, width=960, height=540)
canvas.pack()

bg = ImageTk.PhotoImage(file="bg.jpg")
canvas.create_image(0, 0, image=bg, anchor=NW)

#Creates an entry label
entry = Entry(master, width=100, font=("Helvetica, 12"), bg="#7DC3E1")
entry.place(relx=.5, rely=.5, anchor=CENTER)
entry.insert(0, "Enter log URL")

#Renders the js code FFLogs and sets driver as an object of FFLogs with js
def renderPage(URL):
    global driver
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = Chrome(options=options)
    driver.implicitly_wait(5)
    driver.get(URL)
    time.sleep(10)

#Filling the list variables with time, action, and damage values
def parser():
    global content
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

def list():
    i = 0
    for a in actionList:
        if (a in mitigationList):
            print(a + " used at " + timeList[i])
        elif (a in personalList):
            print(a + " used at " + timeList[i])
        i = i + 1
            
    #actionImg = ImageTk.PhotoImage(file="Resources/Verthunder III.png")
    #actionLabel = Label(master, image=actionImg)
    #actionLabel.grid(row=1, column=0)

def main():
    input = entry.get()
    renderPage(input)
    parser()
    button.pack_forget()
    entry.destroy()
    list()
    print(content)
    print(timeList)
    print(actionList)
    print(damageList)
    print(len(timeList))
    print(len(actionList))
    print(len(damageList))

if __name__ == "__main__":
    button = Button(master, text="Go", command=main)
    button.pack()
    master.mainloop()