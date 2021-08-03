from builtins import len

import pandas as pd
import numpy as np

#df = pd.read_csv("../data/bike_brand_model_type_year.csv")
df = pd.read_csv("../data/brand_model_type_year.csv")
print(df.head())

arrayList = np.array([df["brand"], np.zeros(len(df["brand"])), df["model"], np.zeros(len(df["model"])), df["type"],
                      np.zeros(len(df["type"])), df["year"]])

brands = arrayList[0]
models = arrayList[2]
listBrand = [brands[0]]
countBrand = 1
countModel = 1
model = open("../data/model.txt", "w+")
model.write("{} , {}\n".format(countBrand, models[0]))
for i in range(0, len(brands) - 1):
    arrayList[1][i] = countBrand
    if brands[i + 1] != brands[i]:
        listBrand.append(brands[i + 1])
        countBrand += 1
    arrayList[3][i] = i
    if models[i + 1] != models[i]:
        countModel += 1
        model.write("{} , {}\n".format(countBrand, models[i + 1]))

print("{} , {}, {}".format(countBrand, countModel, len(df["brand"])))

