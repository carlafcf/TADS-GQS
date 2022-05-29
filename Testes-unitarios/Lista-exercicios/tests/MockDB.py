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

        # Medico: id(PK), nome, crm, estado, ativo
        # Horas_plantao: id(PK), data, horas, id_medico(FK)

        query_create_medico = """CREATE TABLE Medico (
                                  id int NOT NULL PRIMARY KEY ,
                                  nome text NOT NULL,
                                  crm text NOT NULL,
                                  estado text NOT NULL,
                                  ativo int NOT NULL
                                )"""
        query_create_horas_plantao = """CREATE TABLE Horas_plantao (
                                  id int NOT NULL PRIMARY KEY ,
                                  data text NOT NULL,
                                  horas int NOT NULL,
                                  id_medico int NOT NULL,
                                  FOREIGN KEY (id_medico) REFERENCES Medico(id)
                                )"""
        try:
            cursor.execute(query_create_medico)
            cursor.execute(query_create_horas_plantao)
            con.commit()
        except sqlite3.Error as error:
            print("Erro na criação das tabelas:", error)
        else:
            print("Criação das tabelas: OK")

        query_insert_medico = """INSERT INTO Medico (id, nome, crm, estado, ativo) VALUES
                                    (1, 'Carla', '2638', 'RN', 1),
                                    (2, 'Danilo', '3768', 'RN', 1),
                                    (3, 'Daniel', '2873', 'SP', 1),
                                    (4, 'Alice', '23689', 'RJ', 0)"""
        query_insert_horas_plantao = """INSERT INTO Horas_plantao (id, data, horas, id_medico) VALUES
                                    (1, '22/04/2022', 12, 1),
                                    (2, '22/04/2022', 6, 2),
                                    (3, '21/04/2022', 12, 2),
                                    (4, '20/04/2022', 12, 2),
                                    (5, '19/04/2022', 6, 1),
                                    (6, '19/04/2022', 6, 2),
                                    (7, '19/04/2022', 12, 2),
                                    (8, '19/04/2022', 6, 2),
                                    (9, '18/04/2022', 12, 2),
                                    (10, '17/04/2022', 12, 1)
                                    """
        try:
            cursor.execute(query_insert_medico)
            cursor.execute(query_insert_horas_plantao)
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
            cursor.execute("DROP TABLE Turma")
            cursor.execute("DROP TABLE Disciplina")
            con.commit()
            cursor.close()
            print("Removeu os dados das tabelas.")
        except sqlite3.Error as error:
            print("Banco de dados não existe. Erro na remoção do BD.", error)
        finally:
            desconectar(con)




