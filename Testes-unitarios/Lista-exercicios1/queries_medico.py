from conexaoDB import *

def ler_medicos_ativos(bd):
    return ler_bd(bd, "SELECT nome FROM Medico WHERE ativo = 1")

def ler_medicos_estado(bd, estado):
    query = "SELECT nome FROM Medico WHERE estado LIKE ?"
    return ler_bd(bd, query, ('%'+estado+'%',))