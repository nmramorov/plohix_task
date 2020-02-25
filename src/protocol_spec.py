from datetime import date, datetime
from collections import namedtuple
import logging


FORMAT = '%(asctime)s %(message)s'
logging.basicConfig(level=logging.INFO, format=FORMAT)
logger = logging.getLogger('protocol')


class Serial_Protocol:

    """
    This protocol is used for transmitting data to 
    the given serial port
    """

    def __init__(self, period: int, user_input: tuple):
        
        self.period = period
        self.font_color, self.background_color = user_input
        self.Package_data = namedtuple("Package_data", "current_date\
                                                   current_day\
                                                   current_time\
                                                   font_color\
                                                   background_color")

    def create_package(self) -> namedtuple:
        """Creates package for serial port, package contains data in bytes"""

        package = self.Package_data(
            current_date=date.today(),
            current_day=str(date.day),
            current_time=datetime.now(),
            font_color='Green',
            background_color='Blue'
        )

        logger.info(f"The package data is:\n\
                    Current date is {package.current_date}\n\
                    Current day is {package.current_day}\n\
                    Current time is {package.current_time}\n\
                    Current font is {package.font_color}\n\
                    Current background is {package.background_color}")
        return package


if __name__ == "__main__":

    Test_Protocol = Serial_Protocol(10, ('test_font', 'test_background'))
    test_package = Test_Protocol.create_package()
    logger.info(test_package)