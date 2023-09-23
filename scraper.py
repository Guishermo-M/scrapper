import os
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import pickle

f = open('credenciales.txt','r')
# Configurar las opciones de Chrome
driver = webdriver.Chrome()
f= open('credenciales.txt','r')
us=f.readline()
pas=f.readline()
usuario=us
driver.get('https://www.instagram.com/')
time.sleep(5)
usuario = ''
contraseña = ''
username= driver.find_element(by=By.NAME,value= 'username')
time.sleep(3)
username.click()
time.sleep(3)
username.send_keys(usuario)
time.sleep(10)
seguidos=f'https://www.instagram.com/{usuario}/following'
