import subprocess
from subprocess import STDOUT

'''
    A class to configure a sandbox environment and run any executable in the constrained environment.
'''
class Sandbox:
    def __init__(self, proc=None, file=None, cpu=None, a_space=None):
        """
        :param proc: Number of processes allowed
        :param file: Max number of files to be allowed
        :param cpu: Max seconds of CPU time
        :param a_space: Max address space in bytes
        """
        self.proc = proc
        self.file = file
        self.a_space = a_space
        self.cpu = cpu

    def __get_proc_config(self):
        return 'proc=' + str(self.proc) if self.proc is not None else None

    def __get_file_config(self):
        return 'file=' + str(self.file) if self.file is not None else None

    '''
        Get the output of the executable by running in the sandbox environment.
    '''
    def exec_output(self, cmd):
        """
        :param cmd: Path to the executable
        :return: output of the executable
        """
        constraints = [
            self.__get_file_config(),
            self.__get_proc_config()
        ]
        constraints = filter(lambda x: x is not None, constraints)
        try:
            params = ['python', '-m', 'sandbox.env', 'cmd=' + str(cmd)] + constraints
            return subprocess.check_output(params, stderr=STDOUT)
        except subprocess.CalledProcessError as e:
            return "ERROR"
