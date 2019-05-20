# Used for heroku as a flask app
import subprocess
import sys
import numpy

def install(package):
    subprocess.call([sys.executable, "-m", "pip", "install", package])
install("Flask")
subprocess.call(["cython","game.pyx","-3","--include-dir",numpy.get_include()])
from flask import Flask,redirect
import os

app = Flask(__name__, static_url_path="", static_folder=".")
@app.route("/")
def home():
    return redirect("http://webmsgr.github.io/feathergame")
app.run("0.0.0.0",os.environ["PORT"])
