from bs4 import BeautifulSoup
from selenium import webdriver
import requests

from selenium import webdriver
from selenium.webdriver.common.by import By


maximum = 0
page =1 

# URL, response, source, soup
url = " https://en.wikipedia.org/wiki/American_football"
response = requests.get(url)
source = response.text
soup = BeautifulSoup(source, "html.parser")

titles = soup.select('#mw-content-text p a')

for title in titles:
    print(title.next)
    
   