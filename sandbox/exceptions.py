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