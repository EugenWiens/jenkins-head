
class HeaderStatusDecisionManager(object):

    __failureStr = 'FAILURE'
    __successStr = 'SUCCESS'

    def __init__(self):
        self.__statusArray = []

    def addStatus(self, status: str):
        self.__statusArray.append(status)

    def getDecision(self) -> str:
        decision = self.__successStr

        if self.__failureStr in self.__statusArray:
            decision = self.__failureStr

        return decision
