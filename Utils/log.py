import sys
from logbook import Logger,StreamHandler

class conf():
    @staticmethod
    def logcon():
        log = Logger('Newadmin系统测试')
        StreamHandler(sys.stdout).push_application()
        return log


