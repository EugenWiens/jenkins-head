import jenkins_head_controller
import pytest

@pytest.mark.unit_test
class TestMainScript():

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
    def test_mainFunction(self, inputParameter, exitCode):
        try:
            jenkins_head_controller.main(inputParameter)
        except Exception as error:
            assert(error)
        except SystemExit as exitException:
            assert(exitException.code == exitCode)
