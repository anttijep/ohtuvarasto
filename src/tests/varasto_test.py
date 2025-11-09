import unittest
from varasto import Varasto

class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_negatiivinen_lisays_ei_muuta_saldoa(self):
        saldo = self.varasto.saldo
        self.varasto.lisaa_varastoon(-5)
        self.assertEqual(saldo, self.varasto.saldo)

    def test_saldon_lisaaminen_yli_maksimin_tuottaa_maksimin(self):
        self.varasto.lisaa_varastoon(1e6)
        self.assertEqual(self.varasto.saldo, self.varasto.tilavuus)

    def test_negatiivinen_otto_ei_muuta_saldo(self):
        saldo = self.varasto.saldo
        self.varasto.ota_varastosta(-5)
        self.assertEqual(saldo, self.varasto.saldo)

    def test_yli_saldon_otto_ottaa_kaiken(self):
        saldo = self.varasto.saldo
        otto = self.varasto.ota_varastosta(1e6)
        self.assertEqual(saldo, otto)
        self.assertEqual(0, self.varasto.saldo)

    def test_print(self):
        string = "saldo = 0, vielä tilaa 10"
        self.assertEqual(str(self.varasto), string)

class TestVirheellinenConstructor(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(-1, -1)

    def test_konstruktor_negatiivinen_tilavuus_antaa_nollan(self):
        self.assertEqual(self.varasto.tilavuus, 0)

    def test_konstruktor_negatiivinen_saldo_antaa_nollan(self):
        self.assertEqual(self.varasto.saldo, 0)

def test_konstruktor_tarkistaa_ettei_saldo_ylita_tilavuutta():
    varasto = Varasto(5, 100)
    assert varasto.saldo == 5
