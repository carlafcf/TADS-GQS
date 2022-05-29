from vendas import *

import unittest

class TestTotalVendas(unittest.TestCase):
    def test_total_vendas(self):
        situacao1 = [[1, 300.5], [2, 400.70], [3, 1000]]
        situacao2 = []
        self.assertEqual(total_vendas(situacao1), 1701.20)
        self.assertEqual(total_vendas(situacao2), 0)


class TestPercentualVendas(unittest.TestCase):
    def test_percentual_vendas(self):
        situacao1 = [[1, 1, 4], [1, 2, 3], [1, 3, 1], [2, 1, 3]]
        self.assertEqual(percentual_vendas(situacao1), [[1, 0.6364], [2, 0.2727], [3, 0.0909]])

class TestMelhoriaVendas(unittest.TestCase):
    def test_melhoria_vendas(self):
        situacao1 = [['1/22', 400.50], ['2/22', 1000.00], ['3/22', 10.50], ['4/22', 10.50]]
        self.assertEqual(melhoria_vendas('1/22', situacao1), False)
        self.assertEqual(melhoria_vendas('2/22', situacao1), 1.4969)
        self.assertEqual(melhoria_vendas('3/22', situacao1), -0.9895)
        self.assertEqual(melhoria_vendas('4/22', situacao1), 0)
