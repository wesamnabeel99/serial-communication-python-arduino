from utils import constants
from lib.read_mnist import read_mnist_image
from lib.serialcommunicator import SerialCommunicator

mnist_image = read_mnist_image(constants.TEST_DATASET_PATH, row_index=20)

try:
    serial_communicator = SerialCommunicator(constants.COM_PORT, constants.BAUDRATE)

    count = 0

    result = serial_communicator.read_from_serial()
    print(result)

    for pixel in mnist_image:
        serial_communicator.write_to_serial(str(pixel))
        count = count + 1

    serial_communicator.write_to_serial("\n")

    result = serial_communicator.read_from_serial()
    print(result)

    if count != 784:
        raise Exception("some data went missing")


except Exception as e:
    print("an error has occurred while trying to write pixels to the serial")
    print(e)
finally:
    print("program finished")
