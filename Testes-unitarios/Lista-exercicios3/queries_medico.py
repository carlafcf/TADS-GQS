from conexaoDB import *

def ler_medicos_paciente(bd, paciente):
    query = "SELECT DISTINCT id_medico FROM Paciente pac, Prontuario pront WHERE pac.id = pront.id_paciente AND pac.nome = ?"
    return ler_bd(bd, query, (paciente,))

def ler_pacientes_especialidade(bd, especialidade):
    query = "SELECT DISTINCT pac.nome FROM Paciente pac, Prontuario pront, Medico m WHERE " \
            "pac.id = pront.id_paciente AND pront.id_medico = m.id AND m.especialidade = ?" \
            "ORDER BY pac.nome"
    return ler_bd(bd, query, (especialidade,))