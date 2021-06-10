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
        return jsonify({"score": getScore(a)})
    except KeyError:
        return 'Invalid input'

    

if __name__ == '__main__':
    app.run(debug=True)

