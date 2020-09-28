import signal


class SignalHandler:

    __terminationRequested = False

    def __init__(self):
        signal.signal(signal.SIGINT, self.__handleSignal)
        signal.signal(signal.SIGTERM, self.__handleSignal)

    def __handleSignal(self, signum, frame):
        self.__terminationRequested = True

    def isTerminationRequested(self) -> bool:
        return self.__terminationRequested
