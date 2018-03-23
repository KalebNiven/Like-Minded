from selenium import webdriver
import time

#Following are optional required
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


urls = ["likes_section_movies", "likes_section_tv_shows", "likes_section_music", "likes_section_books", "likes_people"]

baseurl = "https://www.facebook.com/kniven51/"
# username = "admin"
# password = "admin"
#
# xpaths = { 'usernameTxtBox' : "//input[@name='username']",
#            'passwordTxtBox' : "//input[@name='password']",
#            'submitButton' :   "//input[@name='login']"
#          }


ffprofile = "C:/Users/cjwar/AppData/Roaming/Mozilla/Firefox/Profiles/b4r73h83.Like minded bot"
driver = webdriver.Firefox(firefox_profile=ffprofile)

for u in urls:
    try:
        element = WebDriverWait(driver,3).until(EC.presence_of_element_located((By.ID, 'nav-bar')))
    except TimeoutException:
        print("",end="")
    # url = "https://www.meetup.com/vegan101/members/?offset="+str(i*20)+"&sort=social&desc=1"
    driver.get(baseurl+u)
    for x in range(3):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(.5)

    file_path = "C:\\Users\\cjwar\\Documents\\Esven Enterprises\\Like Minded bot\\Pages\\"+u+".html"
    html_code = driver.page_source
    with open (file_path, 'w', encoding='UTF-8') as fp:
        html_code.encode('UTF-8', 'ignore')
        fp.write(html_code)
driver.quit()
