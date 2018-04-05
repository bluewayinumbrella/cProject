#-*- coding: utf-8 -*-
import requests
import sys
from bs4 import BeautifulSoup
from abc import *

from common import *
# logError(blabla)
# filterList(list, filter)



Class AppStore(metaclass = ABCMeta):
# this is parents class for each AppStore
# Almost Abstract Class

    bingSearch="https://www.bing.com/search?" +
    "q=site%3A{0}&qs=n&form=QBRE&sp=-1&pq=site%3Ahttp%3A{0}&sc=0-44&sk=" +
    "&cvid=886DD08E942B465DABA288E16D94F7A5&first={1}&FORM=PERE"
    # bing advanced search url (site:parentUrl oneMoreKeyword)
    
    def searchInBing(self, site, keyword):
        # search in Bing filtering "site:http://marketaddr/ subdir&blabla"
        # Concatation of site and keyword must compose url of app detail page
        # return the each app detail page

        maxPage = 90
        urlList = []
        urlFilteredList = []

        for idx in range(0, maxPage)
            req = requests.get(bingSearch.format(site + "+" + keyword, 10*idx + 1))
            html = req.text
            soup = BeautifulSoup(html, 'html.parser')
            marketPages = (
            '#b_results > li > div.b_algoheader > a'
            )
            for page in marketPages:
                urlList += url['href']
            
        
        urlFilteredList = filterList(urlList, site + keyword)
                    
            


    @abstractmethod
    def searchInMarket(self, keyword):
        # search some keyword in each searchInMarket
        # return the each app detail page
        pass

    @abstractmethod
    def findListPage(self):
        pass

    @abstractmethod
    def checkUpdateTime(self, detail):
        # find update time in app detail page
        pass

    @abstractmethod    
    def checkReputation(self, detail):
        # custom 
        pass

    @abstractmethod    
    def downloadAppFile(self, detail):    
        pass

    

Class Tensent(AppStore):

    def searchInMarket(self, keyword):
        # search some keyword in each searchInMarket
        # return the each app detail page
        pass

   
    def findListPage(self, addr):
        pass

    
    def checkUpdateTime(self, detail):
        # find update time in app detail page
        pass

        
    def checkReputation(self, detail):
        # custom 
        pass

       
    def downloadAppFile(self, detail):    
        pass


Class Shaomi(AppStore):


Class Mobile365(AppStore):

