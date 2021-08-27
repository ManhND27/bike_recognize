from GoogleImageScrapper import GoogleImageScraper
import os

#Define file path
webdriver_path = os.path.normpath(os.getcwd()+"/chromedriver_linux64/chromedriver")
image_path = os.path.normpath(os.getcwd()+"\\photos")

#Add new search key into array ["cat","t-shirt","apple","orange","pear","fish"]
search_keys= ["Bike Trek 1.1 Road 2017"]

#Parameters
number_of_images = 1000
headless = False
min_resolution=(0,0)
max_resolution=(9999,9999)

#Main program
for search_key in search_keys:
    image_scrapper = GoogleImageScraper(webdriver_path,image_path,search_key,number_of_images,headless,min_resolution,max_resolution)
    image_urls = image_scrapper.find_image_urls()
    image_scrapper.save_images(image_urls)

#Release resources
del image_scrapper



