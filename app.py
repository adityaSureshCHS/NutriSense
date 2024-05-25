import os 
import cv2 as cv
from flask import Flask, request, render_template, url_for, redirect
from openai import OpenAI
import pytesseract

client = OpenAI(
    api_key = os.environ.get("OPENAI_API_KEY")
)

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
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": "What are the ingredients listed in the ingredient section of this image"},
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
