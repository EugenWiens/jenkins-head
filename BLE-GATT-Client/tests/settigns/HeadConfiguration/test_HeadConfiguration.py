import os
import pytest

from contextlib import contextmanager
from settings.ConfigurationHandler import ConfigurationHandler
from settings.HeadConfiguration import HeadConfiguration


@contextmanager
def doesNotRaise():
    yield


@pytest.mark.unit_test
class TestHeadConfiguration(object):

    @pytest.mark.parametrize('file2Test, expectation', [
        ('inputFiles/configuration_content_ok.yaml', doesNotRaise()),
        ('inputFiles/headFiles/wrong_head_key_name_config.yaml', pytest.raises(Exception, match='Key: name not found in')),
        ('inputFiles/headFiles/wrong_head_key_ble_mac_config.yaml', pytest.raises(Exception, match='Key: ble_mac not found in')),
        ('inputFiles/headFiles/wrong_head_key_jobs_config.yaml', pytest.raises(Exception, match='Key: jobs not found in')),
        ('inputFiles/serverFiles/wrong_server_key_authentication_config.yaml', pytest.raises(Exception, match='Key: authentication not found in')),
        ('inputFiles/serverFiles/wrong_server_key_name_config.yaml', pytest.raises(Exception, match='Key: name not found in')),
        ('inputFiles/serverFiles/wrong_server_key_url_config.yaml', pytest.raises(Exception, match='Key: url not found in')),
        ('inputFiles/serverFiles/missing_server_key_authentication_config.yaml', pytest.raises(Exception, match='Key: authentication not found in')),
        ('inputFiles/serverFiles/missing_server_key_name_config.yaml', pytest.raises(Exception, match='Key: name not found in')),
        ('inputFiles/serverFiles/missing_server_key_url_config.yaml', pytest.raises(Exception, match='Key: url not found in')),
        ('inputFiles/serverFiles/wrong_server_referenced.yaml', pytest.raises(Exception, match='Required server: jenkins_server_3 not provided in the server section:'))
    ])
    def test_HeadConfigurationErrorHandling(self, file2Test, expectation):
        fileName = self.__getFilePathRelative2ThisTest(file2Test)
        with expectation:
            configurationHandler = ConfigurationHandler(fileName)
            listOfHeadObjects = configurationHandler.getListOfHeadConfigurationObjects()
            listOfHeadObjects

    @pytest.mark.parametrize('file2Test, length', [
        ('inputFiles/configuration_content_ok.yaml', 1),
        ('inputFiles/headFiles/content_one_head.yaml', 1),
        ('inputFiles/headFiles/content_five_heads.yaml', 5),
        ('inputFiles/headFiles/content_ten_heads.yaml', 10),
    ])
    def test_HeadConfigurationContentTest(self, file2Test, length):
        fileName = self.__getFilePathRelative2ThisTest(file2Test)

        configurationHandler = ConfigurationHandler(fileName)
        listOfHeadObjects = configurationHandler.getListOfHeadConfigurationObjects()

        assert len(listOfHeadObjects) == length, 'wrong head length'

        for head in listOfHeadObjects:
            name = head.getName()
            bleMac = head.getBleMac()
            index = listOfHeadObjects.index(head) + 1
            listOfServers = head.getJobList()

            assert type(listOfServers) is dict, 'job object is not a dict'
            assert len(listOfServers) == 1, 'wrong job length in head: ' + name

            assert name == 'jenkins_head_{0}'.format(index), 'wrong head name'
            assert bleMac == '00:11:22:33:FF:{0:02d}'.format(index), 'wrong head ble mac'

            for serverName, jobList in listOfServers.items():
                assert len(jobList) == index, 'wrong job length in head: ' + name

                for jobValue in jobList:
                    jobParts = jobValue.split('/')
                    jobIndex = jobList.index(jobValue) + 1

                    assert jobParts[0] == 'job{0}'.format(jobIndex), 'wrong job prefix'
                    assert jobParts[1] == 'jenkins_head_{0}'.format(index), 'wrong job head name'
                    assert jobParts[2] == serverName, 'wrong job postfix'

    @pytest.mark.parametrize('file2Test, length', [
        ('inputFiles/configuration_content_ok.yaml', 1),
        ('inputFiles/serverFiles/configuration_content_ok_3_unused_server.yaml', 1),
        ('inputFiles/headFiles/content_one_head.yaml', 1),
        ('inputFiles/headFiles/content_five_heads.yaml', 5),
        ('inputFiles/headFiles/content_ten_heads.yaml', 10)
    ])
    def test_HeadConfigurationGetServerTest(self, file2Test, length):
        fileName = self.__getFilePathRelative2ThisTest(file2Test)

        configurationHandler = ConfigurationHandler(fileName)
        listOfHeadObjects = configurationHandler.getListOfHeadConfigurationObjects()

        assert len(listOfHeadObjects) > 0, 'wrong head length'

        for head in listOfHeadObjects:
            listOfServers = head.getJobList()

            for server in listOfServers:
                serverConfig = head.getServerParameter(server)

                assert serverConfig
                assert type(serverConfig) is dict, 'server config is not a dict'

    def __getFilePathRelative2ThisTest(self, filePath):
        return os.path.dirname(__file__) + '/' + filePath
