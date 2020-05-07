# -*- coding: utf-8 -*-
"""
Created on Mon May  4 16:46:19 2020

@author: LukaszMalucha
"""


import os 
import zipfile
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

from tqdm import tqdm_notebook
from tensorflow.keras.preprocessing.image import ImageDataGenerator


dataset_path="./cats_and_dogs_filtered.zip"

zip_object = zipfile.ZipFile(dataset_path, mode='r')

zip_object.extractall("./")
zip_object.close()



dataset_path_new = "./cats_and_dogs_filtered/"
train_dir = os.path.join(dataset_path_new, "train")
validation_dir = os.path.join(dataset_path_new, "validation")


IMG_SHAPE = (128, 128, 3)


# Custom head as we are prediciting cat/dog only instead of imagenet full spectrum
base_model = tf.keras.applications.MobileNetV2(input_shape=IMG_SHAPE, include_top=False, weights="imagenet")


# Freeze layers of initial network to prevent them from changing
base_model.trainable = False

# Custom head
base_model.output

# Use global average pulling layer to flatter input
global_average_layer = tf.keras.layers.GlobalAveragePooling2D()(base_model.output)
global_average_layer

prediction_layer = tf.keras.layers.Dense(units=1, activation="sigmoid")(global_average_layer)


# Combine base model with custom head


model = tf.keras.models.Model(inputs=base_model.input, outputs=prediction_layer)

model.summary()


model.compile(optimizer=tf.keras.optimizers.RMSprop(lr=0.0001), loss="binary_crossentropy", metrics=["accuracy"])


# Image Data Generator


data_gen_train = ImageDataGenerator(rescale=1/255.)
data_gen_valid = ImageDataGenerator(rescale=1/255.)


train_generator = data_gen_train.flow_from_directory(train_dir, target_size=(128, 128), batch_size=128, class_mode="binary")

valid_generator = data_gen_valid.flow_from_directory(validation_dir, target_size=(128, 128), batch_size=128, class_mode="binary")



model.fit_generator(train_generator, epochs=20, validation_data=valid_generator)


valid_loss, valid_accuracy = model.evaluate_generator(valid_generator)


print("Accuracy after transfer learning: {}".format(valid_accuracy))


# Fine Tuning
#
#base_model.trainable = True
#
#print(f"Number of layers: {len(base_model.layers)}") # 155
#
#fine_tune_at = 100
#
## Freez all layers before 100
#for layer in base_model.layers[:fine_tune_at]:
#    layer.trainable = False



#model.compile(optimizer=tf.keras.optimizers.RMSprop(lr=0.0001), loss="binary_crossentropy", metrics=["accuracy"])
#
#
#model.fit_generator(train_generator, epochs=5, validation_data=valid_generator)
#
#valid_loss, valid_accuracy = model.evaluate_generator(valid_generator)



model_json = model.to_json()
with open("cat_dog_classifier.json", "w") as json_file:
    json_file.write(model_json)


model.save_weights("fashion_model.h5")





















