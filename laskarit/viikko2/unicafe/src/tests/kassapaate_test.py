import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti_hyva=Maksukortti(500)
        self.maksukortti_paha=Maksukortti(100)

    def test_oikea_alku(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa==100000 and self.kassapaate.edulliset==0 and self.kassapaate.maukkaat==0,True)

    def test_syo_edullisesti_kateisella(self):
        
        palautus=self.kassapaate.syo_edullisesti_kateisella(100)
        liian_vahan_ok=(palautus==100) and (self.kassapaate.kassassa_rahaa==100000)
        lounaat_ok1=self.kassapaate.edulliset==0
        
        palautus=self.kassapaate.syo_edullisesti_kateisella(350)
        riittavasti_ok=(palautus==110) and (self.kassapaate.kassassa_rahaa==(100000+240))

        lounaat_ok2=self.kassapaate.edulliset==1

        self.assertEqual(liian_vahan_ok and riittavasti_ok and lounaat_ok1 and lounaat_ok2,True)

    def test_syo_maukkaasti_kateisella(self):
        
        palautus=self.kassapaate.syo_maukkaasti_kateisella(100)
        liian_vahan_ok=(palautus==100) and (self.kassapaate.kassassa_rahaa==100000)
        lounaat_ok1=self.kassapaate.maukkaat==0
        
        palautus=self.kassapaate.syo_maukkaasti_kateisella(450)
        riittavasti_ok=(palautus==50) and (self.kassapaate.kassassa_rahaa==(100000+400))
        lounaat_ok2=self.kassapaate.maukkaat==1
        self.assertEqual(liian_vahan_ok and riittavasti_ok and lounaat_ok1 and lounaat_ok2,True)

    def test_syo_edullisesti_kortilla(self):
        kortti=self.maksukortti_paha
        palautus1=self.kassapaate.syo_edullisesti_kortilla(kortti)==False
        liian_vahan_ok=(kortti.saldo==100) and (self.kassapaate.kassassa_rahaa==100000)
        lounaat_ok1=self.kassapaate.edulliset==0
        
        kortti=self.maksukortti_hyva
        palautus2=self.kassapaate.syo_edullisesti_kortilla(kortti)==True
        riittavasti_ok=(kortti.saldo==260) and (self.kassapaate.kassassa_rahaa==100000)
        lounaat_ok2=self.kassapaate.edulliset==1

        self.assertEqual(palautus1 and palautus2 and liian_vahan_ok and riittavasti_ok and lounaat_ok1 and lounaat_ok2,True)

    def test_syo_maukkaasti_kortilla(self):
        kortti=self.maksukortti_paha
        palautus1=self.kassapaate.syo_maukkaasti_kortilla(kortti) == False
        liian_vahan_ok=(kortti.saldo==100) and (self.kassapaate.kassassa_rahaa==100000)
        lounaat_ok1=self.kassapaate.maukkaat==0
        
        kortti=self.maksukortti_hyva
        palautus2=self.kassapaate.syo_maukkaasti_kortilla(kortti)==True
        riittavasti_ok=(kortti.saldo==100) and (self.kassapaate.kassassa_rahaa==100000)
        lounaat_ok2=self.kassapaate.maukkaat==1

        self.assertEqual(palautus1 and palautus2 and liian_vahan_ok and riittavasti_ok and lounaat_ok1 and lounaat_ok2,True)

    def test_lataa_rahaa(self):
        kortti=self.maksukortti_paha
        self.kassapaate.lataa_rahaa_kortille(kortti,5000)
        self.assertEqual(self.kassapaate.kassassa_rahaa==105000 and kortti.saldo==5100,True)

    def test_lataa_nega_rahaa(self):
        kortti=self.maksukortti_paha
        self.kassapaate.lataa_rahaa_kortille(kortti,-1)
        self.assertEqual(self.kassapaate.kassassa_rahaa==100000 and kortti.saldo==100,True)