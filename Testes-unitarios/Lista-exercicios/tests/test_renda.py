from renda import *

import unittest

class TestRenda(unittest.TestCase):
    # [('Trabalho 1', 3000.50), ('Trabalho 2', 5000.00), ('Trabalho 3', 150), ('Trabalho 4', 200.50)]
    def test_percentual_renda_mensal(self):
        situacao1 = [('Trabalho 1', 3000.50), ('Trabalho 2', 5000.00), ('Trabalho 3', 150), ('Trabalho 4', 200.50)] #8351.00
        r_esperado1 = [('Trabalho 1', 0.3593), ('Trabalho 2', 0.5987), ('Trabalho 3', 0.0180), ('Trabalho 4', 0.0240)]
        situacao2 = [('Trabalho 1', 3000.50), ('Trabalho 2', 5000.00), ('Trabalho 3', 0), ('Trabalho 4', 200.50)] #8201.00
        r_esperado2 = [('Trabalho 1', 0.3659), ('Trabalho 2', 0.6097), ('Trabalho 3', 0), ('Trabalho 4', 0.0244)]
        situacao3 = [('Trabalho 1', 0), ('Trabalho 2', 0), ('Trabalho 3', 0), ('Trabalho 4', 0)]
        r_esperado3 = [('Trabalho 1', 0), ('Trabalho 2', 0), ('Trabalho 3', 0), ('Trabalho 4', 0)]

        self.assertEqual(percentual_renda_mensal(situacao1), r_esperado1)
        self.assertEqual(percentual_renda_mensal(situacao2), r_esperado2)
        self.assertEqual(percentual_renda_mensal(situacao3), r_esperado3)

    def test_percentual_renda_media(self):
        mes1 = [('Trabalho 1', 5000), ('Trabalho 2', 300), ('Trabalho 3', 200)]
        mes2= [('Trabalho 1', 2000), ('Trabalho 2', 100), ('Trabalho 3', 1000)]
        mes3 = [('Trabalho 1', 4000), ('Trabalho 2', 0), ('Trabalho 3', 300)]
        # Trabalho 1 = 11000
        # Trabalho 2 = 400
        # Trabalho 3 = 1500
        # Total = 12900
        r_esperado = [('Trabalho 1', 0.8527), ('Trabalho 2', 0.0310), ('Trabalho 3', 0.1163)]
        self.assertEqual(percentual_renda_media([mes1, mes2, mes3]), r_esperado)