from MockDB import MockBD

from conexaoDB import *
from queries import *

class TestDB(MockBD):
    def test_buscar_produto_nome(self):
        self.assertEqual(buscar_produto_nome(self.mock_db_config.get('bd'), 'prod 1'), [(1,)])
        self.assertEqual(buscar_produto_nome(self.mock_db_config.get('bd'), 'prod. 5'), [])

    def test_buscar_produto_codigo(self):
        self.assertEqual(buscar_produto_codigo(self.mock_db_config.get('bd'), 123), [(1,)])
        self.assertEqual(buscar_produto_codigo(self.mock_db_config.get('bd'), 122), [])

    def test_buscar_produto_categoria(self):
        self.assertEqual(buscar_produto_categoria(self.mock_db_config.get('bd'), 'limpeza'), [(1,), (2,)])
        self.assertEqual(buscar_produto_categoria(self.mock_db_config.get('bd'), 'higiene'), [(3,)])
        self.assertEqual(buscar_produto_categoria(self.mock_db_config.get('bd'), 'papelaria'), [])

    def test_buscar_produtos_venda(self):
        self.assertEqual(buscar_produtos_venda(self.mock_db_config.get('bd'), 1), [('prod 1',), ('prod 2',), ('prod 3',)])
        self.assertEqual(buscar_produtos_venda(self.mock_db_config.get('bd'), 2), [('prod 1',), ('prod 2',), ('prod 4',)])
        self.assertEqual(buscar_produtos_venda(self.mock_db_config.get('bd'), 3), [])