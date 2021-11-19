import unittest
from main_railway import MapLoader

class TestMaploader(unittest.TestCase):
    def setUp(self):
        self.map_to_use=MapLoader()

    def test_map_loader(self):
        self.map_to_use.map_loader()
        self.assertEqual(self.map_to_use.load_successful, True)