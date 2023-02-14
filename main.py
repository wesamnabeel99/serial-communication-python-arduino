from read_mnist import read_mnist_image

from serialcommunicator import SerialCommunicator

mnist_image = read_mnist_image("dataset/mnist_test.csv", row_index=18)

port = "COM3"
baudrate = 9600

try:
    serial_communicator = SerialCommunicator(port, baudrate)
    for pixel in mnist_image:
        serial_communicator.write_to_serial(pixel)
        print("wrote %d to the serial" % pixel)
except Exception as e:
    print("an error has occurred while trying to write pixels to the serial")
    print(e)
finally:
    print("done")