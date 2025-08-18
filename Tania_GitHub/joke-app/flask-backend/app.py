from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return {"message" : "Welcome to the joke API!"}

@app.route("/joke")
def get_joke():
    return jsonify({"joke":"Why don’t scientists trust atoms? Because they make up everything!" })

if __name__ == "__main__":
    app.run(debug=True)