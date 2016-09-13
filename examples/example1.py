from sandbox import Sandbox

PATH_TO_EXECUTABLE = 'ls'

sandbox = Sandbox(proc=0, cpu=10, mem=1048576, file=10)
stdout, stderr = sandbox.execp(PATH_TO_EXECUTABLE)
print stdout
