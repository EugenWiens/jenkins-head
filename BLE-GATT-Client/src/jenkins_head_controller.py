#!/usr/bin/env python3
'''
This module is used as entry point for the jenkins-head-controller
'''
import argparse
import logging
import sys
import time


from SignalHandler import SignalHandler

# this 'other' include form is needed, so that it is possible to mock this two modules
import jenkins_head.HeadsManager as headsManager


versionNumber = '0.0.1'

formatMap = {
    'DEBUG': '%(threadName)-12s: %(levelname)-8s %(asctime)s - %(message)s',
    'INFO': '%(asctime)s - %(message)s',
    'WARNING': '%(asctime)s - %(message)s',
    'ERROR': '%(asctime)s - %(message)s'
}


def initArgumentParser(argv):
    global versionNumber
    parser = argparse.ArgumentParser()
    parser.add_argument('--version', action='version', version='%(prog)s ' + versionNumber)
    parser.add_argument(
        '--log',
        dest='logLevel',
        type=str,
        choices=['DEBUG', 'INFO', 'WARNING', 'ERROR'],
        help='set the level of the logging, default=\'INFO\'',
        default='INFO')
    parser.add_argument('--configuration-file', default='./jenkins-head.yaml', help='this parameter provides an other config file for the heads-config')
    parser.add_argument('--check-delay', type=int, default='5', help='the delay between two checks, default is 5 sec')

    return parser.parse_args(argv)


def initLogger(logLevel: str):
    '''
    set up the logging framework regarding the logging level
    '''
    logFormatString = formatMap[logLevel]
    logging.basicConfig(level=logLevel, format=logFormatString)


def waitSeconds(seconds: int):
    time.sleep(seconds)


def main(argv: list):
    arguments = initArgumentParser(argv)
    initLogger(arguments.logLevel)
    signalHandler = SignalHandler()

    logging.info("starting...")

    manager = headsManager.HeadsManager(arguments.configuration_file)

    while not signalHandler.isTerminationRequested():
        manager.checkAllHeads()
        waitSeconds(arguments.check_delay)


if __name__ == "__main__":
    main(sys.argv)
