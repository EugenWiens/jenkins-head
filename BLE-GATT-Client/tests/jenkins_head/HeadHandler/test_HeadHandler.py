import pytest
import os

from unittest.mock import Mock
from settings.ConfigurationHandler import ConfigurationHandler
from jenkins_head.HeadHandler import HeadHandler
import jenkins_jobmanager.JenkinsJobManager


def mock_JenkinsJobManager(*args, **kwargs):
    mockObject = Mock()
    mockObject.getJobStatus.return_value = 'SUCCESS'
    return mockObject

@pytest.mark.unit_test
class TestHeadHandler:
    def test_statusDessitionsOneJob(self, monkeypatch):
        with monkeypatch.context() as m:
            m.setattr(jenkins_jobmanager.JenkinsJobManager, "JenkinsJobManager", mock_JenkinsJobManager)

            configurationHandler = ConfigurationHandler(os.path.join(os.path.dirname(__file__), './inputFiles/head_config_one_job.yaml'))
            headConfigurationList = configurationHandler.getListOfHeadConfigurationObjects()

            headHandler = HeadHandler(headConfigurationList[0])


            headHandler.check()
