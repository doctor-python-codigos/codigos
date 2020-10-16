

import tensorflow as tf
from keras.preprocessing.image import load_img, img_to_array
from classification_cnn.tutorial import model_cnn

imagen_path = "./data_set/testing_dataset/3.jpg"

img = load_img(imagen_path, target_size=(150, 150))
img = img_to_array(img)
img = img.reshape(1, 150, 150, 3)
img = img.astype('float32')

model = model_cnn()
model.load_weights("model_entrenado.h5")

prediction = model.predict(img)

if prediction == 0:
    print("La imagen corresponde a un gato")
else:
    print("La imagen corresponde a un perro")




