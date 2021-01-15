# -*- coding: utf-8 -*-
import os
from glob import glob
import pandas as pd
import urllib.request

PATH = os.getcwd()
EXT = "*.csv"
all_csv_files = [file
                 for path, subdir, files in os.walk(PATH)
                 for file in glob(os.path.join(path, EXT))]

col_list=["product_page_url", "universal_ product_code (upc)", "title","product_description"
                             ,"price_including_tax", "price_excluding_tax", "number_available"
                             , "category", "review_rating", "image_url"]
for link in all_csv_files:
    df = pd.read_csv(link,usecols=col_list)
    local_links=(df["image_url"])
    for item in local_links:
        urllib.request.urlretrieve(item, 'images\\'+item.split('/')[-1])