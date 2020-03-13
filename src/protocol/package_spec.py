from datetime import datetime
from random import randint
from collections import namedtuple
import re

from bitstring import BitArray


class Package:
    def __init__(self, **kwargs):
        self.user_input = kwargs

    def __get_current_date(self):
        return str(datetime.now())

    def __parse_current_date(self, date_to_parse: str):
        matched = re.match(r'(?P<year>^.{4})-(?P<month>.{2})-(?P<day>.{2}) (?P<hour>.{2}):(?P<minute>.{2}):(?P<second>.{2})', date_to_parse)
        return dict(
            year = matched.group('year'),
            month = matched.group('month'),
            day = matched.group('day'),
            hour = matched.group('hour'),
            minute = matched.group('minute'),
            second = matched.group('second'),
        )

    def __get_package_id(self):
        return randint(1, 100)

    def __to_bits(self, package):
        bit_pkg = BitArray()

        pkg_data = [
            '0b00000001',
            f'uint:8={package.data_len}',
            f'uint:5={package.day}',
            f'uint:4={package.month}',
            f'uint:15={package.year}',
            f'uint:4={package.date_font_color}',
            f'uint:4={package.date_back_color}',
            f'uint:12={package.hour}',
            f'uint:6={package.minute}',
            f'uint:6={package.second}',
            f'uint:4={package.clock_font_color}',
            f'uint:4={package.clock_back_color}',
            f'uint:8={package.checksum}'
        ]
        for data in pkg_data:
            bit_pkg.append(data)
        return bit_pkg

    def create_package(self):
        current_date = self.__get_current_date()
        parsed_date = self.__parse_current_date(current_date)
        Package = namedtuple('Package', 'year month day hour minute second package_id data_len\
                                    date_font_color date_back_color clock_font_color clock_back_color checksum')
        package = Package(
            year = parsed_date['year'],
            month = parsed_date['month'],
            day = parsed_date['day'],
            hour = parsed_date['hour'],
            minute = parsed_date['minute'],
            second = parsed_date['second'],
            package_id = self.__get_package_id(),
            data_len = self.user_input['data_len'],
            date_font_color = self.user_input['date_font_color'],
            date_back_color = self.user_input['date_back_color'],
            clock_font_color = self.user_input['clock_font_color'],
            clock_back_color = self.user_input['clock_back_color'],
            checksum = '88' #magic number
        )
        bit_package = self.__to_bits(package)
        return bit_package


if __name__ == "__main__":
    pkg = Package(
        data_len=80,
        date_font_color=6,
        date_back_color=7,
        clock_font_color=5,
        clock_back_color=4
        )

    package = pkg.create_package()
    print(package)