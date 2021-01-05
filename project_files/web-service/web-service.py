# Adapted from: https://flask.palletsprojects.com/en/1.1.x/quickstart/#a-minimal-application
# https://web.microsoftstream.com/video/05d8b607-56c3-44a8-9539-c940257e43d8?referrer=https:%2F%2Flearnonline.gmit.ie%2F
# https://web.microsoftstream.com/video/63704d51-e829-4da9-ab3d-ae73b71ee8f2

"""
John Shields - G00348436
"""

# flask for web app
import flask as fl

# create a new web app
app = fl.Flask(__name__)


# add root route
@app.route("/")
def home():
    return app.send_static_file('index.html')
