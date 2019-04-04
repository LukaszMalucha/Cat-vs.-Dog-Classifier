### Convolutional Neural Network  - Cat or Dog ???

##################################################################### Building the CNN ################################################



### Importing Libraries

from keras.models import Sequential     # initialize
from keras.layers import Conv2D         # saving model
from keras.models import load_model     # Convolution layer
from keras.layers import MaxPooling2D   # Pooling
from keras.layers import Flatten        # Flattening
from keras.layers import Dense          # Fully connected layers for ANN
from keras.layers import Dropout        # Dropout Rate


### Initializing the CNN

classifier = Sequential()

### Step 1 - Convolution 32x3x3

classifier.add(Conv2D(32, (3, 3),                            ## 32 - number of feature detectors, 3-rows and 3-cols                  
                             input_shape=(128, 128, 3),      ## fixed size of image to standardize dataset + 3d array for color img (reverse order for Tensorflow backend)
                             activation = 'relu'))         ## to make sure there is no negative values in pixel maps to have non-linearity


### Step 2 - Max Pooling

classifier.add(MaxPooling2D(pool_size = (2,2)))            ## dims 2x2

classifier.add(Dropout(rate = 0.25))

### Step 2b - add additional convolutional layer for better result (from 50% to 80% accuracy)

classifier.add(Conv2D(32, (3, 3), activation = 'relu'))      ## No input shape as it was already done
classifier.add(MaxPooling2D(pool_size = (2,2)))            ## dims 2x2

classifier.add(Dropout(rate = 0.2))


### Step 2c - add additional convolutional layer for better result (from 80% to 90% accuracy)

classifier.add(Conv2D(64, (3, 3), activation = 'relu'))      ## No input shape as it was already done
classifier.add(MaxPooling2D(pool_size = (2,2)))            ## dims 2x2

classifier.add(Dropout(rate = 0.3))


### Step 2d - add additional convolutional layer for better result (from 80% to 90% accuracy)

classifier.add(Conv2D(128, (3, 3), activation = 'relu'))      ## No input shape as it was already done
classifier.add(MaxPooling2D(pool_size = (2,2)))            ## dims 2x2

classifier.add(Dropout(rate = 0.4))


### Step 3 - Flattening to one single vector

classifier.add(Flatten())


### Step 4 - Full connection

# Hidden layer - 128 as a experience guess

classifier.add(Dense(activation = 'relu', units = 128))


# Output layer - one node

classifier.add(Dense(activation = 'sigmoid', units = 1))  ## softmax for non--binary


### Compile the CNN Model (alternatively optimizer="RMSprop")

classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])


############################################################ Fitting the CNN to the images ###########################################


### From https://keras.io/preprocessing/image/   apply some random transformations on image dataset
### flow_from_directory method code from webpage

from keras.preprocessing.image import ImageDataGenerator 

train_datagen = ImageDataGenerator(rescale=1./255,
                                   rotation_range=40,
                                   width_shift_range=0.2,
                                   height_shift_range=0.2,
                                   shear_range=0.2,
                                   zoom_range=0.2,
                                   horizontal_flip=True)

test_datagen = ImageDataGenerator(rescale=1./255)

training_set = train_datagen.flow_from_directory('dataset/training_set',       ## extraction directory
                                                 target_size=(128, 128),         ## same dims as in cnn
                                                 batch_size=32,
                                                 class_mode='binary')

test_set = test_datagen.flow_from_directory('dataset/test_set',                ## extraction directory
                                            target_size=(128, 128),              ## same dims as in cnn
                                            batch_size=32,
                                            class_mode='binary')



### Fitting Classifier

classifier.fit_generator(training_set,
                         steps_per_epoch=11,            ## train images
                         epochs=10,                     ## approx 30min/epoch on gpu tf backend
                         validation_data=test_set,
                         validation_steps=11)            ## test images




classifier.save('cat_dog_classifier.h5')        


## Acc - 89% Loss - 25%





############################################################## Single Prediction with CNN ##########################################



from skimage.io import imread
from skimage.transform import resize
import numpy as np
     
class_labels = {v: k for k, v in training_set.class_indices.items()}
     
img = imread('FILEPATH') 
img = resize(img,(128,128))
img = np.expand_dims(img,axis=0)
     
if(np.max(img)>1):
        
        img = img/255.0
     
prediction = classifier.predict_classes(img)
     
print (class_labels[prediction[0][0]])








