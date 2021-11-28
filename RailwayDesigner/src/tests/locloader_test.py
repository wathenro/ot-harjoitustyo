import unittest
from location_loader import LocLoader

class TestLocLoader(unittest.TestCase):
    def setUp(self):
        self.loader=LocLoader()

    def test_location_loader(self):
        self.assertEqual(self.loader.location_loader()\
            ["Latitude"]["Pori"], 61.483726303)
            