import nox
import json

nox.options.sessions = ["lint", "tests"]


@nox.session
def lint(session):
    """run linter for this project"""
    session.install("flake8")
    flakeArguments = []

    with open('.vscode/settings.json') as jsonFile:
        settingsData = json.load(jsonFile)
        flakeArguments = settingsData.get('python.linting.flake8Args', [])

    session.run("flake8", "src", *flakeArguments)


@nox.session(name="dev-venv")
def createVirtualEnvironmentForDevelopment(session):
    """create a virtual environment for the development"""
    session.install("pytest")
    session.install("pytest-cov")
    session.install("flake8")
    # same as pip install .
    session.install("-e", ".")
    session.log("environment is completely installed, please call the following command to use it:")
    session.log("source .nox/dev-venv/bin/activate")


@nox.session
def build(session):
    """build: what ever sdist and bdist_wheels do :)"""
    session.install("setuptools", "wheel", "twinebdist_wheel")

    # python setup.py sdist bdist_wheel && pip install .'
    # session.run(?)
    pass


@nox.session
def tests(session):
    """run tests for this project"""
    session.install("pytest")
    session.install("pytest-cov")
    session.install("-e", ".")

    session.run("pytest", "tests", "--cov=./src", "--cov-branch", "--cov-report=xml", *session.posargs)


@nox.session(name="deploy-test-pypi")
def deployToTestPyPi(session):
    """deploy this package for testing to the pypi test server"""
    # python -m twine upload --repository testpypi'
    pass


@nox.session(name="deploy-pypi")
def deploy(session):
    """deploy this package to the official pypi server"""
    # python -m twine upload --repository testpypi'
    pass


@nox.session(python=False)
def distclean(session):
    """this command removes all auto generated files"""
    foldersToRemove = [
        '.nox'
    ]

    session.run('rm', '-Rf', *foldersToRemove)
