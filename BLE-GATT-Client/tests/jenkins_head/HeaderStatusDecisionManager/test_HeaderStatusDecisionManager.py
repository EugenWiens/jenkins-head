import pytest

from jenkins_head.HeaderStatusDecisionManager import HeaderStatusDecisionManager


@pytest.mark.unit_test
class TestHeaderStatusDecisionManager:

    @pytest.mark.parametrize('statusList, expectedDecision', [
        (['SUCCESS'], 'SUCCESS'),
        (['FAILURE'], 'FAILURE'),
        (['SUCCESS', 'FAILURE'], 'FAILURE'),
        (['SUCCESS', 'FAILURE', 'SUCCESS'], 'FAILURE'),
        (['SUCCESS', 'SUCCESS', 'SUCCESS'], 'SUCCESS'),
        (['FAILURE', 'FAILURE', 'FAILURE'], 'FAILURE'),
    ])
    def test_DecisionLogic(self, statusList: list, expectedDecision: str):
        decisionManager = HeaderStatusDecisionManager()

        for status in statusList:
            decisionManager.addStatus(status)

        assert decisionManager.getDecision() == expectedDecision
