from types import resolve_bases
import flask
from flask import render_template, jsonify
from getScore import getScore

#Initializing a flask app
app = flask.Flask(__name__)

#Creating a default route for the API page that renders the homepage
@app.route("/", methods=['GET'])
def main():
    return render_template("home.html")

#Creating a route that takes in an NBA team and returns required score
@app.route("/<string:a>", methods=['GET'])
def home(a):
    try:
        response = jsonify({"score": getScore(a)})
        response.headers.add("Access-Control-Allow-Origin", "*")
        return response
    except KeyError:
        response = 'Invalid input'
        response.headers.add("Access-Control-Allow-Origin", "*")
        return response

    

if __name__ == '__main__':
    app.run(debug=True)

