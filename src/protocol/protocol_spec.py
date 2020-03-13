from datetime import datetime
from collections import namedtuple
import logging
from re import match

from package_spec import Package


FORMAT = '%(asctime)s %(message)s'
logging.basicConfig(level=logging.INFO, format=FORMAT)
logger = logging.getLogger('protocol')


class Serial_Protocol:

    """
    This protocol is used for transmitting data to 
    the given serial port
    """

    def __init__(self, **kwargs):
        self.user_input = kwargs
    
    def init_package(self):
        p = Package(self.user_input)
        return p.create_package()


if __name__ == "__main__":
    pass