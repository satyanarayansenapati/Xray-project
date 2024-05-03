from flask import Flask, render_template, jsonify, request
import os
from flask_cors import CORS, cross_origin
from cnnClassifier.utilis.common import decodeImage
from cnnClassifier.pipeline.prediction import PredictionPipeline

os.putenv('LANG', 'en_US.UTF-8') 
'''LANG = Language, en_US.UTF-8 = english_US, coded in UTF-8
   This line sets the LANG environment variable to the value 'en_US.UTF-8'''

os.putenv('LC_ALL', 'en_US.UTF-8')
'''The LC_ALL variable controls the locale settings for all aspects of the system, including date formats, currency symbols, and more.
this line sets the LC_ALL environment variable to 'en_US.UTF-8'. '''

#initializing Flask

app = Flask(__name__)
CORS(app)


# receiving and saving user input
class ClientApp:
    def __init__(self):
        self.filename = 'InputImage.jpg'
        self.classifier = PredictionPipeline(self.filename)


# default route

'''The code defines a Flask route using the @app.route("/") decorator. This means that when a user accesses the root URL (i.e., the base URL of the application), the home() function will be executed.'''
@app.route('/', methods=['GET'])
@cross_origin
def home():
    return render_template('index.html')


@app.route("/train", methods=['GET','POST'])
@cross_origin()
def trainRoute():
    #os.system("python main.py")
    os.system("dvc repro")
    return "Training done successfully!"



@app.route("/predict", methods=['POST'])
@cross_origin()
def predictRoute():
    image = request.json['image']
    decodeImage(image, clApp.filename)
    result = clApp.classifier.predict()
    return jsonify(result)


if __name__ == "__main__":
    clApp = ClientApp()

    app.run(host='0.0.0.0', port=8080) #for AWS
