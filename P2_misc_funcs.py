#!/usr/bin/env python3

import sys
import requests
from bs4 import BeautifulSoup


def relative_to_absolute(link, imglink):
    """
    :param link: Lien du site complet
    :param imglink: Lien de l'image incomplet
    :return: Le lien de l'image complète
    """

    splittedlink = link.split('/')
    splittedimglink = imglink.split('/')
    retour = imglink.count('../')
    del splittedimglink[:retour]
    del splittedlink[-retour - 1:]
    sep = '/'
    return sep.join(splittedlink + splittedimglink)


def relative_to_absolute_list(liste, link):
    """
    :param liste: Liste des liens incomplet des
     livre de la catégorie
    :param link: Lien du site
    :return: Liste des liens complet de la page n
        de la catégorie
    """

    newlist = []
    for elem in liste:
        splittedlink = link.split('/')
        retour = elem.count('../')
        splitted = elem.split('/')
        del splitted[:retour]
        del splittedlink[-retour - 1:]
        sep = '/'
        newlist.append(sep.join(splittedlink + splitted))
    return newlist


def get_book_soup(link):
    """
    :param link: Lien de la page du livre
    :return: Objet BeautifulSoup de la page
        ( HTML de la page )
    """
    webpage = requests.get(link)
    webpage.raise_for_status()
    soupe = BeautifulSoup(webpage.content, 'html.parser')
    try:
        titlesoupe = soupe.find(class_='col-sm-6 product_main')
        titlesoupe.find('h1').text
    except AttributeError:
        print('Lien vers livre invalide, veuillez choisir un livre sur'
              ' http://books.toscrape.com/index.html et copiez le lien'
              ' tel que : python P2_book.py <lienLivre>')
        sys.exit(1)
    return soupe


def get_cat_soup(link):
    """
    :param link: Lien de la page de la catégorie
    :return: Objet BeautifulSoup de la page
        ( HTML de la page )
    """
    webpage = requests.get(link)
    webpage.raise_for_status()
    soupe = BeautifulSoup(webpage.content, 'html.parser')
    try:
        soupe.find('div', class_="page-header action").find('h1').text
    except AttributeError:
        print('Lien vers catégorie invalide, veuillez choisir une '
              ' catégorie sur http://books.toscrape.com/index.html'
              ' et copiez le lien tel que : '
              ' python P2_book.py <lienCategory>')
        sys.exit(1)
    return soupe


def get_site_soup():
    """
    :return: Retourne l'objet BeautifulSoup contenant
     la liste des catégories
    """
    webpage = requests.get('http://books.toscrape.com/')
    webpage.raise_for_status()
    soup = BeautifulSoup(webpage.content, 'html.parser')
    soup2 = soup.find('ul', class_='nav nav-list')
    soup3 = soup2.find_all('a')
    return soup3


