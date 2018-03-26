# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 16:33:40 2018

@author: n.cooray
"""
"""
Scraping algorithm
==================
1. List the forum pages, put them in a list
2. Read the list one by one
3. Use requests.get() to get the content of the page
4. Find all "post entry-content" using soup.select
5. Get the text element from each in the list

"""

from bs4 import BeautifulSoup

import requests

import time


url = 'http://www.essentialbaby.com.au/forums/index.php?/topic/888113-has-your-baby-ever-fallen-from-change-table-or-similar/'

page  = requests.get(url)

data = page.text

soup = BeautifulSoup(data, 'html.parser')

#result = soup.find_all("div", {"class":"post entry-content "})

#print(result)

result = soup.select('div[class="post entry-content "]')

print(type(result))

print(len(result))

fileName = time.strftime("%Y%m%d-%H%M%S")+'.txt'


dataFile = open(fileName, 'w')

dataFile.write('\n'+url);
dataFile.write('\n\n Number of responses :'+str(len(result)))
dataFile.write('\n=============================================================')

for i in range(len(result)):
    print(result[i].getText())
    dataFile.write(result[i].getText())
    dataFile.write('\n+++++++++++++++++++++++')

dataFile.write('\n=============================================================')
    
dataFile.close()