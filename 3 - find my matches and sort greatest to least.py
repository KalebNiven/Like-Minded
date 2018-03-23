import os
from bs4 import BeautifulSoup
from collections import Counter

'''Attention: Running this file takes some time. It is searching through thousands of people spread thourgh multiple html files. The output will be a sorted tuple list containing how many likes I have in common with everyone'''


categories = ["likes_section_movies", "likes_section_tv_shows", "likes_section_music", "likes_section_books", "likes_people"]


links_list = []
name_list = []

for index, y in enumerate(categories):
    files = []
    file_dir = "C:\\Users\\cjwar\\Documents\\Esven Enterprises\\Like Minded bot\\Searches\\"+y+"\\"
    for x in os.listdir(file_dir):
        files.append(x)
    # links_list = []
    # name_list = []
    table = {}
    for r in range(len(files)):
        file_input = file_dir+files[r]
        with open (file_input, encoding='utf-8') as fp:
            html_doc = str(fp.read().encode('utf-8'))
            soup = BeautifulSoup(html_doc, 'html.parser')
            all_people = soup.find_all("a", {"class" : "_32mo"})
            print(files[r])
            for x in all_people:
                name =  x.get_text()
                link = x.get('href').replace("https://www.facebook.com/","").replace("?ref=br_rs","").replace("profile.php?id=","").replace("&ref=br_rs","")
                links_list.append(link)
                name_list.append(name)

for i in range(len(name_list)):
    table[links_list[i]] = name_list[i]


print("Start Names")

# for x in Counter(links_list):
#     print(x)
file_output = "C:\\Users\\cjwar\\Documents\\Esven Enterprises\\Like Minded bot\\Output\\all_categories.txt"
table_counter = Counter(links_list)
with open (file_output, 'w') as fo:
    fo.write(str(table_counter))
    print(table_counter)
