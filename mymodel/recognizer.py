from keras.models import load_model
from keras.preprocessing.image import img_to_array, load_img
import numpy as np
from PIL import Image

model = load_model('mymodel\\model.h5')
my_list = ['gorilla', 'orangutan', 'chimpanzee']


def recognizer(img):
    x = Image.open(img)
    x = img_to_array(np.array(x.resize((224, 224))))
    x = np.expand_dims(x, axis=0)
    x /= 255.
    prob = model.predict(x)
    return my_list[np.argmax(prob[0][0])], prob[0][0]*100
