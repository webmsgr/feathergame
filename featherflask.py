# Used for heroku as a flask app

from flask import Flask,redirect
app = Flask(__name__, static_folder=".")
@app.route("/")
def home():
    return redirect("http://webmsgr.github.io/feathergame")
