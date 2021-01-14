# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import csv
import sys

 

class page_scraper():
    
    def __init__(self,link_page):
        #Lien, titre et preparation soupe
        self.link = link_page
        
        page = requests.get(self.link)
        soup = BeautifulSoup(page.content, 'html.parser')
        
        findTitle=soup.find(class_='col-sm-6 product_main')
        self.title = findTitle.find('h1').text
        #trouver le paragraph description qui n'a pas de classe
        self.description = soup.find('p',class_='').getText()
        
        #ittération du tableau des prix
        attrTab = []
        tempTab = soup.find('table',class_='table table-striped')
        tempTab2 = tempTab.findAll('td')
        
        for attr in tempTab2:
            attrTab.append(attr.text)
            
        self.UPC = attrTab[0]
        self.priceNT = attrTab[2]
        self.priceWT = attrTab[3]
        self.numberAvailable = attrTab[5]
        
        #image_url, review rating and category
        categorySoup=soup.find('ul',class_='breadcrumb')
        self.category=categorySoup.findAll('a')[2].text
        
        #chercher dans col-sm-6 product_main le nom de la classe contenant les étoiles
        results=soup.find('div',class_='col-sm-6 product_main')
        if results.find('p',class_="star-rating One"):
            self.rating = "1/5"
        if results.find('p',class_="star-rating Two"):
            self.rating = "2/5"
        if results.find('p',class_="star-rating Three"):
            self.rating = "3/5"
        if results.find('p',class_="star-rating Four"):
            self.rating = "4/5"
        if results.find('p',class_="star-rating Five"):#else
            self.rating = "5/5"
            
        #Image
        image_container = soup.find('div',class_='carousel-inner')
        
        self.image_url = self.relative_to_absolute(image_container.find('img')['src'])
        
        
        
    def get_all(self):
        return (self.link,self.UPC,self.title,
                self.description,self.priceNT,self.priceWT,
                self.numberAvailable,self.category,self.rating,
                self.image_url)
        
    def csv_save(self):
    
        with open('testing.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            
            writer.writerow(["product_page_url", "universal_ product_code (upc)", "title","product_description"
                             ,"price_including_tax", "price_excluding_tax", "number_available"
                             , "category", "review_rating", "image_url"])
    
            writer.writerow([self.link,self.UPC,self.title,
                              self.description,self.priceNT,self.priceWT,
                              self.numberAvailable,self.category,
                              self.rating,self.image_url])
    
    def relative_to_absolute(self,imgLink):
        splittedLink = self.link.split('/')
        splittedImgLink = imgLink.split('/')
        retour = imgLink.count('../')
        del splittedImgLink[:retour]
        del splittedLink[-retour-1:]
        sep = '/'
        return sep.join(splittedLink+splittedImgLink)
            
    
def main(argv):
    
    new_page = page_scraper(argv[0])
    new_page.csv_save()
    
    
if __name__ == "__main__":
    
    main(sys.argv[1:])
