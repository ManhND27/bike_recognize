import sys
import time
import cv2
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import os

from skimage.transform import resize
from sklearn.model_selection import train_test_split

url_path = r'/home/manhnd/src/VMO/bike_recognize/data/data.csv'
url_image = pd.read_csv(url_path)
print(url_image.head())
label_path = r'/home/manhnd/src/VMO/bike_recognize/data/label_brand_model_type.csv'
label = pd.read_csv(label_path)
print(label.head())
# apppend url
base_path = '../data'
array_list = np.array([url_image["brand"], url_image["model"], url_image["type"], url_image["year"], url_image["image_url"]])
array_list_label = np.array([label["brand"], label["model"], label["type"]])
full_path = [os.path.join(base_path, file_name) for file_name in array_list[4]]
print(np.shape(array_list))
print(np.shape(array_list_label))
print(np.shape(full_path))


# read image and resize image
def cvtRGB(img):
    return cv2.cvtColor(img.copy(), cv2.COLOR_BGR2RGB)


labels = []
for j in range(0, len(array_list_label[0])):
    a = [array_list_label[0][j], array_list_label[1][j], array_list_label[2][j]]
    label = " ".join(a)
    labels.append(label)
print(labels)
print(len(labels))

brands = array_list[0]
models = array_list[1]
types = array_list[2]
img_width, img_height, channels = 224, 224, 3
dim = (img_width, img_height)
resized_images = []
label_images = []
for j in range(0, len(labels)):
    count = 0
    for i in range(0, len(brands)):
        check = [brands[i], models[i], types[i]]
        label_data = " ".join(check)
        one_host = np.zeros(len(labels))
        if labels[j] == label_data:
            name = full_path[i]
            image = cv2.imread(name, cv2.IMREAD_UNCHANGED)
            if image is not None and np.shape(image)[0] >= 224 and np.shape(image)[1] >= 224 and np.shape(image)[2] == 3 and count <= 1000:
                image_resize = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
                resized_images.append(image_resize)
                one_host[j] = 1
                label_images.append(one_host)
                count = count + 1
            elif image is not None and np.shape(image)[2] == 3 and count <=1000:
                image_resize = cv2.resize(image, dim, interpolation=cv2.INTER_CUBIC)
                resized_images.append(image_resize)
                one_host[j] = 1
                label_images.append(one_host)
                count = count + 1
plt.imshow(resized_images[0])
print(count)

print(len(resized_images))
print(len(label_images))
print(np.shape(resized_images))
print(np.shape(label_images))

seed = 100
np.random.seed(seed)
np.random.shuffle(resized_images)
np.random.seed(seed)
np.random.shuffle(label_images)

np.savez("../data/data_arr/image_arr.npz", train_images = np.array(resized_images[:12000]), val_images = np.array(resized_images[12000:]), train_labels = np.array(label_images[:12000]), val_labels = np.array(label_images[12000:]))
