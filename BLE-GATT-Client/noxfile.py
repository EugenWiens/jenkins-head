import nox
import json
import tempfile

from time import sleep


nox.options.sessions = ['lint', 'unit-tests']

unitTestDependencies = [
    'pytest',
    'pytest-cov',
    'flake8',
    'mock'
]

integrationTestDependencies = [
    'python-jenkins'
]


@nox.session
def lint(session):
    '''run linter for this project'''
    session.install('flake8')
    flakeArguments = []

    with open('.vscode/settings.json') as jsonFile:
        settingsData = json.load(jsonFile)
        flakeArguments = settingsData.get('python.linting.flake8Args', [])

    session.run('flake8', 'src', *flakeArguments)


@nox.session(name='dev-venv')
def createVirtualEnvironmentForDevelopment(session):
    '''create a virtual environment for the development'''
    session.install(*unitTestDependencies)
    session.install(*integrationTestDependencies)

    # same as pip install .
    session.install('-e', '.')
    session.log('environment is completely installed, please call the following command to use it:')
    session.log('source .nox/dev-venv/bin/activate')


@nox.session
def build(session):
    '''build: what ever sdist and bdist_wheels do :)'''
    session.install('setuptools', 'wheel', 'twinebdist_wheel')

    # python setup.py sdist bdist_wheel && pip install .'
    # session.run(?)
    pass


@nox.session(name='build-jenkins-container')
def buildDocker(session):
    session.run('docker', 'build', './settings/jenkins/', '-t', 'jenkins-test-server:lts', external=True)


@nox.session(name='unit-tests')
def unitTests(session):
    '''run unit tests for this project'''
    session.install(*unitTestDependencies)

    session.install('-e', '.')

    session.run('pytest', '-m', 'unit_test', '--cov=./src', '--cov-branch', '--cov-report=xml', 'tests', *session.posargs)


@nox.session(name='integration-tests')
def integrationTests(session):
    '''run integration tests for this project runs agains a docker image'''
    session.install(*unitTestDependencies)
    session.install(*integrationTestDependencies)
    session.install('-e', '.')

    with tempfile.TemporaryFile(mode='w+') as fp:
        session.run('docker', 'run', '-d', '--rm',
                    '-p', '8080:8080', '-p', '50000:50000',
                    '-v', 'jenkins_home:/var/jenkins_home',
                    'jenkins-test-server:lts',
                    external=True, stdout=fp )

        fp.seek(0)

        shortContainerId = fp.read()[0:8]
        session.log('container started with shortId: ' + shortContainerId)

        session.log('wait for jenkins server is running')
        sleep(10)

        try:
            session.run('pytest', '-m', 'integration_test', 'tests', *session.posargs)
        finally:
            session.run('docker', 'stop', shortContainerId, external=True)


@nox.session(name='deploy-test-pypi')
def deployToTestPyPi(session):
    '''deploy this package for testing to the pypi test server'''
    # python -m twine upload --repository testpypi'
    pass


@nox.session(name='deploy-pypi')
def deploy(session):
    '''deploy this package to the official pypi server'''
    # python -m twine upload --repository testpypi'
    pass


@nox.session(python=False)
def distclean(session):
    '''this command removes all auto generated files'''
    foldersToRemove = [
        '.nox',
        '__pycache__',
        '.pytest_cache'
    ]

    session.run('rm', '-Rf', *foldersToRemove)
