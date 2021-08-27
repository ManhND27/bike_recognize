from re import search

from GoogleImageScrapper import GoogleImageScraper
import os
import pandas as pd
import time
import  random
import threading
from selenium import  webdriver
#Define file path

webdriver_path = os.path.normpath(os.getcwd()+"/chromedriver_linux64/chromedriver")
image_path = os.path.normpath(os.getcwd()+"/photos")

data = pd.read_csv("../../data/brand_model_type_year.txt", header=None)
brand_model_type_year = data.to_numpy()

search_keys = brand_model_type_year[:]

#Parameters
number_of_images = 1000
headless = False
min_resolution=(0,0)
max_resolution=(9999,9999)


def search(search_keys):
    #Main program
    for search_key in search_keys:
        image_scrapper = GoogleImageScraper(webdriver_path,image_path,search_key,number_of_images,headless,min_resolution,max_resolution)
        image_urls = image_scrapper.find_image_urls()
        image_scrapper.save_images(image_urls)
        #Release resources
        del image_scrapper


try:
    print("___Start___")
    t = time.time()
    t1 = threading.Thread(target=search(search_keys[0:250]), args=(webdriver.Chrome(webdriver_path)))
    t2 = threading.Thread(target=search(search_keys[250:450]), args=(webdriver.Chrome(webdriver_path)))
    t3 = threading.Thread(target=search(search_keys[450:650]), args=(webdriver.Chrome(webdriver_path)))
    t4 = threading.Thread(target=search(search_keys[650:]), args=(webdriver.Chrome(webdriver_path)))
    # t1 = threading.Thread(target=search(search_keys[528:620]), args=(webdriver.Chrome(webdriver_path)))
    # t2 = threading.Thread(target=search(search_keys[620:720]), args=(webdriver.Chrome(webdriver_path)))
    # t3 = threading.Thread(target=search(search_keys[720:800]), args=(webdriver.Chrome(webdriver_path)))
    # t4 = threading.Thread(target=search(search_keys[800:]), args=(webdriver.Chrome(webdriver_path)))
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    print("Done in :",time.time() - t)
except:
    print("___ERROR___")


