
from settings.ConfigurationHandler import ConfigurationHandler
from jenkins_head.HeadHandler import HeadHandler


class HeadsManager(object):

    def __init__(self, configFilePath: str):
        self.__listOfHeads = []
        configManager = ConfigurationHandler(configFilePath)
        listOfHeadConfigs = configManager.getListOfHeadConfigurationObjects()

        for headConfig in listOfHeadConfigs:
            self.__listOfHeads.append(HeadHandler(headConfig))

    def checkAllHeads(self):
        for head in self.__listOfHeads:
            head.check()
