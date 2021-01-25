#!/usr/bin/env python3

import sys
import P2_book as BookScraper
import P2_misc_funcs as MiscFuncs
import P2_csv as CsvEdit


class CategoryScraper:
    """une catégorie de livre"""

    def __init__(self, link_page):
        """
        :param link_page: Lien de la catégorie à scrape
        """

        self.firstLink = link_page
        self.firstSoup = MiscFuncs.get_cat_soup(link_page)
        self.cat = self.find_cat()

    def find_cat(self):
        """
        :return: Le nom de la catégorie à scrape
        """
        cat = self.firstSoup.find('div', class_="page-header action").\
            find('h1').text
        return cat

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
            linksoup = current_soup.find_all('li',
                                             class_="col-xs-6 col-sm-4 "
                                                    "col-md-3 col-lg-3")
            linklist = []
            for liste in linksoup:
                linklist.append(liste.find('a')["href"])
            linklist = MiscFuncs.relative_to_absolute_list(linklist, current_link)
            for item in linklist:
                page_obj = BookScraper.PageScraper(item)
                attrs = page_obj.get_all()
                print(f'En cours : {attrs[2]}')
                CsvEdit.csv_save(attrs, self.cat)
            if current_soup.find('li', class_='next'):
                tablink = current_link.split('/')
                tablink[-1] = f'page-{str(ii)}.html'
                sep = '/'
                current_link = sep.join(tablink)
                current_soup = MiscFuncs.get_cat_soup(current_link)
                ii += 1
            else:
                break
    
    
def main(argv):
    """
    :param argv: Lien de la catégorie à scrape
    :return: Utilise la méthode_get all_pages pour écrire
    le fichier CSV
    """
    try:
        category = argv[0]
    except IndexError:
        print("Vous devez spécifier un lien de catégorie"
              " sur http://books.toscrape.com")
        sys.exit(1)
    new_cat = CategoryScraper(category)
    new_cat.get_all_pages()


if __name__ == "__main__":
    main(sys.argv[1:])

