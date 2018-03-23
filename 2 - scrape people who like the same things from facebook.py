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





likes_sections = ["likes_section_music", "likes_section_books", "likes_people"]

page_link_list = [[]]
name_list = [[]]
# for x in range(158)

'''this function scrapes facebook for all likes in the like section array'''
def facebook_search_bot():

    ffprofile = "C:/Users/cjwar/AppData/Roaming/Mozilla/Firefox/Profiles/b4r73h83.Like minded bot"
    driver = webdriver.Firefox(firefox_profile=ffprofile)
    for i, page_link in enumerate(page_link_list[index]):
        try:
            element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'nav-bar')))
        except TimeoutException:
            print("",end="")
        # url = "https://www.meetup.com/vegan101/members/?offset="+str(i*20)+"&sort=social&desc=1"
        driver.get(page_link)

        # Get scroll height
        last_height = driver.execute_script("return document.body.scrollHeight")
        count = 0
        while True and count < 100:
            # Scroll down to bottom
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Wait to load page
            time.sleep(2.5)

            # Calculate new scroll height and compare with last scroll height
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height
            count += 1

        file_path = "C:\\Users\\cjwar\\Documents\\Esven Enterprises\\Like Minded bot\\Searches\\"+str(page_category)+"\\"+name_list[index][i]+".html"
        html_code = driver.page_source
        with open (file_path, 'w', encoding='UTF-8') as fp:
            html_code.encode('UTF-8', 'ignore')
            fp.write(html_code)
        print(str(name_list[index][i]) + " completed")
    driver.quit()


'''this extracts all the names of people who have a matching like, and gets their facebook url and appends it to either name_list or page_link_list'''
for i,x in enumerate(likes_sections):
    page_category = x
    file_input = "C:\\Users\\cjwar\\Documents\\Esven Enterprises\\Like Minded bot\\Pages\\"+page_category+".html"
    with open (file_input, encoding='utf-8') as fp:
        html_doc = str(fp.read().encode('utf-8'))
        soup = BeautifulSoup(html_doc, 'html.parser')
        all_likes = soup.find_all("div", {"class" : "fsl fwb fcb"})
        for x in all_likes:
            # if x != all_likes[0]:
                name =  x.find("a").get_text()
                facebook_search_link = "https://www.facebook.com/search/str/"+name.replace(" ", "+")+"/pages-named/likers/111762725508574/residents/present/intersect"
                link = x.find("a").get('href')
                if "\\x" not in name:
                    name_list[i].append(name)
                    page_link_list[i].append(facebook_search_link)
        name_list.append([])
        page_link_list.append([])

                    # print(name)
del name_list[-1]
del page_link_list[-1]
'''this only has to be run once to get the html data'''
for index, x in enumerate(likes_sections):
    page_category = x
    facebook_search_bot()
# for x in likes_sections:
#     print(x)
