#!/usr/bin/env python3

import P2_category
import P2_misc_funcs as MiscFuncs


def main():
    """
    :return: Toute les catégories du site, un
        fichier CSV par catégorie
    """

    soup = MiscFuncs.get_site_soup()
    link = "http://books.toscrape.com/"
    linklist = []
    for item in soup:
        linklist.append(link + item["href"])
    linklist.pop(0)
    for links in linklist:
        cat_scraper = P2_category.CategoryScraper(links)
        cat_scraper.get_all_pages()
        print(f'{cat_scraper.cat} : Done!\n ')
    
    
if __name__ == "__main__":
    main()
