# from flask_ngrok import run_with_ngrok
from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
from keras.models import model_from_json
from keras.preprocessing import image
import pickle
import cv2
import numpy as np
import matplotlib.pyplot as plt

app_brand_model_type = Flask(__name__)
model = load_model("model_weight/brand_model_type.h5")

labels = ['Cannondale Trail 6 Mountain', "Cannondale Adventure 2 Women's Hybrid", 'Cannondale Quick 4 Road', 'Giant Reign 2 Mountain', 'Giant Defy Advanced 1 Road', 'Giant TCR Advanced 2 Road', 'Giant Simple Single Cruiser', 'Specialized Demo 8 I Mountain', 'Specialized P.3 Mountain', 'Specialized Sirrus Hybrid', 'Specialized Stumpjumper FSR Comp 29er Mountain', 'Trek Fuel EX 7 Mountain', 'Trek 1.2 Road', 'Trek 520 Road', 'Trek 820 Mountain']
img_width, img_height = 224,224
dim = (img_width, img_height)

def predict_val(val_data, model):
  val_input = np.reshape(val_data, (1, img_width, img_height, 3))
  val_input = val_input/255.
  pred = model.predict(val_input)
  class_num = np.argmax(pred)
  return class_num, np.max(pred)
def predict_one_image(img, model):
  img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
  img = np.reshape(img, (1, img_width, img_height, 3))
  img = img/255.
  pred = model.predict(img)
  class_num = np.argmax(pred)
  return class_num, np.max(pred)

def cvtRGB(img):
    return cv2.cvtColor(img.copy(), cv2.COLOR_BGR2RGB)
# test_img = cv2.imread('../input/test-image/Cannondale_Adventure 2 Women_s_Hybrid.jpg')
# pred, probability = predict_one_image(test_img, model)
# print('%s %d%%' % (labels[pred], round(probability, 10) * 100))
# _, ax = plt.subplots(1)
# plt.imshow(cvtRGB(test_img))
# # Turn off tick labels
# ax.set_yticklabels([])
# ax.set_xticklabels([])
# plt.grid(False)
# plt.show()

@app_brand_model_type.route('/')
def index():
    return render_template('index.html', data = 'hey')

@app_brand_model_type.route("/prediction", methods=["POST"])
def prediction():
    img = request.files['img']
    img.save("img.jpg")
    image = cv2.imread("img.jpg")
    pred, probability = predict_one_image(image, model)
    print('%s %d%%' % (labels[pred], round(probability, 10) * 100))
    # data = labels[pred]
    return render_template("prediction.html", data="{} - Accuracy : {}%".format(labels[pred],round(probability * 100, 2)))

if __name__ == "__main__":
    app_brand_model_type.run(port=1289,debug=True)

