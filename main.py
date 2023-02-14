from utils import constants
from lib.read_mnist import read_mnist_image

from lib.serialcommunicator import SerialCommunicator

mnist_image = read_mnist_image(constants.TEST_DATASET_PATH, row_index=18)

try:
    serial_communicator = SerialCommunicator(constants.COM_PORT, constants.BAUDRATE)
    for pixel in mnist_image:
        serial_communicator.write_to_serial(pixel)
        print("wrote %d to the serial" % pixel)
except Exception as e:
    print("an error has occurred while trying to write pixels to the serial")
    print(e)
finally:
    print("done")