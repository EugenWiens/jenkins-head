import signal


class SignalHandler:

    def __init__(self):
        self.__terminationRequested = False

        signal.signal(signal.SIGINT, self.__handleSignal)
        signal.signal(signal.SIGTERM, self.__handleSignal)

    def __handleSignal(self, signum, frame):
        self.__terminationRequested = True

    def isTerminationRequested(self):
        return self.__terminationRequested
