import os, base64

import openai
from PIL import Image

openai.api_key = os.environ.get("OPENAI_API_KEY")


def image_to_png(dir_path, image_name):
    image_path = os.path.join(dir_path, image_name)
    with Image.open(image_path) as img:
        r = img.width/img.height
        img = img.resize((int(412*r), 412)).convert('RGBA')

        name, ext = os.path.splitext(image_name)
        img.save(os.path.join(dir_path, f"{name}.png"), format="PNG")

        if ext != ".png":
            os.remove(image_path)

        return f"{name}.png"


def process_image():
    with open("uploads\\test_formulas.png", "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode('utf-8')

    question = f"What formulas do you see on the image?"

    messages = [
        {"role": "system", "content": "You are a helpful assistant capable of reading and describing images."},
        {"role": "user", "content": question},
        {"role": "assistant", "content": encoded_image, "mime_type": "image/png"}
    ]

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages
    )

    return response


def main():
    response = process_image()
    print(response)


if __name__ == "__main__":
    main()
