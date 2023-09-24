import os
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import pickle

driver = webdriver.Chrome()
f= open('credenciales.txt','r')
us = f.readline().strip()
pas = f.readline().strip()
driver.get('https://www.instagram.com/')
time.sleep(3)
username= driver.find_element(by=By.XPATH,value= '//*[@id="loginForm"]/div/div[1]/div/label/input')
username.click()
time.sleep(3)
username.send_keys(us)
time.sleep(3)
password= driver.find_element(by=By.XPATH,value= '//*[@id="loginForm"]/div/div[2]/div/label/input')
password.click()
time.sleep(3)
password.send_keys(pas)
time.sleep(3)
login = driver.find_element(by=By.XPATH,value='//div[text()="Iniciar sesión"]')
login.click()
time.sleep(3)
usuario='guisherm0'
driver.get(f'https://www.instagram.com/{usuario}')
time.sleep(3)
cant_seguidos=driver.find_element(by=By.XPATH,value='/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[3]/a/span')
val=int(cant_seguidos.text)/5
if not val%2==0:
    val+=1
val = int(cant_seguidos.text)
driver.get(f'https://www.instagram.com/{usuario}/following')
time.sleep(3)
for i in range(val):
    driver.execute_script("""
    var scrollt = document.querySelector('div[role="dialog"] ._aano')
    scrollt.scrollTop = scrollt.scrollHeight
    """)
    time.sleep(3)
set = driver.find_elements(by=By.XPATH,value='//div[@class="_aano"]/div/div/div/div/div/div/div[2]/div/div/div[1]/div/div/a')
set = [i.text for i in set]
save=open("seguidores.txt","w")
save.write(len(set))
save.writelines(set)
save.close()
print(len(set))
print(set)
