import mock
import pytest

from SignalHandler import SignalHandler


class TestSingalHandler(object):

    @pytest.mark.parametrize('terminationRequested', [
        True,
        False
    ])
    @mock.patch.object(SignalHandler, '_SignalHandler__terminationRequested', new_callable=mock.PropertyMock)
    def test_singalHandlerGetter(self, mock_terminationRequested, terminationRequested):
        mock_terminationRequested.return_value = terminationRequested

        signalHandler = SignalHandler()

        assert signalHandler.isTerminationRequested() == terminationRequested

    @mock.patch('signal.signal')
    def test_singalHandlerHandlerSignal(self, mock_signal):
        signalHandler = SignalHandler()

        assert mock_signal.call_count == 2

        callArgumentList = mock_signal.mock_calls[0]
        callbackMethod = callArgumentList.args[1]

        callbackMethod(None, None)

        assert signalHandler.isTerminationRequested() is True
