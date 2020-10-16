#!/usr/bin/env python3

'''
Description: CNN clasificador de data
Fecha:
'''
import os
import tensorflow as tf

Enable_GPU = False
if Enable_GPU:

    os.environ["CUDA_VISIBLE_DEVICES"] = "0"
    physical_devices = tf.config.experimental.list_physical_devices('GPU')
    tf.config.experimental.set_memory_growth(physical_devices[0], True)
    print('Default GPU Device: {}'.format(tf.test.gpu_device_name()))
    print(tf.test.is_built_with_cuda())

else:
    os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.optimizers import RMSprop
from tensorflow.keras.preprocessing.image import ImageDataGenerator


def model_cnn():
    model = Sequential()
    model.add(Conv2D(filters=32, kernel_size=(3, 3), activation='relu', input_shape=(150, 150, 3)))
    model.add(MaxPooling2D((2, 2)))

    model.add(Conv2D(filters=64, kernel_size=(3, 3), activation='relu', ))
    model.add(MaxPooling2D((2, 2)))

    model.add(Conv2D(filters=128, kernel_size=(3, 3), activation='relu', ))
    model.add(MaxPooling2D((2, 2)))

    model.add(Conv2D(filters=256, kernel_size=(3, 3), activation='relu', ))
    model.add(MaxPooling2D((2, 2)))

    model.add(Flatten())

    model.add(Dense(512, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))

    optimizador = RMSprop(lr=1e-4)
    loss_function = 'binary_crossentropy'

    model.compile(optimizer=optimizador, loss=loss_function, metrics=['acc'])
    model.summary()

    return model


def pre_process_image():
    train_directory = './data_set/training_dataset/'
    train_datagen = ImageDataGenerator(rescale=1. / 255)

    train_generator = train_datagen.flow_from_directory(
        train_directory,
        target_size=(150, 150),
        color_mode="rgb",
        class_mode="binary",
        batch_size=32)

    validation_directory = "./data_set/validation_dataset/"
    validation_datagen = ImageDataGenerator(rescale=1. / 255)

    validation_generator = validation_datagen.flow_from_directory(
        validation_directory,
        target_size=(150, 150),
        color_mode="rgb",
        class_mode="binary",
        batch_size=32)

    return train_generator, validation_generator


def train_model(model, train, validat):
    model.fit_generator(train, steps_per_epoch=62, epochs=30, validation_data=validat, validation_steps=32)
    model.save_weights('model_entrenado.h5')


#nn_model = model_cnn()
#train_data, vali_data = pre_process_image()
#rain_model(nn_model, train_data, vali_data)
