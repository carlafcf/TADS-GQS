from prontuario import *

import unittest

class TestProntuario(unittest.TestCase):

    def test_pacientes_mais_visitas(self):
        # Casos de teste
        # 1- Dizer um médico e ele não ter nenhum prontuário associado a ele
        # 2- Dizer um médico e indicar o paciente com mais visitas
        # 3- Dizer um médico e ter dois ou mais pacientes com o mesmo número de visitas

        # (id_prontuario, nome_paciente, data_visita, id_medico_atendente)

        situacao1 = [(1, 'Carla', '5/2/22', 1), (2, 'Danilo', '5/2/22', 1), (3, 'Carla', '5/2/22', 2), (4, 'Danilo', '5/2/22', 2), (5, 'Carla', '4/9/21', 1)]
        # Médico id=5
        r_esperado1 = []
        # Médico id=1
        r_esperado2 = ['Carla']
        # Médico id=2
        r_esperado3 = ['Carla', 'Danilo']

        self.assertEqual(pacientes_mais_visitas(situacao1, 5), r_esperado1)
        self.assertEqual(pacientes_mais_visitas(situacao1, 1), r_esperado2)
        self.assertEqual(pacientes_mais_visitas(situacao1, 2), r_esperado3)

    def test_pacientes_premiados(self):
        # Casos de teste
        # 1- Não ter nenhum paciente premiado
        # 2- Ter mais de um paciente premiado
        # 3- Ter mais de um paciente com a mesma quantidade de visitas (6)

        # (mes, id_paciente, id_medico)

        situacao1 = [('1/22', 1, 1), ('1/22', 2, 4), ('2/22', 3, 2), ('3/22', 3, 3), ('4/22', 4, 7), ('5/22', 1, 4), ('6/22', 1, 8), ('7/22', 1, 10)]
        r_esperado1 = []

        situacao2 = [('1/22', 1, 1), ('1/22', 2, 4), ('2/22', 1, 2), ('3/22', 1, 3), ('4/22', 1, 7), ('5/22', 1, 4), ('6/22', 1, 8), ('7/22', 1, 10)]
        r_esperado2 = [1]

        situacao3 = [('1/22', 1, 1), ('1/22', 2, 4), ('2/22', 1, 2), ('3/22', 1, 3), ('4/22', 1, 7), ('5/22', 1, 4), ('6/22', 1, 8), ('7/22', 1, 10),
                     ('1/22', 2, 1), ('1/22', 2, 4), ('2/22', 2, 2), ('3/22', 2, 3), ('4/22', 2, 7), ('5/22', 2, 4), ('6/22', 1, 8), ('7/22', 3, 10),]
        r_esperado3 = [1, 2]

        self.assertEqual(pacientes_premiados(situacao1), r_esperado1)
        self.assertEqual(pacientes_premiados(situacao2), r_esperado2)
        self.assertEqual(pacientes_premiados(situacao3), r_esperado3)