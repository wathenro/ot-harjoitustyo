import unittest
from loaders.map_maker import MapMaker
from loaders.location_loader import LocLoader
from optimizers.optimizer import Optimizer


class TestLocLoader(unittest.TestCase):
    def setUp(self):
        self.loader=LocLoader()
        self.maker=MapMaker()
        self.optimizer=Optimizer()
        self.created_map,self.c_on_map=self.maker.make_map\
            ("Helsinki","Porvoo",self.loader.location_loader())
    def test_optimizer(self):
        _,_,_,_,track=self.optimizer.optimizer\
            ("Helsinki","Porvoo",self.created_map,self.c_on_map,60)
        self.assertEqual(track,"Helsinki-Vantaa-Sipoo-Porvoo")