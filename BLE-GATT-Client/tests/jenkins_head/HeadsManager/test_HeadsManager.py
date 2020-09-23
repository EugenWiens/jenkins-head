
import pytest
import os
import mock


from jenkins_head.HeadsManager import HeadsManager
from jenkins_head.HeadHandler import HeadHandler


class TestHeadsManager(object):

    @pytest.mark.parametrize('file2Test, elementCount', [
        ('inputFiles/one_head_config.yaml', 1),
        ('inputFiles/three_heads_config.yaml', 3),
        ('inputFiles/five_heads_config.yaml', 5)
    ])
    @mock.patch.object(HeadHandler, 'check')
    def test_HeadsManager(self, mock_check, file2Test, elementCount):
        headsManager = HeadsManager(self.__getFilePathRelative2ThisTest(file2Test))
        headsManager.checkAllHeads()

        assert mock_check.call_count == elementCount

    def __getFilePathRelative2ThisTest(self, filePath):
        return os.path.join(os.path.dirname(__file__), filePath)
