#!/usr/bin/env python3

import sys
import requests
import P2_book as BookScraper
import P2_misc_funcs as MiscFuncs
import P2_csv as CsvEdit
from bs4 import BeautifulSoup


class CategoryScraper:
    """une catégorie de livre"""
    def __init__(self, link_page):
        """
        :param link_page: Lien de la catégorie à scrape
        """
        self.firstLink = link_page
        self.firstSoup = BeautifulSoup(requests.get(self.firstLink).content,
                                       'html.parser')
        self.cat = self.firstSoup.find('div',
                                       class_="page-header action").find('h1').text

    def get_all_pages(self):
        """Ecrit dans un fichier CSV les informations
        de tous les livres de la catégorie (attr: cat)
        dans un fichier csv : /category/<category.csv>
        """
        ii = 2
        current_soup = self.firstSoup
        current_link = self.firstLink
        CsvEdit.csv_init(self.cat)
        while True:
            linksoup = current_soup.findAll('li',
                                            class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")
            linklist = []
            for liste in linksoup:
                linklist.append(liste.find('a')["href"])
            linklist = MiscFuncs.relative_to_absolute_list(linklist, current_link)
            for item in linklist:
                page_obj = BookScraper.PageScraper(item)
                attrs = page_obj.get_all()
                print('En cours :', attrs[2], '\n')
                CsvEdit.csv_save(attrs, self.cat)
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
    """
    :param argv: Lien de la catégorie à scrape
    :return: Utilise la méthode_get all_pages pour écrire
    le fichier CSV
    """
    new_cat = CategoryScraper(argv[0])
    new_cat.get_all_pages()


if __name__ == "__main__":
    main(sys.argv[1:])

