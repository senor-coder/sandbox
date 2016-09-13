from subprocess import Popen, PIPE
from exceptions import *
from flags import *

'''
    A class to configure a sandbox environment and run any executable in the constrained environment.
'''


class Sandbox:
    def __init__(self, proc=None, file=None, cpu=None, mem=None):
        """
        :param proc: Number of processes allowed
        :param file: Max number of files to be allowed
        :param cpu: Max seconds of CPU time
        :param mem: Max address space in bytes. (STACK , HEAP and ADDRESS SPACE)
        :param flags: Other optional flags.
        """
        self.proc = proc
        self.file = file
        self.mem = mem
        self.cpu = cpu

    def __get_proc_config(self):
        return 'proc=' + str(self.proc) if self.proc is not None else None

    def __get_file_config(self):
        return 'file=' + str(self.file) if self.file is not None else None

    def __get_mem_config(self):
        return 'mem=' + str(self.mem) if self.mem is not None else None

    def __get_cpu_config(self):
        return 'cpu=' + str(self.cpu) if self.cpu is not None else None

    '''
        Get the output of the executable by running in the sandbox environment.
    '''

    def __get_constraints(self):
        return filter(lambda x: x is not None, [
            self.__get_file_config(),
            self.__get_proc_config(),
            self.__get_mem_config(),
            self.__get_cpu_config()
        ])

    def __get_command(self, cmd, path=True):
        flags = [EXECVP_FLAG] if path else []
        return ['python', '-m', 'sandbox.env', 'cmd=' + str(cmd)] + self.__get_constraints() + flags

    def __exec(self, cmd):
        """
        :param cmd: Path to the executable
        :return: output of the executable
        """

        p = Popen(cmd, stdout=PIPE, stderr=PIPE)
        output, error = p.communicate()
        if p.returncode == -11:
            raise OutOfMemoryException()

        elif p.returncode == -24:
            raise TimeoutException()

        elif p.returncode != 0:
            error = '' if error is None else error
            raise ProcessErrorException(
                'Process ended with an error code: ' + str(p.returncode) + '\nERROR:\n' + error)
        return output, error

    def execv(self, cmd):
        return self.__exec(self.__get_command(cmd, path=False))

    def execp(self, cmd):
        return self.__exec(self.__get_command(cmd, path=True))
