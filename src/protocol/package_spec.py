from datetime import datetime
from random import randint

from bitstring import BitArray


class Package:
    
    def __init__(self, **kwargs):
        self.user_input = kwargs

    def __get_current_date(self):
        date = datetime.now()
        parsed_date = __parse_current_date(date)
        return parsed_date

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
        pkg_id = randint(1, 100)
        return pkg_id

    def __to_bits(self, package):
        bit_pkg = BitArray(
            f'uint:8={self.package.package_id}',
            f'uint:8={self.package.package_len}',
            f'uint:5={self.package.day}',
            f'uint:4={self.package.month}',
            f'uint:15={self.package.year}',
            f'uint:4={self.package.date_font_color}',
            f'uint:4={self.package.date_back_color}',
            f'uint:12={self.package.hour}',
            f'uint:6={self.package.minute}',
            f'uint:6={self.package.second}',
            f'uint:4={self.package.clock_font_color}',
            f'uint:4={self.package.clock_back_color}',
            f'uint:8={self.package.control_sum}'
        )

        return bit_pkg

    def create_package(self):
        current_date = __get_current_date()
        parsed_date = __parse_current_date(current_date)

        Package = namedtuple('Package', 'year month day hour minute second package_id package_len\
                                    date_font_color date_back_color clock_font_color clock_back_color')

        package = Package(
            year = parsed_date['year'],
            month = parsed_date['month'],
            day = parsed_date['day'],
            hour = parsed_date['hour'],
            minute = parsed_date['minute'],
            second = parsed_date['second'],
            package_id = __get_package_id(),
            package_len = self.user_input['package_len'],
            date_font_color = self.user_input['date_font_color'],
            date_back_color = self.user_input['date_back_color'],
            clock_font_color = self.user_input['clock_font_color'],
            clock_back_color = self.user_input['clock_back_color'],
            checksum = __count_checksum()
        )

        bit_package = __to_bits(package)
        return bit_package

    