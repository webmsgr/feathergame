# Used for heroku as a flask app
import subprocess
import sys
import numpy
from hashlib import md5
def install(package):
    subprocess.call([sys.executable, "-m", "pip", "install", package])
def hashie(text):
    r = md5(text.encode())
    return r.hexdigest()
install("Flask")
subprocess.call(["cython","game.pyx","-3","--include-dir",numpy.get_include()])
from flask import Flask,redirect
import os

app = Flask(__name__, static_url_path="", static_folder=".")
@app.route("/")
def home():
    return redirect("http://webmsgr.github.io/feathergame")
@app.route("/hash/<file>")
def hashof(file):
    return hashie(open(file).read())
app.run("0.0.0.0",os.environ["PORT"])
