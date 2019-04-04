# Cat vs. Dog Image Classifier

### ** REWORK **************************

### Try it yourself:
https://dogcatclassifier.herokuapp.com/classifier


## PROJECT OVERVIEW

Image classifier trained to distinct between cats and dogs images. Convolutional Neural Network was built with Keras & Tensorflow(GPU). 
Heroku-hosted web application was built with Flask framework. <br>

Kaggle Dataset:<br>
https://www.kaggle.com/c/dogs-vs-cats/data

## CONVOLUTIONAL NEURAL NETWORK CHARACTERISTICS

1. Image Input Shape - 128,128,3, activation - relu
2. Three additional Convolutional Layers (batch size - respectively 32,64,128, dropout rate - 0.25,0.2,0.3)
3. Units in hidden layer - 128
4. Compiler - optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy']
5. Acc - 89% Loss - 25% (approx 30min/epoch on GPU)
6. CNN Code Location: deep_learning/ConvolutionalNeuralNetwork.py
## WEB APP
### Main Page
<br>

![predict1](https://user-images.githubusercontent.com/26208598/46571284-fa20c200-c969-11e8-8672-97ff251c882c.PNG)

### Prediction
<br>

![predict2](https://user-images.githubusercontent.com/26208598/46571286-fbea8580-c969-11e8-9f53-a1bad88b780c.PNG)

<br>
## TOOLS, MODULES & TECHNIQUES

##### Python – web development:
flask | Conda | Heroku
##### Python – CNN:
keras | tensorflow | scikit-image | pandas | numpy | h5py

##### Web Development:
HTML | CSS | Bootstrap | Materialize


## INSTALLING REQUIREMENTS (Conda Environment, Cloud9)

wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh<br>
chmod a+x Miniconda3-latest-Linux-x86_64.sh<br>
./Miniconda3-latest-Linux-x86_64.sh<br>

##### NEW TERMINAL

conda create -n py3 python=3 ipython <br>
source activate py3 <br>
pip install --upgrade pip<br>

##### CNN Build

pip install numpy <br>
conda install -c conda-forge tensorflow<br>
pip install keras==2.1.3<br>
pip install scikitlearn <br>
pip install scikit-image<br>

##### Flask App Build

pip install flask<br>
pip install flask-boostrap<br>
pip install Flask-Uploads<br>

pip freeze --local > requirements.txt
<br>
<br>
##### Thank you,

Lukasz Malucha