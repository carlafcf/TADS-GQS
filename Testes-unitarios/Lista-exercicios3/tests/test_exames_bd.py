from MockDB import MockBD

import sys
sys.path.insert(0, '..')
from conexaoDB import *
from queries_exames import *

class TestMedicoDB(MockBD):
    def test_exames_mais_feitos(self):
        # Teste 1 = Dois exames com mesma quantidade
        retorno_esperado = [('Exame 1',), ('Exame 2',)]
        self.assertEqual(ler_exames_mais_feitos(self.mock_db_config.get('bd')), retorno_esperado)

    def test_exames_paciente_medico(self):
        # Teste 1 = Mais de uma visita
        # Teste 2 = apenas uma visita
        # Teste 3 = não há visitas, ou não há médico, ou não há paciente

        paciente1 = 'Carla'
        medico1 = 'Guilherme'
        retorno_esperado1 = [('Exame 1',), ('Exame 2',), ('Exame 4',), ('Exame 5',)]

        paciente2 = 'Carla'
        medico2 = 'Melissa'
        retorno_esperado2 = [('Exame 3',)]

        paciente3 = 'Alice'
        medico3 = 'Guilherme'
        retorno_esperado3 = []

        paciente4 = 'Ana'
        medico4 = 'Pedro'
        retorno_esperado4 = []
        self.assertEqual(ler_exames_paciente_medico(self.mock_db_config.get('bd'), paciente1, medico1), retorno_esperado1)
        self.assertEqual(ler_exames_paciente_medico(self.mock_db_config.get('bd'), paciente2, medico2), retorno_esperado2)
        self.assertEqual(ler_exames_paciente_medico(self.mock_db_config.get('bd'), paciente3, medico3), retorno_esperado3)
        self.assertEqual(ler_exames_paciente_medico(self.mock_db_config.get('bd'), paciente4, medico4), retorno_esperado4)