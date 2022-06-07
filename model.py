import matplotlib.pyplot as plt
#import keras
from sklearn.preprocessing import OneHotEncoder
from keras.models import Sequential
from keras.layers import Dense, Conv2D , MaxPool2D , Flatten , Dropout 
from keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.optimizers import Adam
from sklearn.metrics import classification_report,confusion_matrix
#import tensorflow as tf
import cv2
from keras.preprocessing import image
from keras.applications.inception_v3 import InceptionV3
import os, random, sys, csv
import numpy as np
import matplotlib.pyplot as plt
#from preprocessing import *


#x_train, y_train = get_data()
#count=0
#full = np.array([])
#for image in x_train:
#    print(image)
#    np.append(full, image)
#    count+=1

#np.savez('training_data.npz', full)

data = np.load('training_data.npz')
print(data)
print('hi')
for item in data.files:
    print(item)
base_model = InceptionV3(include_top=False, weights="imagenet", classes=195)
optimizer = Adam(lr=0.00001)
base_model.compile(optimizer, loss='categorical_crossentropy', metrics=['accuracy'])
base_model.fit(x_train, y_train, batch_size=150, epochs=100)
base_model.save()

