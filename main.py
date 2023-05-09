from utils import constants
from lib.read_mnist import read_mnist_image
from lib.serialcommunicator import SerialCommunicator

sample = int(input("choose row:"))
mnist_image = read_mnist_image(constants.TEST_DATASET_PATH, row_index=sample)

try:
    serial_communicator = SerialCommunicator(constants.COM_PORT, constants.BAUDRATE)

    arduino_output = serial_communicator.read_from_serial()
    print(arduino_output)

    count = 0

    for pixel in mnist_image:
        serial_communicator.write_to_serial(pixel)
        serial_communicator.write_to_serial('\n')
        count = count + 1

        arduino_output = serial_communicator.read_from_serial()

    if count != 784:
        raise Exception("some data went missing")

    arduino_output = serial_communicator.read_from_serial()
    print(arduino_output)

except Exception as e:
    print("an error has occurred while trying to write pixels to the serial")
    print(e)
finally:
    print("program finished")
