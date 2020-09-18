
from settings.HeadConfiguration import HeadConfiguration
from jenkins_head.HeaderStatusDecisionManager import HeaderStatusDecisionManager

# this 'other' include form is needed, so that it is possible to mock this two modules
import jenkins_jobmanager.JenkinsJobManager as jobmanager
import ble.GattServerConnector as gattServer


class HeadHandler(object):

    def __init__(self, headConfiguration: HeadConfiguration):
        self.__headConfiguration = headConfiguration
        self.__gattServerConnector = gattServer.GattServerConnector(headConfiguration.getBleMac())
        self.__jobList = self.__headConfiguration.getJobList()

    def check(self):
        decisionManager = HeaderStatusDecisionManager()

        for jobKey in self.__jobList.keys():
            serverConfiguration = self.__headConfiguration.getServerParameter(jobKey)
            url = serverConfiguration['url']
            authentication = serverConfiguration['authentication']
            username = authentication['username']
            secrete = authentication['secret']
            jenkinsJobManager = jobmanager.JenkinsJobManager(url, username, secrete)

            for jobName in self.__jobList[jobKey]:
                status = jenkinsJobManager.getJobStatus(jobName)
                decisionManager.addStatus(status)

        decisionStatus = decisionManager.getDecision()
        self.__gattServerConnector.sendStatus(decisionStatus)
