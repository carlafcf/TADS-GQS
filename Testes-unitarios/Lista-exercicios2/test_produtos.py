from produtos import *

import unittest

class TestProdutosEmFalta(unittest.TestCase):
    def test_qnt_produtos(self):
        situacao1 = [['Shampoo', 10], ['Sabonete', 5], ['Condicionador', 2]]
        situacao2 = [['Shampoo', 10], ['Sabonete', 6], ['Condicionador', 9]]
        self.assertEqual(produtos_reposicao(situacao1), 1)
        self.assertEqual(produtos_reposicao(situacao2), 0)