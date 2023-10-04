import os

import cv2
import openai
from pytesseract import pytesseract

pytesseract.tesseract_cmd = os.environ.get("TESSERACT_PATH")
openai.api_key = os.environ.get("OPENAI_API_KEY")

image = cv2.imread("test_pic.jpg")
text = pytesseract.image_to_string(image)

message = f"Hi ChatGPT! Please, solve the following problems:\n{text}"

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": message}])
print(completion.choices[0].message.content)

print(text)
