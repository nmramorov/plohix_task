from datetime import date, datetime
from collections import namedtuple
import logging


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
            current_day=date.day,
            current_time=datetime.now,
            font_color='Green',
            background_color='Blue'
        )

        return package