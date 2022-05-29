from conexaoDB import *

def ler_plantoes_medico(bd, medico):
    query = "SELECT data, horas FROM Horas_plantao hp, Medico m WHERE m.id = hp.id_medico AND m.nome = ?"
    return ler_bd(bd, query, (medico,))

def ler_dias_excesso_horas(bd):
    query = "SELECT data FROM Horas_plantao GROUP BY data HAVING SUM(horas) > 24"
    return ler_bd(bd, query)