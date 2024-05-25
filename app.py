import os 
import cv2 as cv
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return "hello world"



