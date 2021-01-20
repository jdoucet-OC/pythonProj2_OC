# -*- coding: utf-8 -*-
import P1_doucet_jason_cat as P1cat
import requests
from bs4 import BeautifulSoup


def main():
    link = "http://books.toscrape.com/"
    soup = BeautifulSoup(requests.get(link).content, 'html.parser')
    soup2 = soup.find('ul', class_='nav nav-list')
    soup3 = soup2.findAll('a')
    linklist = []
    for item in soup3:
        linklist.append(link + item["href"])
    linklist.pop(0)
    for links in linklist:
        cat_scraper = P1cat.CategoryScraper(links)
        cat_scraper.get_all_pages()
    
    
if __name__ == "__main__":
    main()
