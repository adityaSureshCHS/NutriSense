import os 
from flask import Flask, request, render_template, redirect, url_for
import cv2 as cv
import pytesseract

app = Flask(__name__)


@app.route("/")
def main():
    return render_template("main.html", path = url_for("photo"))


@app.route("/photo")
def photo():
    return render_template("photo.html", path = url_for("results"))
    
@app.route("/results", methods=["POST", "GET"])
def results():
    if request.method == 'POST':
        data = request.form['image']
        print(data)
    return render_template("results.html")

