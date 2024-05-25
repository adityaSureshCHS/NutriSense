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
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer sk-proj-SzMfABSwegh6iXPuHjndT3BlbkFJs3o3bUb6FdlYRoMUAIyM"
        }
        
        payload = {
            "model": "gpt-4o",
            "messages": [
                {
                    "role":"user",
                    "content": [
                        {
                            "type": "text",
                            "text": "What is the text paragraph inside of the ingredients section?"
                        },
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": data
                            }
                        }
                    ]
                }
            ]
        }
        response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
        print(response.json)
    return render_template("results.html")
