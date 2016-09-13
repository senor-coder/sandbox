class ResourceLimitException(Exception):
    def __init__(self, message):
        Exception.__init__(self, message)


class TimeoutException(ResourceLimitException):
    def __init__(self):
        Exception.__init__(self, 'Time limit exceeded.')


class OutOfMemoryException(ResourceLimitException):
    def __init__(self):
        Exception.__init__(self, 'Memory limit exceeded.')


class ProcessErrorException(Exception):
    def __init__(self, message):
        Exception.__init__(self, message)


class InsufficientInputException(Exception):
    def __init__(self):
        Exception.__init__(self, 'Please supply the cmd attribute')


class UnknownArgException(Exception):
    def __init__(self, arg):
        Exception.__init__(self, 'Unknown argument: ' + arg)
