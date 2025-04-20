import PIL.Image
import google.generativeai as genai
import os
os.environ['GOOGLE_API_KEY']="AIzaSyAqcI1RyrbBx4M_079FKItccOfILOgr72c"
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])


model = genai.GenerativeModel("gemini-1.5-flash")

img=PIL.Image.open('OIP.jfif')
# response=model.generate_content(img)
response=model.generate_content(["write a short, engaging blog post based on the image ",img])
response.resolve()

print(response.text)