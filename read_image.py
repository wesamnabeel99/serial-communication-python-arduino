from PIL import Image


def read_image_pixels(image_path):
    image = Image.open(image_path)
    return image.getdata()

