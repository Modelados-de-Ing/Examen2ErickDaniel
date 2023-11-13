from Examen2 import MiClase
import unittest
class TestDB(unittest.TestCase):
    def test_ObtieneValencia (self):
         db = MiClase(5, 120, 12, ["Canción 1", "Canción 2", "Canción 3"], [0.8, 0.9, 0.7])
         self.assertEqual(db.ObtieneValencia(123589),4)
    def test_DivisibleTempo(self):
        db = MiClase(5, 120, 12, ["Canción 1", "Canción 2", "Canción 3"], [0.8, 0.9, 0.7])
        self.assertEqual(db.DivisibleTempo(10),[1,2,5,10])
    def test_ObtieneMasBailable(self):
        db = MiClase(5, 120, 12, ["Canción 1", "Canción 2", "Canción 3"], [0.8, 0.9, 0.7])
        self.assertEqual(db.ObtieneMasBailable([1,2,3]),3)
    def test_VerificaListaCanciones(self):
        db= MiClase(5, 120, 12, ["Canción 1", "Canción 2", "Canción 3"], [0.8, 0.9, 0.7])
        self.assertTrue(db.VerificaListaCanciones(["Canción 1", "Canción 2", "Canción 3"]))
if __name__ == "__main__":
    unittest.main()