# -*- coding: utf-8 -*-
# MLP for Pima Indians Dataset Serialize to JSON and HDF5
import numpy as np
import tensorflow as tf
from keras.preprocessing import image
from keras.models import Sequential
from keras.layers import Dense
from keras.models import model_from_json
import os
import cv2
from PIL import Image
from time import sleep

def percentage():
    image = Image.open('capture.jpg')
    image = image.convert('L')
    threshold = 100
    affected_pixels = 0
    total_pixels = image.width * image.height
    for x in range(image.width):
        for y in range(image.height):
            if image.getpixel((x, y)) < threshold:
                affected_pixels += 1
    
    affected_percentage = (affected_pixels / total_pixels) * 100
    print(f'Affected percentage: {affected_percentage}%')



json_file = open('model1.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
model = model_from_json(loaded_model_json)
# load weights into new model
model.load_weights("model1.h5")
print("Loaded model from disk")

##label=['aneurysms','exudates','hemorrhages','microaneurysms','normal']

def classify(img_file): 
    img_name = img_file
    test_image = image.load_img(img_name, target_size = (128, 128))

    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis=0)
    result = model.predict(test_image)
    print(result)
    a=np.round(result[0][0])
    b=np.round(result[0][1])
    c=np.round(result[0][2])
    d=np.round(result[0][3])
    e=np.round(result[0][4])


    print(a)
    print(b)
    print(c)
    print(d)
    print(e)

    if a == 1:
        prediction = 'aneurysms'
        print(prediction)
        percentage()
        sleep(2)
    elif b == 1:
        prediction = 'exudates'
        print(prediction)
        percentage()
        sleep(2)
    elif c == 1:
        prediction = 'hemorrhages'
        print(prediction)
        percentage()
        sleep(2)
    elif d  == 1:
        prediction = 'microaneurysms'
        print(prediction)
        percentage()
        sleep(2)
    elif e  == 1:
        prediction = 'normal'
        print(prediction)


import os
path = 'data/test'
files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
   for file in f:
     if '.jpg' in file:
       files.append(os.path.join(r, file))

for f in files:
   classify(f)
   print('\n')









##test_image = image.img_to_array(test_image)
##test_image = np.expand_dims(test_image, axis = 0)
##result = loaded_model.predict(test_image)
##print(result)
##fresult=np.max(result)
##label2=label[result.argmax()]
###print(label2)








