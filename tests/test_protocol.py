import unittest
from collections import namedtuple
import logging
import sys
import os.path

sys.path.insert(0, os.path.abspath('src'))

import protocol_spec


class TestProtocol(unittest.TestCase):

    def test_protocol(self):

        Test_Protocol = protocol_spec.Serial_Protocol(period=10,
                                                     user_input=('Test_font', 'Test_color')
                                                    )
        test_package = Test_Protocol.create_package()
        
        self.assertIsNotNone(test_package)


if __name__ == "__main__":

    unittest.main()