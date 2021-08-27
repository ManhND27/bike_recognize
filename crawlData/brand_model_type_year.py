import csv
from builtins import len
from collections import Counter
import pandas as pd
import numpy as np
import os
from csv import writer
import matplotlib.pylab as plt
import shutil
def read_csv():
    df = pd.read_csv("../data/bike_brand_model_type_year.csv")
    #df = pd.read_csv("../data/brand_model_type_year.csv")
    print(df.head())

    arrayList = np.array([df["brand"], np.zeros(len(df["brand"])), df["model"], np.zeros(len(df["model"])), df["type"],df["year"]])

    brands = arrayList[0]
    models = arrayList[2]
    types = arrayList[4]
    years = arrayList[5]
    listBrand = [brands[0]]
    dict_model = Counter(models)
    countBrand = 1
    length = 1
    #search key to gg image
    full_key = open("../data/brand_model_type_year.txt", "w+")
    full_key_csv =open("../data/brand_model_type_year.csv", "w+")
    writer_full_key = writer(full_key_csv)
    #check number image by count key
    key = open("../data/brand_model_type.txt", "w+")
    key_csv =  open("../data/brand_model_type.csv", "w+")
    writer_key = writer(key_csv)
    full_key.write("{} {} {} {}\n".format(brands[0], models[0], types[0], years[0]))
    for i in range(0, len(brands) - 1):
        arrayList[1][i] = countBrand
        if brands[i + 1] != brands[i]:
            listBrand.append(brands[i + 1])
            countBrand += 1
        if dict_model[models[i]] >= 8:
            full_key.write("Bike {} {} {} {}\n".format(brands[i], models[i], types[i], years[i]))
            full_key_i = [brands[i], models[i], types[i], years[i]]
            writer_full_key.writerow(full_key_i)
            if models[i] != models[i+1]:
                key.write("Bike {} {} {}\n".format(brands[i], models[i], types[i]))
                key_i = [brands[i], models[i], types[i]]
                writer_key.writerow(key_i)
            length += 1
    print("{}".format(length))
    full_key.close()
    full_key_csv.close()
    key.close()
    key_csv.close()

def check_count_image():
    dict = {}
    dict_new = {}
    brand_model_types = []
    key_names = open("../data/brand_model_type.txt", "r")
    lines = key_names.readlines()
    for line in lines:
        line = line.replace("Bike ", "")
        line = line.replace("\n", "")
        brand_model_types.append(line)
    for i in brand_model_types:
        dict["{}".format(i)] = 0
    print(dict)

    FORDER_PATH = r'/home/manhnd/src/VMO/bike_recognize/crawlData/GoogleImageScrapy/photos'
    fileNames = os.listdir(FORDER_PATH)
    for fileName in fileNames:
        fileName = (fileName.split("']")[0]).split(" ")[1:-1]
        fileName = " ".join(fileName)
        for brand_model_type in brand_model_types:
            if fileName == brand_model_type:
                dict["{}".format(brand_model_type)] += 1
    print(dict)
    print(dict.values())
    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0
    count_dict_new = 0
    for item in dict:
        if item.split(" ")[0] == "Trek":
            if dict["{}".format(item)] >= 2200:
                dict_new["{}".format(item)] = dict["{}".format(item)]
                count_dict_new += dict["{}".format(item)]
                count1 += 1
        if item.split(" ")[0] == "Specialized":
            if dict["{}".format(item)] >= 1500:
                dict_new["{}".format(item)] = dict["{}".format(item)]
                count_dict_new += dict["{}".format(item)]
                count2 += 1
        if item.split(" ")[0] == "Giant":
            if dict["{}".format(item)] >= 2200:
                dict_new["{}".format(item)] = dict["{}".format(item)]
                count_dict_new += dict["{}".format(item)]
                count3 += 1
        if item.split(" ")[0] == "Cannondale":
            if dict["{}".format(item)] >= 1400:
                dict_new["{}".format(item)] = dict["{}".format(item)]
                count_dict_new += dict["{}".format(item)]
                count4 += 1
    print("_______Dict new______")
    print(dict_new)
    print("Count1 : {},Count2 : {},Count3 : {},Count4 : {}, {}".format(count1, count2, count3, count4, count_dict_new))
    # plt.bar(*zip(*dict_new.items()))
    # plt.show()
    for fileName in fileNames:
        URL = "/home/manhnd/src/VMO/bike_recognize/crawlData/GoogleImageScrapy/photos/{}".format(fileName)
        DICT_PATH = "/home/manhnd/src/VMO/bike_recognize/data/data_image/{}".format(fileName)
        for item in dict_new:
            # print(item)
            if " ".join(fileName.split(" ")[1:-1]) == item:
                # cv2.imwrite(URL)
                try:
                    shutil.copyfile(URL, DICT_PATH)
                    print("File copied successfully.")
                # If source and destination are same
                except shutil.SameFileError:
                    print("Source and destination represents the same file.")
                # If destination is a directory.
                except IsADirectoryError:
                    print("Destination is a directory.")
                # If there is any permission issue
                except PermissionError:
                    print("Permission denied.")
                # For other errors
                except:
                    print("Error occurred while copying file.")

if __name__ == '__main__':
    # read_csv()
    check_count_image()
