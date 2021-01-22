#!/usr/bin/env python3

import sys
import requests
import P2_csv as CsvEdit
import P2_misc_funcs as miscFuncs
from bs4 import BeautifulSoup


class PageScraper:
    """un livre"""
    def __init__(self, link_page):
        """
        :param link_page: Lien du livre à scrape
        """
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
        """
        :return: Le titre du livre
        """
        title = self.soup.find(class_='col-sm-6 product_main')
        return title.find('h1').text

    def find_desc(self):
        """
        :return: La description du livre, si pas de description
            retourne " Aucune description "
        """
        try:
            return self.soup.find('p', class_='').text
        except AttributeError:
            return "Aucune Description"

    def find_tab_attrs(self):
        """
        :return: dans l'ordre - L'UPC, le prix hors taxe,
            le prix avec taxe et le nombre de livre disponible
        """
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
        """
        :return: La catégorie (thème) du livre
        """
        categorysoup = self.soup.find('ul', class_='breadcrumb')
        return categorysoup.findAll('a')[2].text

    def get_all(self):
        """
        :return: Tous les attributs dans une liste
        """
        return [self.link, self.UPC, self.title,
                self.description, self.priceNT, self.priceWT,
                self.numberAvailable, self.category, self.rating,
                self.image_url]

    def get_rating(self):
        """
        :return: Vérifie quelle classe HTML est présente,
            la note sur 5 correspond la classe trouvée.
        """
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
        """
        :return: le lien de l'image
        """
        image_container = self.soup.find('div', class_='carousel-inner')
        return miscFuncs.relative_to_absolute(self.link, image_container.find('img')['src'])
            
    
def main(argv):
    """
    :param argv: str: Le Lien de la page du livre à scrape

    Ecrit toutes les informations du livre dans un fichier
    CSV : /books/<titrelivre.csv>
    """
    new_page = PageScraper(argv[0])
    CsvEdit.book_csv_init(new_page.title, new_page.get_all())
    
    
if __name__ == "__main__":
    main(sys.argv[1:])
