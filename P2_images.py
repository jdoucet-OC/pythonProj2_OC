#!/usr/bin/env python3

import os
from glob import glob
import pandas as pd
import urllib.request


def main():
    """
    :return: toutes les images de livre du site dans
        /images/<image>.jpg
    """

    path = os.getcwd()
    ext = "*.csv"
    all_csv_files = [file
                     for path, subdir, files in os.walk(path)
                     for file in glob(os.path.join(path, ext))
                     if 'category' in path]

    col_list = ["product_page_url", "universal_ product_code (upc)", "title", "product_description",
                "price_including_tax", "price_excluding_tax", "number_available",
                "category", "review_rating", "image_url"]
    ii = 1
    if not os.path.exists('images'):
        os.makedirs('images')
    for link in all_csv_files:
        df = pd.read_csv(link, usecols=col_list)
        local_links = (df["image_url"])
        for item in local_links:
            urllib.request.urlretrieve(item, 'images/'+item.split('/')[-1])
            print('Image '+str(ii)+'/1000')
            ii += 1


if __name__ == "__main__":
    main()
