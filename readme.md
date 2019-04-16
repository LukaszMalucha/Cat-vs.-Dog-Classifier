# Cat vs. Dog Image Classifier


#### [Visit the App](http://www.cork-ai.com/)


<br>

![1](https://user-images.githubusercontent.com/26208598/55568076-e24ab080-56f6-11e9-82e2-ed877c52ff6b.JPG)

<br>


## PROJECT OVERVIEW

Image classifier trained to distinct between cats and dogs images. Convolutional Neural Network was built with Keras & Tensorflow(GPU). 
Heroku-hosted web application was built with Flask framework. <br>

[Kaggle Dataset](https://www.kaggle.com/c/dogs-vs-cats/data)

## CONVOLUTIONAL NEURAL NETWORK CHARACTERISTICS

1. Image Input Shape - 128,128,3, activation - relu
2. Three additional Convolutional Layers (batch size - respectively 32,64,128, dropout rate - 0.25,0.2,0.3)
3. Units in hidden layer - 128
4. Compiler - optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy']
5. Acc - 89% Loss - 25% (approx 30min/epoch on GPU)
6. CNN Code Location: deep_learning/ConvolutionalNeuralNetwork.py


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