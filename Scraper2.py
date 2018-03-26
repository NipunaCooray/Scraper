# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 17:22:14 2018

@author: n.cooray
"""

import requests
from bs4 import BeautifulSoup
result = requests.get("http://www.essentialbaby.com.au/forums/index.php?/topic/781996-i-dropped-my-baby/")
print(result.status_code)
c = result.content
soup = BeautifulSoup(c)
samples = soup.find_all("a", "item-title")

#div itemprop="commentText"