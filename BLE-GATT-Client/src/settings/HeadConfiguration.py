import pprint

from settings.ConfigurationBaseClass import ConfigurationBaseClass
from settings.HeadConfiguration import HeadConfiguration


class HeadConfiguration(ConfigurationBaseClass):
    """ This class wraps the configuration of one jenkins head. The content is made
    available via the constructor, after which the parameters can be accessed
    using getter methods.
    """

    __mNameKey = 'name'
    __mBleMacKey = 'ble_mac'
    __mJobsKey = 'jobs'

    def __init__(self, headConfiguration: HeadConfiguration, serverAliasesList: list):
        """ wraps the jenkins head configuration and substitute the server alias
        with one of the server configuration provided by serverAliasesList

        headConfiguration -- the configuration of one jenkins head
        serverAliasesList -- a list with server configurations
        """
        self.__checkHeadConfiguration(headConfiguration)
        self.__checkRequiredServerConfiguration(headConfiguration, serverAliasesList)

        self.__mHeadConfiguration = headConfiguration
        self.__mServerConfiguration = self.__removeUnnecessaryServerConfig(headConfiguration, serverAliasesList)

    def getName(self) -> str:
        return self.__mHeadConfiguration[self.__mNameKey]

    def getBleMac(self) -> str:
        return self.__mHeadConfiguration[self.__mBleMacKey]

    def getJobList(self) -> list:
        return self.__mHeadConfiguration[self.__mJobsKey]

    def getServerParameter(self, serverName: str) -> dict:
        return self.__mServerConfiguration

    def __checkRequiredServerConfiguration(self, headConfiguration: HeadConfiguration, serverAliasesList: list):
        requiredServers = headConfiguration[self.__mJobsKey]

        for serverAlias in requiredServers:
            if serverAlias in serverAliasesList:
                serverConfig = serverAliasesList[serverAlias]
                self._checkServerContent(serverConfig)
            else:
                raise Exception('Required server: ' + serverAlias + ' not provided in the server section: ' + pprint.pformat(serverAliasesList))

    def __checkHeadConfiguration(self, headConfiguration: HeadConfiguration):
        keysToCheck = [
            self.__mNameKey,
            self.__mBleMacKey,
            self.__mJobsKey
        ]

        self._checkConfigurationStructure(headConfiguration, keysToCheck)

    def __removeUnnecessaryServerConfig(self, headConfiguration: HeadConfiguration, serverAliasesList: list)->list:
        requiredSevers = headConfiguration[self.__mJobsKey]
        cleanServerAliasesList = {}

        for serverAlias in serverAliasesList:
            if serverAlias in requiredSevers:
                serverConfig = serverAliasesList[serverAlias]
                self._checkServerContent(serverConfig)
                cleanServerAliasesList.update(serverConfig)

        return cleanServerAliasesList
