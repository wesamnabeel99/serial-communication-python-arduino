import time

from utils import constants
from lib.read_mnist import read_mnist_image
from lib.serialcommunicator import SerialCommunicator

mnist_image = read_mnist_image(constants.TEST_DATASET_PATH, row_index=352)

try:
    serial_communicator = SerialCommunicator(constants.COM_PORT, constants.BAUDRATE)

    count = 0

    for pixel in mnist_image:
        serial_communicator.write_to_serial(pixel)
        serial_communicator.write_to_serial('\n')

        count = count + 1

    if count != 784:
        raise Exception("some data went missing")


except Exception as e:
    print("an error has occurred while trying to write pixels to the serial")
    print(e)
finally:
    print("program finished")
