import logging

from src.protocol.package_spec import Package


FORMAT = '%(asctime)s %(message)s'
logging.basicConfig(level=logging.INFO, format=FORMAT)
logger = logging.getLogger('protocol')

class Serial_Protocol:

    """
    This protocol is used for transmitting data to 
    the given serial port
    """

    def __init__(self, data_len, date_font_color, date_back_color, clock_font_color, clock_back_color):
        self.data_len=data_len,
        self.date_font_color=date_font_color,
        self.date_back_color=date_back_color,
        self.clock_font_color=clock_font_color,
        self.clock_back_color=clock_back_color
    
    def init_package(self):
        p = Package(data_len=self.data_len,
                    date_font_color=self.date_font_color,
                    date_back_color=self.date_back_color,
                    clock_font_color=self.clock_font_color,
                    clock_back_color=self.clock_back_color
                )
        return p.create_package()


if __name__ == "__main__":
    pass