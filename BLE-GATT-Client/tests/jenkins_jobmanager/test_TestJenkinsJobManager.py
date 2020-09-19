import pytest
import pprint

from jenkins_jobmanager.JenkinsJobManager import JenkinsJobManager


@pytest.fixture(scope="class")
def jenkinsManager():
    jenkinsManager = JenkinsJobManager(url='http://localhost:8080', username='admin', password='admin')
    yield jenkinsManager
    del jenkinsManager


@pytest.mark.integration_test
class TestJenkinsJobManager(object):

    @pytest.mark.parametrize('jobName, jobParameter, expectedJobStatus', [
        ('TestJob1-FS', {}, 'SUCCESS'),
        ('TestJob2-FS', {'SUCCESSFUL_BUILD': False}, 'FAILURE'),
        ('TestJob2-FS', {'SUCCESSFUL_BUILD': True}, 'SUCCESS'),
        ('TestJob3-PL', {}, 'SUCCESS'),
        ('TestJob4-PL', {'SUCCESSFUL_BUILD': False}, 'FAILURE'),
        ('TestJob4-PL', {'SUCCESSFUL_BUILD': True}, 'SUCCESS'),
    ])
    def test_jenkinsRequests(self, jenkinsManager, jobName, jobParameter, expectedJobStatus):
        jenkinsManager.runJob(jobName, jobParameter)
        jobStatus = jenkinsManager.getJobStatus(jobName)

        assert jobStatus == expectedJobStatus, 'get wrong status for jobName: {name} with parameters: {parameters} jobStatus: {jobStatus}'.format(name=jobName, parameters=jobParameter, jobStatus=pprint.pformat(jobStatus))
