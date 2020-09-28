import pprint
import logging

from settings.HeadConfiguration import HeadConfiguration


class ConfigurationBaseClass(object):
    """this base class contains all basic methods for configuration handlong"""

    _mServerNameKey = 'name'
    _mServerUrlKey = 'url'
    _mServerAuthentication = 'authentication'

    def _checkConfigurationStructure(self, configurationConten: HeadConfiguration, mandetoryKeyList: list):

        if configurationConten is not None:
            for keyToCheck in mandetoryKeyList:
                if keyToCheck not in configurationConten:
                    raise Exception('Key: ' + keyToCheck + ' not found in ' + pprint.pformat(configurationConten))
                if not configurationConten[keyToCheck]:
                    raise Exception('Element with key: ' + keyToCheck + ' is empty in ' + pprint.pformat(configurationConten))
        else:
            raise Exception('The configuration content is none Type')

    def _checkServerContent(self, serverConfig: dict):
        keysToCheck = [
            self._mServerAuthentication,
            self._mServerNameKey,
            self._mServerUrlKey
        ]

        try:
            self._checkConfigurationStructure(serverConfig, keysToCheck)
        except Exception as error:
            logging.error('Wrong structure in server entry: ' + pprint.pformat(serverConfig))
            raise error
