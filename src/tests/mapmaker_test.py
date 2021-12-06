import unittest
from loaders.map_maker import MapMaker
from loaders.location_loader import LocLoader


class TestLocLoader(unittest.TestCase):
    def setUp(self):
        self.loader=LocLoader()
        self.maker=MapMaker()

    def test_make_map(self):
        idle_image,pruned_communities=self.maker.make_map\
            ("Pori","Kotka",self.loader.location_loader())
        no_image=idle_image is None
        self.assertEqual(pruned_communities["Latitude"]["Riihimäki"], 60.736737225)
        self.assertEqual(no_image,False)
            