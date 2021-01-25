#!/usr/bin/env python3

import os
import csv
import re


def book_csv_init(book, tab):
    """
    :param book: Titre du livre
    :param tab: Tableau des attributs du livre
    :return:Créer et édite le fichier CSV du livre
    """
    try:
        if not os.path.exists('books'):
            os.makedirs('books')
        title = re.sub(r'[^A-Za-z0-9]', ' ', book)
        with open(f'books/{title}.csv', 'w', encoding="utf-8", newline='') as file:
            fields = ["product_page_url", "universal_ product_code (upc)", "title",
                      "product_description", "price_including_tax", "price_excluding_tax",
                      "number_available", "category", "review_rating", "image_url"]
            writer = csv.DictWriter(
                file, fieldnames=fields)
            writer.writeheader()
            dictcomp = {fields[i]: tab[i] for i in range(len(fields))}
            writer.writerow(dictcomp)
        file.close()
    except OSError as err:
        print("OS error: {0}".format(err))


def csv_init(category):
    """
    :param category: catégorie du livre
    :return: créé un fichier CSV de la catégorie, avec
        ses entêtes
    """
    try:
        if not os.path.exists('category'):
            os.makedirs('category')
        with open(f'category/{category}.csv', 'w', encoding="utf-8", newline='') as file:
            writer = csv.DictWriter(
                file, fieldnames=["product_page_url", "universal_ product_code (upc)", "title",
                                  "product_description", "price_including_tax", "price_excluding_tax",
                                  "number_available", "category", "review_rating", "image_url"])
            writer.writeheader()
        file.close
    except OSError as err:
        print("OS error: {0}".format(err))


def csv_save(tab, category):
    """
    :param tab: tableau des attributs du livre
    :param category: catégorie du livre permettant de trouver
        le bon fichier CSV
    :return: édite le fichier CSV de la catégorie
    """
    with open(f'category/{category}.csv', 'a', encoding="utf-8", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(tab)
