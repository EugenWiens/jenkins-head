import logging
import yaml
import pprint

from settings.HeadConfiguration import HeadConfiguration
from settings.ConfigurationBaseClass import ConfigurationBaseClass


class ConfigurationHandler(ConfigurationBaseClass):
    """
    This class handels the configuration file. After loading the content this class
    provides getter methods to the content.
    """

    __mServerSectionKey = 'servers'
    __mHeadsSectionKey = 'heads'

    def __init__(self, configurationFilePath):
        self.__mFilePath = configurationFilePath

        with open(configurationFilePath, 'r') as fileHandle:
            configurationContent = yaml.safe_load(fileHandle)

        self.__checkConfigurationFileContent(configurationContent)

        serverList = configurationContent[self.__mServerSectionKey]
        self.__checkServerListContent(serverList)

        self.__mServers = serverList
        self.__mHeads = configurationContent[self.__mHeadsSectionKey]
        listOfHeads = self.__convertHeadsConfig2ListOfHeads()
        self.__checkListOfHeads(listOfHeads)
        self.__mListOfHeads = listOfHeads

    def getListOfHeadConfigurationObjects(self):
        return self.__mListOfHeads

    def __convertHeadsConfig2ListOfHeads(self):
        listOfHeadConfigurationsObjects = []

        for headConfiguration in self.__mHeads:
            listOfHeadConfigurationsObjects.append(HeadConfiguration(headConfiguration, self.__mServers))

        return listOfHeadConfigurationsObjects

    def __checkConfigurationFileContent(self, configurationContent):
        keysToCheck = [
            self.__mServerSectionKey,
            self.__mHeadsSectionKey
        ]

        try:
            self._checkConfigurationStructure(configurationContent, keysToCheck)
        except Exception as error:
            logging.error('Wrong structure in file: ' + self.__mFilePath)
            raise error

        logging.debug('All section are found in file: ' + self.__mFilePath)

    def __checkServerListContent(self, serverList):
        for serverKey, server in serverList.items():
            self._checkServerContent(server)

    def __checkListOfHeads(self, listOfHeads):
        occurrence = {}

        for head in listOfHeads:
            self.__countKey(occurrence, head.getName())
            self.__countKey(occurrence, head.getBleMac())

        for key, value in occurrence.items():
            if value > 1:
                raise Exception('Multiple occurrence of heads found: ' + pprint.pformat(occurrence))

    def __countKey(self, occurrenceDict, key):
        if key in occurrenceDict:
            occurrenceDict[key] += 1
        else:
            occurrenceDict[key] = 1
