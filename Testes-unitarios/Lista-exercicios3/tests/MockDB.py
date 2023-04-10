from unittest import TestCase

import sys
sys.path.insert(0, '..')
from conexaoDB import *

BD = "TestDB.db"

class MockBD(TestCase):
    @classmethod
    def setUpClass(cls):
        con = conectar(BD)
        cursor = con.cursor()

        # Medico: id(PK), nome, crm, especialidade
        # Paciente: id (PK), nome
        # Prontuario: id (PK), id_medico (FK), id_paciente(FK)
        # Exames: id (PK), nome, id_prontuario (FK), resultado

        query_create_medico = """CREATE TABLE Medico (
                                  id int NOT NULL PRIMARY KEY ,
                                  nome text NOT NULL,
                                  crm text NOT NULL,
                                  especialidade text NOT NULL
                                )"""
        query_create_paciente = """CREATE TABLE Paciente (
                                  id int NOT NULL PRIMARY KEY ,
                                  nome text NOT NULL
                                )"""
        query_create_prontuario = """CREATE TABLE Prontuario (
                                  id int NOT NULL PRIMARY KEY,
                                  id_medico int NOT NULL,
                                  id_paciente int NOT NULL,
                                  FOREIGN KEY (id_medico) REFERENCES Medico(id),
                                  FOREIGN KEY (id_paciente) REFERENCES Paciente(id)
                                )"""
        query_create_exames = """CREATE TABLE Exames (
                                  id int NOT NULL PRIMARY KEY ,
                                  nome text NOT NULL,
                                  id_prontuario int NOT NULL,
                                  resultado int NOT NULL,
                                  FOREIGN KEY (id_prontuario) REFERENCES Prontuario(id)
                                )"""
        try:
            cursor.execute(query_create_medico)
            cursor.execute(query_create_paciente)
            cursor.execute(query_create_prontuario)
            cursor.execute(query_create_exames)
            con.commit()
        except sqlite3.Error as error:
            print("Erro na criação das tabelas:", error)
        else:
            print("Criação das tabelas: OK")

        query_insert_medico = """INSERT INTO Medico (id, nome, crm, especialidade) VALUES
                                    (1, 'Guilherme', '2638', 'Cardiologista'),
                                    (2, 'Sarah', '3768', 'Cardiologista'),
                                    (3, 'Melissa', '2873', 'Nefrologista'),
                                    (4, 'Gisele', '23689', 'Nefrologista')"""

        query_insert_paciente = """INSERT INTO Paciente (id, nome) VALUES
                                    (1, 'Carla'),
                                    (2, 'Danilo'),
                                    (3, 'Daniel'),
                                    (4, 'Alice')"""

        query_insert_prontuario = """INSERT INTO Prontuario (id, id_medico, id_paciente) VALUES
                                    (1, 1, 1),
                                    (2, 1, 2),
                                    (3, 1, 1),
                                    (4, 2, 2),
                                    (5, 3, 3),
                                    (6, 4, 3),
                                    (7, 4, 2),
                                    (8, 3, 1),
                                    (9, 1, 1)
                                    """

        query_insert_exames = """INSERT INTO Exames (id, nome, id_prontuario, resultado) VALUES
                                    (1, 'Exame 1', 1, 100),
                                    (2, 'Exame 1', 2, 90),
                                    (3, 'Exame 2', 3, 50),
                                    (4, 'Exame 2', 4, 30),
                                    (5, 'Exame 3', 8, 50),
                                    (6, 'Exame 4', 1, 120),
                                    (7, 'Exame 1', 7, 100),
                                    (8, 'Exame 2', 7, 100),
                                    (9, 'Exame 5', 9, 100),
                                    (10, 'Exame 4', 9, 100)
                                    """
        try:
            cursor.execute(query_insert_medico)
            cursor.execute(query_insert_paciente)
            cursor.execute(query_insert_prontuario)
            cursor.execute(query_insert_exames)
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
            cursor.execute("DROP TABLE Medico")
            cursor.execute("DROP TABLE Paciente")
            cursor.execute("DROP TABLE Prontuario")
            cursor.execute("DROP TABLE Exames")
            con.commit()
            cursor.close()
            print("Removeu os dados das tabelas.")
        except sqlite3.Error as error:
            print("Banco de dados não existe. Erro na remoção do BD.", error)
        finally:
            desconectar(con)




