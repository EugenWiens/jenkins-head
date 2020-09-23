
import pytest
import mock

from ble.GattServerConnector import GattServerConnector

# this 'other' include form is needed, so that it is possible to mock this two modules
# import jenkins_jobmanager.JenkinsJobManager as jobmanager


@pytest.mark.unit_test
class TestHeaderStatusDecisionManager(object):

    @pytest.mark.parametrize('status, redValue, greenValue, blueValue', [
        ('SUCCESS', 0, 255, 0),
        ('FAILURE', 255, 0, 0),
        ('FAILURE_WRONG', None, None, None),
        ('SUCCESS_WRONG', None, None, None)
    ])
    @mock.patch.object(GattServerConnector, '_GattServerConnector__setRgbValues')
    def test_SendStatus(self, mock_setRgbValues, status, redValue, greenValue, blueValue):
        gattServerConnector = GattServerConnector('00:00:00:00:00:00')

        if (redValue and greenValue and blueValue) is None:
            with pytest.raises(KeyError):
                gattServerConnector.sendStatus(status)
                assert mock_setRgbValues.called == 0
        else:
            gattServerConnector.sendStatus(status)
            mock_setRgbValues.mock_calls == mock.call(redValue, greenValue, blueValue)
