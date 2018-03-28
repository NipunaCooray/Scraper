# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 16:15:18 2018

@author: n.cooray
"""
from bs4 import BeautifulSoup
import requests
import time

def saveData(url):
    #url = 'http://www.essentialbaby.com.au/forums/index.php?/topic/888113-has-your-baby-ever-fallen-from-change-table-or-similar/'
    
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

    return



with open('links.txt') as f:
    links = f.read().splitlines()


for i in range(len(links)):
    saveData(links[i])


   
#saveData('http://www.essentialbaby.com.au/forums/index.php?/topic/888113-has-your-baby-ever-fallen-from-change-table-or-similar/')    