import google.generativeai as genai
import PIL.Image
gemini_key = "AIzaSyCvHRoH7oHsJa8J2D4kZIOJ5qxG4ZNHXm0"

genai.configure(api_key = gemini_key)
model = genai.GenerativeModel('gemini-pro-vision')
img = PIL.Image.open("burn.jpg")
response = model.generate_content(["Identify the ingredients. List each ingredient. Do not add extra characters, dashes, parenthesis, or commas. List the ingredients", img])
print(response.text)
