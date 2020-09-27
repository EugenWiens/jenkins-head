import jenkins_head_controller
import pytest
import mock
import os

from SignalHandler import SignalHandler
from jenkins_head.HeadsManager import HeadsManager


@pytest.mark.unit_test
class TestMainScript(object):

    @pytest.mark.parametrize('inputParameter, exitCode', [
        ('', 0),
        (['--help'], 0),
        (['--version'], 0),
        (['--log', 'DEBUG'], 0),
        (['--log', 'INFO'], 0),
        (['--log', 'WARNING'], 0),
        (['--log', 'ERROR'], 0),
        (['--log', 'WRONG_LEVEL'], 2),
        (['--wrong-parameter'], 2)
    ])
    @mock.patch.object(SignalHandler, 'isTerminationRequested', return_value=True)
    def test_mainFunction(self, mock_isTerminationRequested, inputParameter, exitCode):

        try:
            jenkins_head_controller.main(inputParameter)
        except Exception as error:
            assert(error)
        except SystemExit as exitException:
            assert(exitException.code == exitCode)

    @pytest.mark.parametrize('inputParameter, configFileName', [
        ([], './jenkins-head.yaml'),
        (['--configuration-file', 'eugen'], 'eugen')
    ])
    @mock.patch('jenkins_head_controller.waitSeconds')
    @mock.patch.object(SignalHandler, 'isTerminationRequested', side_effect=[False, True])
    @mock.patch('jenkins_head.HeadsManager.HeadsManager')
    def test_configurationFileParameter(self, mock_HeadsManager, mock_isTerminationRequested, mock_waitSeconds, inputParameter, configFileName):
        # mock_waitSeconds: this mock is only created to speedup the tests otherwise there is a default delay of 5 seconds
        jenkins_head_controller.main(inputParameter)

        assert mock_HeadsManager.mock_calls == [mock.call(configFileName), mock.call().checkAllHeads()]

    @pytest.mark.parametrize('inputParameter, delay', [
        ([], 5),
        (['--check-delay', '1'], 1),
        (['--check-delay', '3'], 3),
        (['--check-delay', '6'], 6),
        (['--check-delay', '100'], 100)
    ])
    @mock.patch('jenkins_head_controller.waitSeconds')
    @mock.patch.object(SignalHandler, 'isTerminationRequested', side_effect=[False, True])
    @mock.patch.object(HeadsManager, 'checkAllHeads', return_value=True)
    def test_checkDelayParameter(self, mock_checkAllHeads, mock_isTerminationRequested, mock_waitSeconds, inputParameter, delay):

        inputParameter.extend(['--configuration-file', self.__getFilePathRelative2ThisTest('inputFiles/head_config_one_job.yaml')])

        jenkins_head_controller.main(inputParameter)

        mock_checkAllHeads.assert_called_once()
        assert mock_waitSeconds.mock_calls == [mock.call(delay)]

    def __getFilePathRelative2ThisTest(self, filePath):
        return os.path.join(os.path.dirname(__file__), filePath)
