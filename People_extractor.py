from bs4 import BeautifulSoup
from selenium import webdriver
import time

#Following are optional required
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pprint import pprint



file_input = "C:\\Users\\cjwar\\Documents\\Esven Enterprises\\Like Minded bot\\Pages\\Star Wars.html"

page_link_list = []
name_list = []
# for x in range(158)
with open (file_input, encoding='utf-8') as fp:
    html_doc = str(fp.read().encode('utf-8'))
    soup = BeautifulSoup(html_doc, 'html.parser')
    all_people = soup.find_all("a", {"class" : "_32mo"})
    for x in all_people:
        name =  x.get_text()
        link = x.get('href')
        print(name)
        # name =  x.find("a").get_text()
        # name_list.append(name)
        # facebook_search_link = "https://www.facebook.com/search/str/"+name.replace(" ", "+")+"/pages-named/likers/111762725508574/residents/present/intersect"
        # page_link_list.append(facebook_search_link)
        # link = x.find("a").get('href')
        # print(facebook_search_link)
