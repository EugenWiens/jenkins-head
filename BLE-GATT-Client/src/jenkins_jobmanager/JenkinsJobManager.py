
import jenkins
import logging

from time import sleep
from jenkins import JenkinsException


class JenkinsJobManager(object):

    def __init__(self, url: str, username: str, password: str):
        self.__server = jenkins.Jenkins(url, username=username, password=password)
        user = self.__server.get_whoami()
        version = self.__server.get_version()
        print('Connected to server with user ' + str(user) + ' server version is ' + version)

    def runJob(self, jobName: str, jobParameter: dict):
        jobInfo = self.__server.get_job_info(jobName, depth=1)
        nextBuildNumber = jobInfo['nextBuildNumber']

        self.__server.build_job(jobName, jobParameter)
        self.__waitForJobExecution(jobName, nextBuildNumber)

    def getJobStatus(self, jobName: str) -> str:
        self.__waitForJobStatusIsReady(jobName)

        jobInfo = self.__server.get_job_info(jobName, depth=1)
        return jobInfo['lastBuild']['result']

    def __waitForJobExecution(self, jobName: str, buildNumber: int):
        # this delay is needed because of the jenkins status update inertia
        for step in range(20):
            sleep(1)
            try:
                buildInfo = self.__server.get_build_info(jobName, buildNumber)
                if buildInfo['number'] == buildNumber:
                    logging.debug('waited for job: {jobName} {seconds} s'.format(jobName=jobName, seconds=step) )
                    break
            except JenkinsException:
                # still waiting
                pass

    def __waitForJobStatusIsReady(self, jobName: str):
        # this delay is needed because of the jenkins status update inertia
        for step in range(20):
            sleep(1)
            try:
                jobInfo = self.__server.get_job_info(jobName, depth=1)
                if jobInfo['lastBuild']['result']:
                    logging.debug('waited for job: {jobName} {seconds} s'.format(jobName=jobName, seconds=step) )
                    break
            except JenkinsException:
                # still waiting
                pass

    def __del__(self):
        print('delete object')
        del self.__server
