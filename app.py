import os 
from flask import Flask, request, render_template, redirect, url_for
import cv2 as cv
import pytesseract
from openai import OpenAI

client = OpenAI()

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
        print(data)
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": "What are all the ingredients listed under the INGREDIENTS paragraph?"},
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": data,
                            },
                        },
                    ],
                 }
            ],
            max_tokens=300,
        )
        
        
        print(response.choices[0])
    return render_template("results.html")
