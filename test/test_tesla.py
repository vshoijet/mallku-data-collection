import unittest
from tesla import get_tesla_facilities


class TeslaTest(unittest.TestCase):

    def test_dataframe_should_be_of_correct_size(self):
        tesla_facilities = get_tesla_facilities()
        self.assertEqual(6, len(tesla_facilities.index))
