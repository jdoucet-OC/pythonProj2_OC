# -*- coding: utf-8 -*-
import sys
import P2_csv
import requests
from bs4 import BeautifulSoup


class PageScraper:
    
    def __init__(self, link_page):
        self.link = link_page
        self.soup = BeautifulSoup(requests.get(link_page).content, 'html.parser')
        self.title = self.find_title()
        self.description = self.find_desc()
        self.UPC,\
            self.priceNT,\
            self.priceWT,\
            self.numberAvailable = self.find_tab_attrs()
        self.category = self.get_category()
        self.rating = self.get_rating()
        self.image_url = self.get_img_link()

    def find_title(self):
        title = self.soup.find(class_='col-sm-6 product_main')
        return title.find('h1').text

    def find_desc(self):
        try:
            return self.soup.find('p', class_='').text
        except AttributeError:
            return "Aucune Description"

    def find_tab_attrs(self):
        attrtab = []
        temptab = self.soup.find('table', class_='table table-striped')
        temptab2 = temptab.findAll('td')

        for attr in temptab2:
            attrtab.append(attr.text)

        upc = attrtab[0]
        pricent = attrtab[2]
        pricewt = attrtab[3]
        numberavailable = attrtab[5]

        return upc, pricent, pricewt, numberavailable

    def get_category(self):
        categorysoup = self.soup.find('ul', class_='breadcrumb')
        return categorysoup.findAll('a')[2].text

    def get_all(self):
        return [self.link, self.UPC, self.title,
                self.description, self.priceNT, self.priceWT,
                self.numberAvailable, self.category, self.rating,
                self.image_url]

    def get_rating(self):
        results = self.soup.find('div', class_='col-sm-6 product_main')
        if results.find('p', class_="star-rating One"):
            return "1/5"
        if results.find('p', class_="star-rating Two"):
            return "2/5"
        if results.find('p', class_="star-rating Three"):
            return "3/5"
        if results.find('p', class_="star-rating Four"):
            return "4/5"
        if results.find('p', class_="star-rating Five"):  # else
            return "5/5"

    def get_img_link(self):
        image_container = self.soup.find('div', class_='carousel-inner')
        return self.relative_to_absolute(image_container.find('img')['src'])

    def relative_to_absolute(self, imglink):
        splittedLink = self.link.split('/')
        splittedImgLink = imglink.split('/')
        retour = imglink.count('../')
        del splittedImgLink[:retour]
        del splittedLink[-retour-1:]
        sep = '/'
        return sep.join(splittedLink+splittedImgLink)
            
    
def main(argv):
    new_page = PageScraper(argv[0])
    P2_csv.book_csv_init(new_page.title, new_page.get_all())
    
    
if __name__ == "__main__":
    main(sys.argv[1:])
