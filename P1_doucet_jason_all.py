# -*- coding: utf-8 -*-
from P1_doucet_jason_cat import category_scraper
import sys
import requests
from bs4 import BeautifulSoup


class entire_site_scraper():
    
    def __init__(self):
        self.link = "http://books.toscrape.com/"
        page = requests.get(self.link)
        soup = BeautifulSoup(page.content, 'html.parser')
        soup2 = soup.find('ul',class_='nav nav-list')
        soup3 = soup2.findAll('a')
        linkList = []
        for item in soup3:
            linkList.append(self.link+item["href"])
        #retirer la catégorie " Book " qui contient tous les livres
        linkList.pop(0)
        for links in linkList:
            category_scraper(links)
        
            
    
    
        
        
def main():
    entire_site_scraper()
    
    
if __name__ == "__main__":
    main()