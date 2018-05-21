import os
import time
from collections import namedtuple
from contextlib import contextmanager

DELAY = 0.1
MAX_WAIT_TIME = 1.0

_FileInfo = namedtuple('_FileInfo', ['name', 'data'])


class FileInfo(_FileInfo):
    def exists(self):
        return FileContext(self.name)

    def read(self):
        with open(self.name, 'r') as fileObject:
            return fileObject.read()

    def write(self, data):
        with open(self.name, 'w') as fileObject:
            fileObject.write(data)


class NoFileInfo(_FileInfo):
    @staticmethod
    @contextmanager
    def exists():
        yield

    @staticmethod
    def read():
        return None

    @staticmethod
    def write(data):
        pass


class FileContext(object):
    def __init__(self, name):
        self.__name = name

    def __enter__(self):
        print 'create file {}'.format(self.__name)
        timer = 0
        while not os.path.exists(self.__name):
            try:
                open(self.__name, 'a').close()
            except IOError as ex:
                if timer > MAX_WAIT_TIME:
                    raise
                print ex
                timer += DELAY
                time.sleep(DELAY)

    def __exit__(self, exc_type, exc_val, exc_tb):
        print 'delete file {}'.format(self.__name)
        timer = 0
        while os.path.exists(self.__name):
            try:
                os.remove(self.__name)
            except IOError as ex:
                if timer > MAX_WAIT_TIME:
                    raise
                print ex
                timer += DELAY
                time.sleep(DELAY)


DEFAULT_FILE_INFO = NoFileInfo(None, None)
