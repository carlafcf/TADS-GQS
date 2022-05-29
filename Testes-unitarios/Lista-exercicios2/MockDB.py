from unittest import TestCase

import sys
sys.path.insert(0, '..')
from conexaoDB import *

BD = "TestBD.db"

class MockBD(TestCase):
    @classmethod
    def setUpClass(cls):
        con = conectar(BD)
        cursor = con.cursor()

        query_create_usuario = """CREATE TABLE Usuario (
                                  id int NOT NULL PRIMARY KEY ,
                                  nome text NOT NULL,
                                  endereco text NOT NULL,
                                  tipo text NOT NULL
                                )"""
        query_create_produto = """CREATE TABLE Produto (
                                  id int NOT NULL PRIMARY KEY ,
                                  nome text,
                                  codigo int,
                                  categoria text,
                                  preco float,
                                  quantidade int
                                )"""
        query_create_venda = """CREATE TABLE Venda (
                                  id int NOT NULL PRIMARY KEY ,
                                  id_responsavel int NOT NULL,
                                  total float,
                                  FOREIGN KEY (id_responsavel) REFERENCES Usuario(id)
                                )"""
        query_create_produto_venda = """CREATE TABLE Produto_Venda (
                                  id int NOT NULL PRIMARY KEY ,
                                  id_produto int NOT NULL,
                                  id_venda int not null,
                                  quantidade int,
                                  FOREIGN KEY (id_produto) REFERENCES Produto(id),
                                  FOREIGN KEY (id_venda) REFERENCES Venda(id)
                                )"""
        try:
            cursor.execute(query_create_usuario)
            cursor.execute(query_create_produto)
            cursor.execute(query_create_venda)
            cursor.execute(query_create_produto_venda)
            con.commit()
        except sqlite3.Error as error:
            print("Erro na criação das tabelas:", error)
        else:
            print("Criação das tabelas: OK")

        query_insert_usuario = """INSERT INTO Usuario (id, nome, endereco, tipo) VALUES
                                    (1, 'Carla F.', 'rua', 'admin'),
                                    (2, 'Danilo', 'rua', 'vendedor'),
                                    (3, 'Daniel', 'rua', 'vendedor'),
                                    (4, 'Alice', 'rua', 'cliente')"""
        query_insert_produto = """INSERT INTO Produto (id, nome, codigo, categoria, preco, quantidade) VALUES
                                    (1, 'prod 1', 123, 'limpeza', 7.50, 10),
                                    (2, 'prod 2', 1234, 'limpeza', 20, 10),
                                    (3, 'prod 3', 1235, 'higiene', 7.50, 10),
                                    (4, 'prod 4', 1236, 'laticínios', 7.50, 10)"""
        query_insert_venda = """INSERT INTO Venda (id, id_responsavel, total) VALUES
                                    (1, 2, 100.50),
                                    (2, 3, 200.00)"""
        query_insert_produto_venda = """INSERT INTO Produto_venda (id, id_produto, id_venda, quantidade) VALUES
                                    (1, 1, 1, 4),
                                    (2, 2, 1, 3),
                                    (3, 3, 1, 1),
                                    (4, 1, 2, 3),
                                    (5, 2, 2, 1),
                                    (6, 4, 2, 5)"""
        try:
            cursor.execute(query_insert_usuario)
            cursor.execute(query_insert_produto)
            cursor.execute(query_insert_venda)
            cursor.execute(query_insert_produto_venda)
            con.commit()
        except sqlite3.Error as error:
            print("Erro na inserção de dados:", error)
        else:
            print("Inserção dos dados: OK")

        cursor.close()

        desconectar(con)

        testconfig ={
            'bd': BD
        }
        cls.mock_db_config = testconfig

    @classmethod
    def tearDownClass(cls):
        print("TearDown")
        con = conectar(BD)
        cursor = con.cursor()

        try:
            cursor.execute("DROP TABLE Usuario")
            cursor.execute("DROP TABLE Produto")
            cursor.execute("DROP TABLE Venda")
            cursor.execute("DROP TABLE Produto_venda")
            con.commit()
            cursor.close()
            print("Removeu os dados das tabelas.")
        except sqlite3.Error as error:
            print("Banco de dados não existe. Erro na remoção do BD.", error)
        finally:
            desconectar(con)




