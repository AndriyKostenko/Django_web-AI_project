import time
import numpy as np
import os
import cv2
import pickle
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten, Conv2D, MaxPooling2D
import tensorflow as tf
from tensorflow.keras.callbacks import TensorBoard

DATADIR = "/home/andriy/Downloads/kagglecatsanddogs_5340/PetImages"
CATEGORIES = ["Dog", "Cat"]
IMG_SIZE = 50  # resizing the shape

training_data = []


def create_training_data():
    for category in CATEGORIES:
        path = os.path.join(DATADIR, category)  # path to cats of dogs dir
        class_num = CATEGORIES.index(category)
        for img in os.listdir(path):
            try:
                img_array = cv2.imread(os.path.join(path, img), cv2.IMREAD_GRAYSCALE)
                new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
                training_data.append([new_array, class_num])
            except Exception as e:
                print(f' Something went wrong: {e.args}.')

create_training_data()

X = []
Y = []

for features, label in training_data:
    X.append(features)
    Y.append(label)

X = np.array(X).reshape(-1, IMG_SIZE, IMG_SIZE, 1)


pickle_out = open("X.pickle", "wb")
pickle_out_2 = open("Y.pickle", "wb")

pickle.dump(X, pickle_out)
pickle.dump(Y, pickle_out_2)

pickle_out.close()
pickle_out_2.close()


########################################################################################3




tensorboard = TensorBoard(log_dir='logs/'.format())

gpu_options = tf.compat.v1.GPUOptions(per_process_gpu_memory_fraction=0.333)
sess = tf.compat.v1.Session(config=tf.compat.v1.ConfigProto(gpu_options=gpu_options))

pickle_in = open('X.pickle', 'rb')
pickle_in_2 = open('Y.pickle', 'rb')

X = pickle.load(pickle_in)
Y = pickle.load(pickle_in_2)

X = np.array(X)
Y = np.array(Y)

X = X/255.0

dense_layers = [1]
layer_sizes = [64]
conv_layers = [3]

for dense_layer in dense_layers:
    for layer_size in layer_sizes:
        for conv_layer in conv_layers:
            NAME = '{}-conv-{}-nodes-{}-dense-{}'.format(conv_layer, layer_size, dense_layer, int(time.time()))
            tensorboard = TensorBoard(log_dir='logs/'.format())
            model = Sequential()

            model.add(Conv2D(64, (3, 3), input_shape=X.shape[1:]))  #64 units followed by window size
            model.add(Activation("relu"))
            model.add(MaxPooling2D(pool_size=(2,2)))

            for l in range(conv_layer-1):
                model.add(Conv2D(64, (3, 3)))
                model.add(Activation("relu"))
                model.add(MaxPooling2D(pool_size=(2,2)))

            model.add(Flatten())
            for l in range(dense_layer):
                model.add(Dense(512))
                model.add(Activation("relu"))
                model.add(Dropout(0.2))



            model.add(Dense(1))  # output layer
            model.add(Activation('sigmoid'))

            model.compile(loss="binary_crossentropy",
                          optimizer="adam",
                          metrics=['accuracy'])

            model.fit(X, Y, batch_size=32, epochs=10, validation_split=0.1, callbacks=[tensorboard])  #debenps on the size of data i'v maked 10 rounds
pickle_in.close()
pickle_in_2.close()
model.save('cat_&_others.model')

############################################################################3





