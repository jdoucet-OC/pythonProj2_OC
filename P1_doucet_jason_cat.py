# -*- coding: utf-8 -*-
from P1_doucet_jason import page_scraper
import csv
import sys
import requests
from bs4 import BeautifulSoup


class category_scraper():
    
    def __init__(self,link_page):
            self.link = link_page
            page = requests.get(self.link)
            soup = BeautifulSoup(page.content, 'html.parser')
            ii=2
            cat=soup.find('div',class_="page-header action").find('h1').text
            self.init_csv(str(cat).strip())
            while True:
                linkSoup = soup.findAll('li',class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")
                linkList = []
                for liste in linkSoup:
                    linkList.append(liste.find('a')["href"])
                linkList=self.relative_to_absolute(linkList)
                for item in linkList:
                    page_obj=page_scraper(item)
                    attrs=page_obj.get_all()
                    print('En cours :',attrs[2],'\n')
                    self.csv_save(attrs,cat)
                if soup.find('li',class_='next'):
                    tabLink = self.link.split('/')
                    tabLink[-1] = 'page-'+str(ii)+'.html'
                    sep = '/'
                    self.link=sep.join(tabLink)
                    page = requests.get(self.link)
                    soup = BeautifulSoup(page.content, 'html.parser')
                    ii += 1
                else:
                    break
            print('Done!')
                 
    def relative_to_absolute(self,liste):
        newList=[]
        for elem in liste:
            splittedLink = self.link.split('/')
            retour = elem.count('../')
            splitted = elem.split('/')
            del splitted[:retour]
            del splittedLink[-retour-1:]
            sep = '/'
            newList.append(sep.join(splittedLink+splitted))
        return newList
    
    def init_csv(self,category):
        with open(category+'.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            
            writer.writerow(["product_page_url", "universal_ product_code (upc)", "title","product_description"
                             ,"price_including_tax", "price_excluding_tax", "number_available"
                             , "category", "review_rating", "image_url"])
    
    def csv_save(self,tab,category):
        with open(category+'.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(tab)
    
    
def main(argv):
    category_scraper(argv[0])
    
    
if __name__ == "__main__":
    main(sys.argv[1:])