import matplotlib.pyplot as plt
from sklearn.preprocessing import OneHotEncoder
#import cv2
import os, random, sys, csv
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image, ImageOps, ImageFilter
from tensorflow.keras.utils import to_categorical

def get_data():
    class_names = []
    class_indices = dict()
    class_names = open("class_names.txt", "r").read().split('\n')[:-1]
    print(class_names)

    for count, car_class in enumerate(class_names):
        class_indices[car_class]=count
    class_names = [[c] for c in class_names]
    print(class_names)
    #one_hot_classes = to_categorical(class_names, 196, 'str')
    encoder = OneHotEncoder(sparse=False)
    one_hot_classes = encoder.fit_transform(class_names)
    print((one_hot_classes[0]))

    #[8000, pixel]

    x_train = []
    y_train = []
    class_folder_names_train = next(os.walk("sorted_data/train"))[1]
    for folder_name in class_folder_names_train:
        for f in os.listdir(os.path.join("sorted_data/train/", folder_name)):
            x_train.append(f)
            y_train.append(one_hot_classes[class_indices[folder_name]])
            #print(y_train)
    #print(x_train)
    #print(y_train)
    
    x_test = []
    y_test = []
    class_folder_names_test = next(os.walk("sorted_data/test"))[1]
    for folder_name in class_folder_names_test:
        for f in os.listdir(os.path.join("sorted_data/test/", folder_name)):
            x_test.append(f)
            y_test.append(one_hot_classes[class_indices[folder_name]])#
    

    #preprocess images
    print('start')
    preprocessed_x_train = []
    count = 0
    for img_name in x_train:
        count += 1
        #print(count)
        #print(img_name)
        img_path = 'train_data/'+img_name
        #print(img_path)
        preprocessed_img = preprocess(img_path, 299, 299)
        #plt.imshow(preprocessed_img)
        #plt.show()
        #grayscaled = grayscale(preprocessed_img)
        numpy_img = np.asarray(preprocessed_img)
        #print(numpy_img)
        #image2 = Image.fromarray(numpy_img)
        #plt.imshow(image2)
        #plt.show()

        preprocessed_x_train.append(numpy_img)
        #return preprocessed_x_train, y_train
    """preprocessed_x_test = []
    count = 0
    for img_name in x_test:
        count += 1
        print(count)
        #print(img_name)
        img_path = 'cars_data/cars_test/'+img_name
        preprocessed_img = preprocess(img_path, 299, 299)
        grayscaled = grayscale(preprocessed_img)
        #plt.imshow(grayscaled)
        #plt.show()
        preprocessed_x_test.append(preprocessed_img)"""

    return preprocessed_x_train, y_train#, preprocessed_x_test, y_test

def preprocess(path, target_width, target_height):
    orig_img = Image.open(path)
    
    ratio_w = target_width / orig_img.width
    ratio_h = target_height / orig_img.height
    
    if ratio_w < ratio_h:
        new_width = target_width
        new_height = round(ratio_w * orig_img.height)
    else:
        new_height = target_height
        new_width = round(ratio_h * orig_img.width)

    
    image_resize = orig_img.resize((new_width, new_height), Image.ANTIALIAS)
    background = Image.new('RGBA', (target_width, target_height), (255, 255, 255, 255))
    
    offset = (round((target_width - new_width) / 2), round((target_height - new_height) / 2))
    #print(f'Offset: {offset}')

    background.paste(image_resize, offset)
    new_img = background.convert('RGB')
    #plt.imshow(new_img)
    #plt.show()
    

    #streaking
    pixels = new_img.load()
    if ratio_w < ratio_h:
        for i in range(new_img.size[0]):
            for j in range(offset[1], 0, -1):
                pixels[i,j] = pixels[i, offset[1]]
        
        for i in range(new_img.size[0]):
            for j in range(offset[1]+new_height-1, target_height):
                pixels[i, j] = pixels[i, offset[1]+new_height-1]

    else:
        for j in range(new_img.size[1]):
            for i in range(offset[0], 0, -1):
                pixels[i, j] = pixels[offset[0], j]

        for j in range(new_img.size[1]):
            for i in range(offset[0]+new_width-1, target_width):
                pixels[i, j] = pixels[offset[0]+new_width-1, j]

    #blur on edges
    blurred = new_img.filter(ImageFilter.GaussianBlur(radius = 5))
    
    blurred_pixels = blurred.load()
    if ratio_w < ratio_h:
        for i in range(new_img.size[0]):
            for j in range(offset[1], 0, -1):
                pixels[i,j] = blurred_pixels[i, j]
        
        for i in range(new_img.size[0]):
            for j in range(offset[1]+new_height-1, target_height):
                pixels[i, j] = blurred_pixels[i, j]

    else:
        for j in range(new_img.size[1]):
            for i in range(offset[0], 0, -1):
                pixels[i, j] = blurred_pixels[i, j]

        for j in range(new_img.size[1]):
            for i in range(offset[0]+new_width-1, target_width):
                pixels[i, j] = blurred_pixels[i, j]

    return new_img

def grayscale(og_image):
    return og_image.convert('LA')

get_data()