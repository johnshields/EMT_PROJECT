"""
Code References:
https://flask.palletsprojects.com/en/1.1.x/quickstart/#a-minimal-application
https://web.microsoftstream.com/video/05d8b607-56c3-44a8-9539-c940257e43d8?referrer=https:%2F%2Flearnonline.gmit.ie%2F
https://web.microsoftstream.com/video/63704d51-e829-4da9-ab3d-ae73b71ee8f2
https://pythonbasics.org/flask-http-methods/
https://www.tensorflow.org/api_docs/python/tf/keras/models/load_model
https://stackoverflow.com/questions/24808660/sending-a-form-array-to-flask
https://pythonexamples.org/python-list-to-json/
https://stackoverflow.com/questions/16615444/take-off-from-json-string

John Shields - G00348436

Web Service
Flask App that handles API requests for user input and
uses the model to make predictions to respond to the user

# run the web service in cli
set FLASK_APP=web_service.py && python -m flask run
"""

# convert to JSON
import json

# numpy arrays
import numpy as np
# flask app
from flask import request, jsonify, render_template, Flask
# neural networks
# for loading model
from tensorflow.keras.models import load_model

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
    model = load_model_prediction()
    print(model)
    # get entered speed request
    speed = request.form
    if speed is not None:
        speed_value = float(speed['value'])
        # takes value and turns to array
        array_element = np.array([speed_value])
        # puts array into model to have it predict
        prediction = model.predict(array_element)
        prdtn = prediction.tolist()
        #  take python list and convert into JSON string
        jsn = json.dumps(prdtn)
        # strip out the '[[]]' from the string
        power_response = jsn.strip('[[]]')
        power["response"] = power_response
        # respond with a prediction in JSON
        power["success"] = True
    else:
        pass
    return jsonify(power)


# function to load model from file
# attempts to load the model from the first location in the first try
# if fails it will try look for the file another location
def load_model_prediction():
    try:
        model = load_model("../mp2.h5")
    except:
        try:
            model = load_model("mp2.h5")
        except:
            print("failed to load model")
    finally:
        return model


# have the app run a localhost on the port 5000
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
