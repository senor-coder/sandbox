import resource
import sys
import os


class InsufficientInputException(Exception):
    def __init__(self):
        Exception.__init__(self, 'Please supply the cmd attribute')


class UnknownArgException(Exception):
    def __init__(self, arg):
        Exception.__init__(self, 'Unknown argument -> ' + arg)


def set_proc_limit(limit):
    limit = int(limit)
    resource.setrlimit(resource.RLIMIT_NPROC, (limit, limit))


def set_file_limit(limit):
    limit = int(limit)
    resource.setrlimit(resource.RLIMIT_NOFILE, (limit, limit))


def set_cpu_limit(limit):
    limit = int(limit)
    resource.setrlimit(resource.RLIMIT_CPU, (limit, limit))


def set_mem_limit(limit):
    limit = int(limit)
    resource.setrlimit(resource.RLIMIT_DATA, (limit, limit))
    resource.setrlimit(resource.RLIMIT_STACK, (limit, limit))
    resource.setrlimit(resource.RLIMIT_AS, (limit, limit))


resource_mappings = {
    # PROCESS LIMIT
    'proc': set_proc_limit,
    # FILE LIMIT
    'file': set_file_limit,
    # CPU_LIMIT
    'cpu': set_cpu_limit,
    # ADDRESS SPACE LIMIT
    'mem': set_mem_limit,
}


def execute(command):
    if isinstance(command, list):
        os.execv(command[0], command)
    else:
        os.execv(command, [command])


if __name__ == '__main__':
    command = None
    for arg in sys.argv[1:]:
        arg_split = arg.split('=')
        key = arg_split[0]
        value = arg_split[1]
        if key == 'cmd':
            command = value
            continue
        if key not in resource_mappings:
            raise UnknownArgException(key)
        resource_mappings[key](value)
    if command is None:
        raise InsufficientInputException()
    execute(command)
