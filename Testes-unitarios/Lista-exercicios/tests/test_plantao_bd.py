from MockDB import MockBD

import sys
sys.path.insert(0, '..')
from conexaoDB import *
from queries_plantao import *

class TestPlantaoDB(MockBD):
    def test_plantoes_medico(self):
        medico = "Carla"
        retorno_esperado = [('22/04/2022', 12), ('19/04/2022', 6), ('17/04/2022', 12)]
        self.assertEqual(ler_plantoes_medico(self.mock_db_config.get('bd'), medico), retorno_esperado)


    def test_dias_excesso_horas(self):
        retorno_esperado = [('19/04/2022',)]
        self.assertEqual(ler_dias_excesso_horas(self.mock_db_config.get('bd')), retorno_esperado)