import os
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

import numpy as np


class PredictionPipeline:

    def __init__(self, filename):
        self.filename = filename

    def Predict(self):
        model = load_model(os.path.join('model','model.h5'))

        imagename = self.filename
        test_image = image.load_img(imagename, target_size = (224,224))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis = 0)

        '''   np.expand_dims(test_image, axis=0): The expand_dims function from NumPy adds an extra dimension to the array. In this case, it adds a new dimension at the beginning (axis 0). This is often done to prepare the image data for input to a neural network, which typically expects a batch of images as input.   '''

        result = np.argmax(model.predict(test_image), axis=0)

        if result[0]==1:
            prediction = 'Tumor'
            return [f"image :  {prediction}"]
        else :
            prediction = 'Normal'
            return [f"image :  {prediction}"]
