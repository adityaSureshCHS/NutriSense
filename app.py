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
        response = model.generate_content(["Identify the ingredients. List each ingredient. Even if an ingredient is made of more than one word, separate the ingredient. Do not add extra characters, dashes, parenthesis, or commas. List the ingredients", img])
        global list1
        list1 = response.text.split("\n")
        model = genai.GenerativeModel('gemini-pro')
        response2 = model.generate_content(f"Using the following ingredients: {response.text} write a short paragraph explaining what each ingredient is/does, health risks, benefits and why combined they can be either harmful or healthy.")
        
        global list2
        list2 = response2.text.split("\n")
        filter(lambda a: a!= '', list2)
        print(list1)
        print()
        print(list2)
    return render_template("results.html", list1=list1, list2=list2)
        