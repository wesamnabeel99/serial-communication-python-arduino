import serial.tools.list_ports


class SerialCommunicator:
    def __init__(self, serial_port, baudrate):
        self.__serial_port = serial_port
        self.__baudrate = baudrate
        self.__serial = serial.Serial(port=serial_port, baudrate=baudrate)
        self.__serial.close()
        self.__serial.open()

    def write_to_serial(self, data):
        self.__serial.write(bytes(data,'utf-8'))

    def read_from_serial(self):
        return self.__serial.readline().decode('utf-8')

    @staticmethod
    def print_com_ports():
        ports = serial.tools.list_ports.comports()
        for com_ports in ports:
            print(str(com_ports))

    def close(self):
        self.__serial.close()