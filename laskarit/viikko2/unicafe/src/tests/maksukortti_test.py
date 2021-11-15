import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_saldo_alussa_oikein(self):
        self.assertEqual(self.maksukortti.saldo,10)

    def test_lataa_oikein(self):
        self.maksukortti.lataa_rahaa(5)
        self.assertEqual(self.maksukortti.saldo,15)

    def test_rahaa_tarpeeksi_ottoon(self):
        self.assertEqual(self.maksukortti.ota_rahaa(5),True)

    def test_rahaa_tarpeeksi_ottoon_niin_saldo_vahenee(self):
        self.maksukortti.ota_rahaa(5)
        self.assertEqual(self.maksukortti.saldo,5)

    def test_rahaa_ei_tarpeeksi_saldo_ei_vahene(self):
        onko_rahaa=self.maksukortti.ota_rahaa(11)
        self.assertEqual(self.maksukortti.saldo==10 and onko_rahaa==False,True)

    def test_kuvaus(self):
        mk=str(self.maksukortti)
        self.assertEqual(mk,"saldo: 0.1")