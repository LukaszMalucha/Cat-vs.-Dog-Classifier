# Cat vs. Dog Image Classifier


#### [Visit the App](https://www.septellar.com/)


<br>

![1](https://user-images.githubusercontent.com/26208598/60211178-72137d00-9856-11e9-90b6-5a6a29094c0a.PNG)

<br>


## PROJECT OVERVIEW

Image classifier trained to distinct between cats and dogs images. Convolutional Neural Network was built with Keras & Tensorflow 2.0(GPU). 
Heroku-hosted web application was built with Flask framework. <br>

[Kaggle Dataset](https://www.kaggle.com/c/dogs-vs-cats/data)

## CONVOLUTIONAL NEURAL NETWORK CHARACTERISTICS

1. Image Input Shape - 128,128,3, activation - relu
2. Transferred Learning from Google MobileNetV2 with customized head
4. Compiler - optimizer = 'RMSprop', loss = 'binary_crossentropy', metrics = ['accuracy']
5. Acc - 92% Loss - 19% (approx 30min/epoch on GPU)
6. CNN Code Location: deep_learning/ConvolutionalNeuralNetwork_V2.py


## TOOLS, MODULES & TECHNIQUES:

##### Travis CI
[![Build Status](https://travis-ci.com/LukaszMalucha/Cat-vs.-Dog-Classifier.svg?branch=master)](https://travis-ci.com/LukaszMalucha/Cat-vs.-Dog-Classifier)

##### Python – web development:
Flask 
##### Python – CNN:
keras | tensorflow | scikit-image | pandas | numpy | h5py
##### Web Development:
HTML | CSS | Bootstrap | Materialize

##### Thank you,

Lukasz Malucha