from datetime import datetime
from collections import namedtuple
import logging
from re import match


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
        self.Package_data = namedtuple("Package_data", "package_id\
                                                    package_len\
                                                    day\
                                                    month\
                                                    year\
                                                    date_font_color\
                                                    date_back_color\
                                                    hour\
                                                    minute\
                                                    second\
                                                    clock_font_color\
                                                    clock_back_color\
                                                    control_sum")

    def __get_current_date(self):
        date = datetime.now()
        parsed_date = __parse_current_date(date)
        return parsed_date

    def __parse_current_date(self, date_to_parse: str):
        matched = re.match(r'(?P<year>^.{4})-(?P<month>.{2})-(?P<day>.{2}) (?P<hour>.{2}):(?P<minute>.{2}):(?P<seconds>.{2})', date_to_parse)


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