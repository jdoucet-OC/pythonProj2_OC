# -*- coding: utf-8 -*-


import sys
import requests
from bs4 import BeautifulSoup
import P1_doucet_jason as P1book
import P2_csv
import misc_funcs


class CategoryScraper:
    
    def __init__(self, link_page):
        self.firstLink = link_page
        self.firstSoup = BeautifulSoup(requests.get(self.firstLink).content, 'html.parser')
        self.cat = self.firstSoup.find('div', class_="page-header action").find('h1').text

    def get_all_pages(self):
        ii = 2
        current_soup = self.firstSoup
        current_link = self.firstLink
        P2_csv.csv_init(self.cat)
        while True:
            linksoup = current_soup.findAll('li', class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")
            linklist = []
            for liste in linksoup:
                linklist.append(liste.find('a')["href"])
            linklist = misc_funcs.relative_to_absolute(linklist, current_link)
            for item in linklist:
                page_obj = P1book.PageScraper(item)
                attrs = page_obj.get_all()
                print('En cours :', attrs[2], '\n')
                P2_csv.csv_save(attrs, self.cat)
            if current_soup.find('li', class_='next'):
                tablink = current_link.split('/')
                tablink[-1] = 'page-' + str(ii) + '.html'
                sep = '/'
                current_link = sep.join(tablink)
                current_soup = BeautifulSoup(requests.get(current_link).content, 'html.parser')
                ii += 1
            else:
                break

    
def main(argv):
    new_cat = CategoryScraper(argv[0])
    new_cat.get_all_pages()


if __name__ == "__main__":
    main(sys.argv[1:])
