import numpy as np
import pandas as pd
import tensorflow as tf
from keras.models import load_model
from keras.preprocessing import image
import os


class PredictPipeline:
    def __init__(self,filename):
        self.filename=filename


    def predict(self):
        model =load_model("artifacts","training","model.h5")
        imagename=self.filename
        test_image=image.load_img(imagename,target_size=(224,224))
        test_image=image.img_to_array(test_image)
        test_image=np.expand_dims(test_image,axis=0)
        result=np.argmax(model.predict(test_image),axis=1)
        print(result)

        if result==0:
            prediction="Healthy"
            return [{"image":prediction}]
        
        elif result==1:
            prediction = 'Coccidiosis'
            return [{ "image" : prediction}]