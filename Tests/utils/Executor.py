import sys
import subprocess

PYTHON_PATH = sys.executable
BUFFER_SIZE = 1024


class ProcessContext(object):
    def __init__(self, args):
        self.__args = args
        self.__process = None

    def __enter__(self):
        print 'run process {}'.format(' '.join(self.__args))
        self.__process = process = subprocess.Popen(self.__args,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            bufsize=BUFFER_SIZE
        )
        return process

    def __exit__(self, exc_type, exc_val, exc_tb):
        print 'kill process {}'.format(' '.join(self.__args))
        if self.__process.returncode is None:
            self.__process.kill()


def run(script, *args):
    return ProcessContext((PYTHON_PATH, script) + args)
