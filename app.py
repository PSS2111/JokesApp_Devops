from flask import Flask, render_template
import requests

app = Flask(__name__)

API_URL = "https://official-joke-api.appspot.com/random_joke"

@app.route("/")
def home():
    try:
        response = requests.get(API_URL)
        joke = response.json()
    except:
        joke = {"setup": "Error", "punchline": "API failed"}
    return render_template("index.html", joke=joke)

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)