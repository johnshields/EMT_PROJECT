"""
Code References:
https://flask.palletsprojects.com/en/1.1.x/quickstart/#a-minimal-application
https://web.microsoftstream.com/video/05d8b607-56c3-44a8-9539-c940257e43d8?referrer=https:%2F%2Flearnonline.gmit.ie%2F
https://web.microsoftstream.com/video/63704d51-e829-4da9-ab3d-ae73b71ee8f2
https://pythonbasics.org/flask-http-methods/
https://www.tensorflow.org/api_docs/python/tf/keras/models/load_model
https://stackoverflow.com/questions/24808660/sending-a-form-array-to-flask
https://pythonexamples.org/python-list-to-json/

John Shields - G00348436
Web Service App that uses the model to make predictions

# run the web service in cli
set FLASK_APP=web_service.py && python -m flask run
"""

# necessary imports
# convert python lists to JSON
import json
# for loading model
from os import path
# numpy arrays
import numpy as np
# neural networks
import tensorflow.keras as krs
# flask stuff
from flask import request, jsonify, render_template, Flask

# create a new web app
app = Flask(__name__, static_folder="static", template_folder="templates")
app.config["DEBUG"] = True


# add root route
@app.route("/")
def home():
    # have the index.html on home page
    return render_template('index.html')


# method to respond with a power prediction
@app.route("/api/model-playground", methods=["POST"])
def predict_power():
    power = {"success": False}
    # load the model
    model = load_model()
    print(model)
    speed = request.form
    # get entered speed value request
    if speed is not None:
        speed_value = float(speed['value'])
        # takes float value and turns to array
        array_element = np.array([speed_value])
        # puts array into model to have it predict the power
        prediction = model.predict(array_element)
        prdtn = prediction.tolist()
        #  take python list and convert into JSON string
        jsn = json.dumps(prdtn)
        power["response"] = jsn
        # respond with a power prediction
        power["success"] = True
    else:
        pass
    return jsonify(power)


# function to load model from file
# attempts to load the model from the first location in the first try
# if fails it will try look for the file another location
def load_model():
    # local
    try:
        model = krs.models.load_model("mp2.h5")
    except:
        # server/docker
        try:
            model = krs.models.load_model("mp2.h5")
        except:
            print("failed to load model")
            print(path.isfile("mp2.h5"))
    finally:
        return model


# have the app run a localhost on the port 8080
if __name__ == "__main__":
    app.run(host='localhost', port=8080)
