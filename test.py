import unittest
from health_utils import calculate_imc, calculate_mb

class TestHealthUtils(unittest.TestCase):
    def test_calculate_imc(self):
        self.assertAlmostEqual(calculate_imc(1.80, 80), 24.69, places=2)
    
    def test_calculate_mb_homme(self):
        self.assertAlmostEqual(calculate_mb(180, 80, 40, 'homme'), 1796.86, places=2)
    
    def test_calculate_mb_femme(self):
        self.assertAlmostEqual(calculate_mb(150, 50, 25, 'femme'), 1266.39, places=2)

if __name__ == '__main__':
    unittest.main()