import serial.tools.list_ports


class SerialCommunicator:
    def __init__(self, serial_port, baudrate):
        self.__serial_port = serial_port
        self.__baudrate = baudrate
        self.__serial = serial.Serial(port=serial_port, baudrate=baudrate)

    def write_to_serial(self, data):
        self.__serial.open()
        self.__serial.write(data)

    def read_from_serial(self):
        return self.__serial.read()

    @staticmethod
    def print_com_ports():
        ports = serial.tools.list_ports.comports()
        for com_ports in ports:
            print(str(com_ports))

