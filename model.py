import os

import openai
from PIL import Image

openai.api_key = os.environ.get("OPENAI_API_KEY")


def image_to_png(dir_path, image_name):
    image_path = os.path.join(dir_path, image_name)
    with Image.open(image_path) as img:
        r = img.height/img.width
        img = img.resize((256, int(256*r))).convert('RGBA')

        name, ext = os.path.splitext(image_name)
        img.save(os.path.join(dir_path, f"{name}.png"), format="PNG")

        if ext != ".png":
            os.remove(image_path)

        return f"{name}.png"


def process_image(dir_path, image_name):
    response = openai.Image.create_edit(
        image=open(os.path.join(dir_path, image_name), "rb"),
        prompt="Hi ChatGPT! Please, find formulas in the uploaded image and create another image, where those formulas are nicely formatted.",
        n=1,
        size="256x256"
    )

    image_url = response['data'][0]['url']
    print(image_url)
