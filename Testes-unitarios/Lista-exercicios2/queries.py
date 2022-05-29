from conexaoDB import *

def buscar_produto_nome(bd, nome):
    return ler_bd(bd, "SELECT id FROM Produto WHERE nome = ?", (nome,))

def buscar_produto_codigo(bd, codigo):
    return ler_bd(bd, "SELECT id FROM Produto WHERE codigo = ?", (codigo,))

def buscar_produto_categoria(bd, categoria):
    return ler_bd(bd, "SELECT id FROM Produto WHERE categoria = ?", (categoria,))

def buscar_produtos_venda(bd, id_venda):
    query = "SELECT p.nome FROM Produto p, Produto_venda pv WHERE pv.id_produto = p.id AND pv.id_venda = ?"
    return ler_bd(bd, query, (id_venda,))