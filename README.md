# Like-Minded
Find Like Minded people through matching facebook likes


This program consists of 3 python files. They are:

1 - get my likes from facebook.py
2 - scrape people who like the same things from facebook.py
3 - find my matches and sort greatest to least.py

The people_extractor.py file is not currently being used. 

 There are 5 categories of 'likes' on facebook. They are:
1. Movies
2. Music
3. TV Shows
4. Books
5. People 

The program first scrapes my likes in all these categories. 
The second program opens facebook and searches for every like that I have in my page, starting with movies, and ending with people. This process takes a couple hours, because the only way to get everyone, is to scroll down on the facebook page for every like. This can take 5 minutes per like. 
The third program opens up all the copied facebook data, and sees how many likes each person has in common with me. 

You can find all the people it is scraping in the "Searches" folder.


The results of this project are saved in the Ouput folder. Each of the 5 categories have a list of the people most like me. Then there is a 6th list that combines all the previous 5 lists, and does a recount to see who is most like me across all of my likes combined. 
