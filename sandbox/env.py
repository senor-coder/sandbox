import resource
import sys
import os
from flags import *
from .exceptions import *


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


def execv(command):
    if isinstance(command, list):
        os.execv(command[0], command)
    else:
        os.execv(command, [command])


def execp(command):
    if isinstance(command, list):
        os.execvp(command[0], command)
    else:
        os.execvp(command, [command])


if __name__ == '__main__':
    command = None
    flags = []

    for arg in sys.argv[1:]:
        arg_split = arg.split('=')

        if len(arg_split) == 1:
            flag = arg_split[0].strip()
            if flag in FLAGS:
                flags.append(flag)
        else:
            key, value = arg_split[0], arg_split[1]

            if key == 'cmd':
                command = value.split()

            elif key in resource_mappings:
                resource_mappings[key](value)

            else:
                raise UnknownArgException(key)

    if command is None:
        raise InsufficientInputException()

    if EXECVP_FLAG in flags:
        execp(command)
    else:
        execv(command)
