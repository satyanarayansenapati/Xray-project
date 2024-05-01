import os
import urllib.request as request
from zipfile import ZipFile
import tensorflow as tf
from pathlib import Path

from cnnClassifier.entity.config_entity import (PrepareBaseModelConfig)

class PrepareBaseModel:

    #initializing
    def __init__(self, config : PrepareBaseModelConfig):
        self.config = config
    

    #downloading the VGG16 model
    def get_base_model(self):

        '''This function downloads the VGG16 model from the internet'''

        self.model = tf.keras.applications.vgg16.VGG16(
            input_shape=self.config.params_image_size,
            weights= self.config.params_weights,
            include_top= self.config.params_include_top,       
        )

    #saving the base model
          

        self.save_model(path = self.config.base_model_path, model = self.model)

    
    #updating the base model
    @staticmethod
    def prepare_full_model(model, classes, freeze_all, freeze_till, learning_rate):

        '''This model update the base model with mentioned modifications'''

        if freeze_all:
            for layer in model.layers:
                model.trainable = False
        elif (freeze_till is not None) and (freeze_till > 0):
            for layer in model.layers[:-freeze_till]:
                model.trainable = False

        flatten_in = tf.keras.layers.Flatten()(model.output)
        prediction = tf.keras.layers.Dense(
            units=classes,
            activation="softmax"
        )(flatten_in)

        full_model = tf.keras.models.Model(
            inputs=model.input,
            outputs=prediction
        )

        full_model.compile(
            optimizer=tf.keras.optimizers.SGD(learning_rate=learning_rate),
            loss=tf.keras.losses.CategoricalCrossentropy(),
            metrics=["accuracy"]
        )

        full_model.summary()
        return full_model
    
    @staticmethod
    def save_model(path : Path, model : tf.keras.Model):
        '''This function saves the model'''
        model.save(path)
    
    #applying <prepare_full_model> function to create an updated model
    def update_base_model(self):
        self.full_model = self.prepare_full_model(
            model=self.model,
            classes=self.config.params_classes,
            freeze_all=True,
            freeze_till=None,
            learning_rate=self.config.params_learning_rate
        )
    
        #saving the updated model
        self.save_model(path=self.config.base_updated_model_path, model = self.full_model)
