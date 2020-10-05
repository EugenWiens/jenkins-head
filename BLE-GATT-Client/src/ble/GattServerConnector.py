import pygatt
import logging


class GattServerConnector(object):

    __rgbMap = {
        'SUCCESS': {
            'red': bytearray('200', 'utf-8'),
            'green': bytearray('200', 'utf-8'),
            'blue': bytearray('200', 'utf-8')
        },
        'FAILURE': {
            'red': bytearray('255', 'utf-8'),
            'green': bytearray('0', 'utf-8'),
            'blue': bytearray('0', 'utf-8')
        },
    }

    __redUuid           = '2e252e00-2f8b-4326-91de-26742dda4aa7'
    __greenUuid         = '6aeba5cd-4476-43b6-830b-021109ae6dea'
    __blueUuid          = '46f27bf3-5b1c-403e-bc20-90934a784e66'
    __brightnessUuid    = 'fc75589b-54ae-4b28-b54d-a35979f42b39'

    def __init__(self, bleAddress: str):
        self.__bluethoothAdapter = None
        self.__bleAddress = bleAddress

    def sendStatus(self, status: str):
        rgbDict = self.__rgbMap[status]
        if rgbDict:
            self.__setRgbValues(rgbDict['red'], rgbDict['green'], rgbDict['blue'])

    def __setRgbValues(self, red: str, green: str, blue: str):
        try:
            self.__handleBluetoothConnection()

            self.__device.char_write(self.__redUuid, red)
            self.__device.char_write(self.__greenUuid, green)
            self.__device.char_write(self.__blueUuid, blue)
        except Exception as exception:
            logging.debug('Error on write: ' + str(exception))

    def __handleBluetoothConnection(self):
        if self.__bluethoothAdapter is None:
            self.__bluethoothAdapter = pygatt.GATTToolBackend()
            self.__bluethoothAdapter.start()

            self.__device = self.__bluethoothAdapter.connect(self.__bleAddress)

    def __del__(self):
        self.__bluethoothAdapter.stop()
