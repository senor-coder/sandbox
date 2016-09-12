from sandbox import Sandbox

PATH_TO_EXECUTABLE = '/Users/ashwin/test/infinity'

sandbox = Sandbox(proc=0, file=10,cpu=2,mem=1048576)
print sandbox.exec_output(PATH_TO_EXECUTABLE)
