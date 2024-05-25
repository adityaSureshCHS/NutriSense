import os 
import cv2 as cv
from flask import Flask, request, render_template, url_for, redirect
from openai import OpenAI
import pytesseract
import google.generativeai as genai
import PIL.Image
from urllib import request as req
import io
import base64

gemini_key = "AIzaSyCvHRoH7oHsJa8J2D4kZIOJ5qxG4ZNHXm0"
genai.configure(api_key = gemini_key)
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
        global data
        data = request.form['image']
        data = req.urlopen(data).read()
        img = PIL.Image.open(io.BytesIO(data))
        model = genai.GenerativeModel('gemini-pro-vision')
        response = model.generate_content(["Identify the ingredients. List each ingredient. Do not add extra characters, dashes, parenthesis, or commas. List the ingredients", img])
        print(response.text)
        
    return render_template("results.html")
