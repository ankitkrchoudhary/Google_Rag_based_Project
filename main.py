import google.generativeai as genai
import os
os.environ['GOOGLE_API_KEY']="AIzaSyAqcI1RyrbBx4M_079FKItccOfILOgr72c"
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])

# for m in genai.list_models():          ##This helps to find out the all the models
#     if 'generateContent' in m.supported_generation_methods:
#         print(m.name)

model = genai.GenerativeModel("gemini-1.5-pro-latest")
response=model.generate_content("What is meaning of life?")
print(response.text)