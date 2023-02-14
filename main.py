from read_mnist import read_mnist_image
from read_image import read_image_pixels

read_mnist_image("dataset/mnist_test.csv",row_index=18)
pixels = read_image_pixels("temp/sample.png")

for pixel in pixels:
    print(pixel)
