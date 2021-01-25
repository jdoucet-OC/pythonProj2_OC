#!/usr/bin/env python3

import requests
import P2_category
import P2_misc_funcs as MiscFuncs
from bs4 import BeautifulSoup


def main():
    """
    :return: Toute les catégories du site, un
        fichier CSV par catégorie
    """

    link = "http://books.toscrape.com/"
    soup = MiscFuncs.get_soup(link)
    soup2 = soup.find('ul', class_='nav nav-list')
    soup3 = soup2.find_all('a')
    linklist = []
    for item in soup3:
        linklist.append(link + item["href"])
    linklist.pop(0)
    for links in linklist:
        cat_scraper = P2_category.CategoryScraper(links)
        cat_scraper.get_all_pages()
        print(f'{cat_scraper.cat} : Done!\n ')
    
    
if __name__ == "__main__":
    main()
