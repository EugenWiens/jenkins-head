#!/usr/bin/env python3
'''
This module is used as entry point for the jenkins-head-controller
'''
import argparse
import logging
import sys


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
    return parser.parse_args(argv)


def initLogger(logLevel):
    '''
    set up the logging framework regarding the logging level
    '''
    logFormatString = formatMap[logLevel]
    logging.basicConfig(level=logLevel, format=logFormatString)


def main(argv):
    arguments = initArgumentParser(argv)
    initLogger(arguments.logLevel)
    logging.info("starting...")


if __name__ == "__main__":
    main(sys.argv)
