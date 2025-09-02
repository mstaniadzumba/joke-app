from flask import Flask, jsonify,request
from flask_cors import CORS
import requests
import sqlite3
from database.db import insert_joke, init_db

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return {"message" : "Welcome to the joke API!"}

@app.route("/joke")
def get_joke():

    try:
        response = requests.get("https://official-joke-api.appspot.com/random_joke")
        response.raise_for_status()#check for http erros
        joke_data = response.json()
        return jsonify({
            "setup": joke_data["setup"],
            "punchline": joke_data["punchline"]
            })

    except requests.RequestException:
            return jsonify({"error": "could not fetch a joke at this time"}), 500



@app.route("/user-joke", methods=["POST"])
def add_joke():
    data = request.get_json()
    setup = data['setup']
    punchline = data['punchline']
    init_db()
    insert_joke(setup, punchline)

    return jsonify({"message": "Joke inserted successfully"}), 200



if __name__ == "__main__":
    app.run(debug=True)