'''
Shopify would like to build an internal URL shortener service (similar to bit.ly), 
which would allow users to create shortened links and share them around for convenience.


We will start with a simplified version of the problem, and add new requirements gradually to make things more interesting. 
Try to design your system so that you can extend it as you go, and feel free to refactor as you learn more.
'''

import random
import string
import re

class urlShortener:
    def __init__(self):
        self.urls = dict()
    
    def shortenUrl(self, originalUrl):
        return
    
    def randomize(self):
        res = [''] * 5
        for i in range(len(res)):
            res[i] = random.choice(string.ascii_letters)
        return ''.join(res)


'''
https://youtube.com/eosuiahnofjlkasdf
https://youtube.com/eosuiahnofjlkasdf
https://youtube.com/1
'''
urlShorter = urlShortener()
urlShorter.randomize()