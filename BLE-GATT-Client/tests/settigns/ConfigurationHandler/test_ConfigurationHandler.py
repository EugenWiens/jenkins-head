import os
import pytest

from contextlib import contextmanager
from settings.ConfigurationHandler import ConfigurationHandler


@contextmanager
def doesNotRaise():
    yield


class TestConfigurationHandler(object):

    @pytest.mark.parametrize('file2Test, expectation', [
        ('thisFileIsNotExists.yaml', pytest.raises(FileNotFoundError)),
        ('inputFiles/configuration_no_content.yaml', pytest.raises(Exception, match='The configuration content is none Type')),
        ('inputFiles/configuration_content_ok.yaml', doesNotRaise()),
        ('inputFiles/configuration_content_ok_2_heads.yaml', doesNotRaise()),
        ('inputFiles/configuration_content_ok_5_heads.yaml', doesNotRaise()),
        ('inputFiles/configuration_wrong_5_same_name_in_heads.yaml', pytest.raises(Exception, match='Multiple occurrence of heads found:')),
        ('inputFiles/configuration_wrong_5_same_blemac_in_heads.yaml', pytest.raises(Exception, match='Multiple occurrence of heads found:')),
        ('inputFiles/basicContent/configuration_content_empty_heads.yaml', pytest.raises(Exception, match='Element with key: heads is empty in')),
        ('inputFiles/basicContent/configuration_content_empty_servers.yaml', pytest.raises(Exception, match='Element with key: servers is empty in')),
        ('inputFiles/basicContent/configuration_content_no_servers.yaml', pytest.raises(Exception, match='Key: servers not found in')),
        ('inputFiles/basicContent/configuration_content_no_heads.yaml', pytest.raises(Exception, match='Key: heads not found in')),
        ('inputFiles/basicContent/configuration_content_wrong_server_config.yaml', pytest.raises(Exception, match='Key: url not found in')),
        ('inputFiles/basicContent/configuration_content_wrong_heads_config.yaml', pytest.raises(Exception, match='Key: name not found in')),
        ('inputFiles/serverFiles/wrong_server_key_authentication_config.yaml', pytest.raises(Exception, match='Key: authentication not found in')),
        ('inputFiles/serverFiles/wrong_server_key_name_config.yaml', pytest.raises(Exception, match='Key: name not found in')),
        ('inputFiles/serverFiles/wrong_server_key_url_config.yaml', pytest.raises(Exception, match='Key: url not found in')),
        ('inputFiles/serverFiles/missing_server_key_authentication_config.yaml', pytest.raises(Exception, match='Key: authentication not found in')),
        ('inputFiles/serverFiles/missing_server_key_name_config.yaml', pytest.raises(Exception, match='Key: name not found in')),
        ('inputFiles/serverFiles/missing_server_key_url_config.yaml', pytest.raises(Exception, match='Key: url not found in'))
    ])
    def test_ConfigurationHandlerErrorHandling(self, file2Test, expectation):
        fileName = self.__getFilePathRelative2ThisTest(file2Test)
        with expectation:
            configurationHandler = ConfigurationHandler(fileName)
            configurationHandler

    def __getFilePathRelative2ThisTest(self, filePath):
        return os.path.dirname(__file__) + '/' + filePath
