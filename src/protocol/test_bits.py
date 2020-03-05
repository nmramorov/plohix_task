from bitstring import BitArray

class Package:
    
    def __init__(self, package_data):
        self.data = package_data

    def create_package(self):
        bitarr = BitArray(
            f'uint:8={self.data.package_id}',
            f'uint:8={self.data.package_len}',
            f'uint:5={self.data.day}',
            f'uint:4={self.data.month}',
            f'uint:15={self.data.year}',
            f'uint:4={self.data.date_font_color}',
            f'uint:4={self.data.date_back_color}',
            f'uint:12={self.data.hour}',
            f'uint:6={self.data.minute}',
            f'uint:6={self.data.second}',
            f'uint:4={self.data.clock_font_color}',
            f'uint:4={self.data.clock_back_color}',
            f'uint:8={self.data.control_sum}'
        )

        return bitarr