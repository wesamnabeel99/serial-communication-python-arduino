import pandas as pd
import matplotlib.pyplot as plt

from utils import constants


def read_mnist_image(file_path, row_index):
    sample_mnist_row = pd.read_csv(file_path, header=None, skiprows=row_index, nrows=1).values[0]

    sample_mnist_image = sample_mnist_row[constants.PIXELS_START_COLUMN:]
    sample_mnist_image_2d = sample_mnist_image.reshape(28, 28)

    plt.figure(1)
    plt.imshow(sample_mnist_image_2d)
    plt.savefig(constants.TEMP_SAVE_PATH)
    plt.show()

    sample_mnist_label = sample_mnist_row[constants.LABEL_COLUMN]
    print("the label of mnist image is %d" % sample_mnist_label)

    return sample_mnist_image
