from conexaoDB import *

def ler_exames_mais_feitos(bd):
    query = "SELECT nome FROM Exames GROUP BY nome " \
            "HAVING COUNT(nome) = ( " \
            "SELECT MAX(quantidade) FROM ( " \
            "SELECT nome, COUNT(nome) AS quantidade " \
            "FROM Exames " \
            "GROUP BY nome) " \
            ")"
    return ler_bd(bd, query)

def ler_exames_paciente_medico(bd, paciente, medico):
    query = "SELECT DISTINCT ex.nome FROM Exames ex, Prontuario pront, Paciente pac, Medico m WHERE " \
            "pac.id = pront.id_paciente AND m.id = pront.id_medico AND ex.id_prontuario = pront.id AND " \
            "pac.nome = ? AND m.nome = ?"
    return ler_bd(bd, query, (paciente, medico,))