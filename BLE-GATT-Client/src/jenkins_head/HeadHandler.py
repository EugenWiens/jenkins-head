
from settings.HeadConfiguration import HeadConfiguration
from ble.GattServerConnector import GattServerConnector
from jenkins_head.HeaderStatusDecisionManager import HeaderStatusDecisionManager

import jenkins_jobmanager.JenkinsJobManager as jobmanager


class HeadHandler(object):

    def __init__(self, headConfiguration: HeadConfiguration, gattServerConnector: GattServerConnector):
        self.__headConfiguration = headConfiguration
        self.__gattServerConnector = gattServerConnector
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
