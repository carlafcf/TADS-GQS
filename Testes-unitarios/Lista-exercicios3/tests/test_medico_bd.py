from MockDB import MockBD

import sys
sys.path.insert(0, '..')
from conexaoDB import *
from queries_medico import *

class TestMedicoDB(MockBD):
    def test_pacientes_medico(self):
        # Teste 1 = Paciente existente, visitou médicos
        # Teste 2 = Paciente não existente
        # Teste 3 = Paciente existe, não visitou nenhum médico
        paciente1 = 'Carla'
        retorno_esperado1 = [(1,), (3,)]
        paciente2 = 'João'
        retorno_esperado2 = []
        paciente3 = 'Alice'
        retorno_esperado3 = []
        self.assertEqual(ler_medicos_paciente(self.mock_db_config.get('bd'), paciente1), retorno_esperado1)
        self.assertEqual(ler_medicos_paciente(self.mock_db_config.get('bd'), paciente2), retorno_esperado2)
        self.assertEqual(ler_medicos_paciente(self.mock_db_config.get('bd'), paciente3), retorno_esperado3)

    def test_pacientes_especialidade(self):
        especialidade1 = 'Nefrologista'
        retorno_esperado1 = [('Carla',), ('Daniel',), ('Danilo',)]
        especialidade2 = 'Cirurgião'
        retorno_esperado2 = []
        self.assertEqual(ler_pacientes_especialidade(self.mock_db_config.get('bd'), especialidade1), retorno_esperado1)
        self.assertEqual(ler_pacientes_especialidade(self.mock_db_config.get('bd'), especialidade2), retorno_esperado2)