import os
import csv


def book_csv_init(book, tab):
    if not os.path.exists('books'):
        os.makedirs('books')
    with open('books/'+book + '.csv', 'w', encoding="utf-8", newline='') as file:
        fields = ["product_page_url", "universal_ product_code (upc)", "title",
                  "product_description", "price_including_tax", "price_excluding_tax",
                  "number_available", "category", "review_rating", "image_url"]
        writer = csv.DictWriter(
            file, fieldnames=fields)
        writer.writeheader()
        dictcomp = {fields[i]: tab[i] for i in range(len(fields))}
        writer.writerow(dictcomp)
    file.close()


def init_csv(category):
    if not os.path.exists('category'):
        os.makedirs('category')
    with open('category/' + category + '.csv', 'w', encoding="utf-8", newline='') as file:
        writer = csv.DictWriter(
            file, fieldnames=["product_page_url", "universal_ product_code (upc)", "title",
                              "product_description", "price_including_tax", "price_excluding_tax",
                              "number_available", "category", "review_rating", "image_url"])
        writer.writeheader()
    file.close


def csv_save(tab, category):
    with open('category/' + category + '.csv', 'a', encoding="utf-8", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(tab)
