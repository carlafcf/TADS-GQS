from MockDB import MockBD

import sys
sys.path.insert(0, '..')
from conexaoDB import *
from queries_medico import *

class TestMedicoDB(MockBD):
    def test_medicos_ativos(self):
        retorno_esperado = [('Carla',), ('Danilo',), ('Daniel',)]
        self.assertEqual(ler_medicos_ativos(self.mock_db_config.get('bd')), retorno_esperado)


    def test_filtro_nome(self):
        retorno_esperado_1 = [('Carla',), ('Danilo',)]
        retorno_esperado_2 = []
        self.assertEqual(ler_medicos_estado(self.mock_db_config.get('bd'), 'RN'), retorno_esperado_1)
        self.assertEqual(ler_medicos_estado(self.mock_db_config.get('bd'), 'PB'), retorno_esperado_2)