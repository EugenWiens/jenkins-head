class GattServerConnector(object):

    __rgbMap = {
        'SUCCESS': {
            'red': 0,
            'green': 255,
            'blue': 0
        },
        'FAILURE': {
            'red': 255,
            'green': 0,
            'blue': 0
        },
    }

    def __init__(self, bleAddress: str):
        self.__bleAddress = bleAddress

    def sendStatus(self, status: str):
        rgbDict = self.__rgbMap[status]
        if rgbDict:
            self.__setRgbValues(rgbDict['red'], rgbDict['green'], rgbDict['blue'])

    def __setRgbValues(self, red: int, green: int, blue: int):
        pass
