#packages
from flask import Flask, render_template, request, session, redirect, url_for, jsonify
#built-ins
import json, os
from pprint import pprint
#files
from linreg import getPosture

#flask app
app = Flask(__name__)

app.config.update( #sets encryption key for session-cookies
    TESTING=True,
    SECRET_KEY=os.environ["FLASK_KEY"]
)

@app.route("/")
def homepage():
    return "Testing :)))"

@app.route("/api/getPosture/", methods=["GET"])
def manipulateGyroscope():
    pprint(f"Received request: {json.loads(request.json)}")

    return jsonify({
        "isGoodPosture" : getPosture()
    }), 200

if __name__ == "__main__":
    app.run()

