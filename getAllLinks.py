# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 18:47:23 2018

@author: n.cooray
"""
"""
import requests
from bs4 import BeautifulSoup
page = requests.get('https://www.google.dz/search?q=site:http://www.essentialbaby.com.au/forums/index.php?/forum/50-birth-6-months/"baby falls fell drop fallen -pregnant" ')
soup = BeautifulSoup(page.content,'html.parser')

links = soup.findAll("a")
print(links)
"""
import requests
from bs4 import BeautifulSoup
page = requests.get('https://www.google.dz/search?q=site:http://www.essentialbaby.com.au/forums/index.php?/forum/50-birth-6-months/"baby falls fell drop fallen -pregnant" ')
soup = BeautifulSoup(page.content,'html.parser')
import re
links = soup.findAll("a")
for link in  soup.find_all("a",href=re.compile("(?<=/url\?q=)(htt.*://.*)")):
    print(re.split(":(?=http)",link["href"].replace("/url?q=","")))