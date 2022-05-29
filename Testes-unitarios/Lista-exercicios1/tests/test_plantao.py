from plantao import *

import unittest

class TestMedicoCampeao(unittest.TestCase):
    # [('Carla', 300), ('Danilo', 200), ('Daniel', 150), ('Alice', 20)]
    def test_max_horas(self):
        situacao1 = [('Carla', 300), ('Danilo', 200), ('Daniel', 150), ('Alice', 20)]
        situacao2 = [('Carla', 300), ('Danilo', 200), ('Daniel', 300), ('Alice', 20)]
        situacao3 = []

        self.assertEqual(max_horas(situacao1), [('Carla', 300)])
        self.assertEqual(max_horas(situacao2), [('Carla', 300), ('Daniel', 300)])
        self.assertEqual(max_horas(situacao3), [])