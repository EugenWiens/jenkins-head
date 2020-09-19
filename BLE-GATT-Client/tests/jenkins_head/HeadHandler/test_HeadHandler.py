import pytest
import os
import mock

from settings.ConfigurationHandler import ConfigurationHandler
from jenkins_head.HeadHandler import HeadHandler

import jenkins_jobmanager.JenkinsJobManager
import ble.GattServerConnector


@pytest.mark.unit_test
class TestHeadHandler(object):

    @pytest.mark.parametrize('headConfigFile, jenkinsStatus', [
        ('./inputFiles/head_config_one_job.yaml', 'SUCCESS'),
        ('./inputFiles/head_config_one_job.yaml', 'FAILURE'),
        ('./inputFiles/head_config_three_jobs.yaml', 'SUCCESS'),
        ('./inputFiles/head_config_three_jobs.yaml', 'FAILURE')
    ])
    @mock.patch('jenkins_jobmanager.JenkinsJobManager.JenkinsJobManager')
    @mock.patch('ble.GattServerConnector.GattServerConnector')
    def test_HeadHandlerCheck(self, mock_GattServerConnector, mock_JenkinsJobManager, headConfigFile, jenkinsStatus):
        instance = mock_JenkinsJobManager.return_value
        instance.getJobStatus.return_value = jenkinsStatus

        configurationHandler = ConfigurationHandler(os.path.join(os.path.dirname(__file__), headConfigFile))
        headConfigurationList = configurationHandler.getListOfHeadConfigurationObjects()

        headHandler = HeadHandler(headConfigurationList[0])
        headHandler.check()

        assert mock_GattServerConnector.mock_calls == [mock.call('00:11:22:33:FF:01'), mock.call().sendStatus(jenkinsStatus)]
