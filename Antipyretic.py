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
input = "https://www.fflogs.com/reports/QVT2MqxGPrvRbk4J#fight=30&type=damage-done&source=7&view=events"

master = Tk()
master.resizable(False, False)
canvas = Canvas(master, width=960, height=540)
canvas.pack()

bg = ImageTk.PhotoImage(file="bg.jpg")
canvas.create_image(0, 0, image=bg, anchor=NW)

entry = Entry(master, width=100, font=("Helvetica, 12"), bg="#7DC3E1")
entry.place(relx=.5, rely=.5, anchor=CENTER)
entry.insert(0, "Enter log URL")

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

def main():
    input = entry.get()
    renderPage(input)
    parser()
    print(content)
    print(timeList)
    print(actionList)
    print(damageList)

if __name__ == "__main__":
    button = Button(master, text="Go", command=main)
    button.pack()
    #threading.Thread(target=main())
    master.mainloop()
    #renderPage(entry)
    #parser()