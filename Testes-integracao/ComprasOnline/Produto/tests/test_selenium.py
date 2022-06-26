from django.test import LiveServerTestCase
from selenium.webdriver.common.keys import Keys

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from django.urls import reverse

from Produtos.models import Produto

import time 

class ProdutoSeleniumTest(LiveServerTestCase):

  @classmethod
  def setUp(cls):
    cls.driver = webdriver.Chrome(ChromeDriverManager().install())
  
  @classmethod
  def tearDownClass(cls):
      cls.driver.quit()
      super().tearDownClass()

  def test_form_1_ok(self):
    self.driver.get('http://127.0.0.1:8081/produtos/criar_produto/')
    time.sleep(2)
    self.driver.find_element_by_id('id_nome').send_keys("Produto")
    self.driver.find_element_by_id('id_fornecedor').send_keys("Madeira")
    self.driver.find_element_by_id('id_preco_de_venda').send_keys("1000.55")

    submit = self.driver.find_element_by_id('submit_button')
    time.sleep(2)
    submit.send_keys(Keys.RETURN)
    # submit.click()
    time.sleep(2)

    # assert "Produto" in self.driver.find_element_by_id('id_Produto_Madeira').text
    assert "Produto" in self.driver.page_source
    assert "4 produtos" in self.driver.page_source

  def test_form_2_not_ok(self):
    self.driver.get('http://127.0.0.1:8081/produtos/criar_produto/')
    time.sleep(2)
    self.driver.find_element_by_id('id_nome').send_keys("Cama")
    self.driver.find_element_by_id('id_fornecedor').send_keys("Madeira")
    self.driver.find_element_by_id('id_preco_de_venda').send_keys("1000.55")

    submit = self.driver.find_element_by_id('submit_button')
    time.sleep(2)
    submit.send_keys(Keys.RETURN)
    # submit.click()
    time.sleep(2)

    # assert "Produto" in self.driver.find_element_by_id('id_Produto_Madeira').text
    assert "Já há um produto deste fornecedor com este nome cadastrado." in self.driver.page_source
  
  def test_detalhes(self):
    self.driver.get('http://127.0.0.1:8081/produtos/listar_produtos/')
    time.sleep(2)

    detalhes_button = self.driver.find_element_by_id('id_button_1')
    detalhes_button.click()
    time.sleep(2)

    assert "Detalhes produto Ar condicionado" in self.driver.page_source
    assert "Preço de venda: 1000,55" in self.driver.find_element_by_id('id_preco_de_venda').text
    assert "Fornecedor: LG" in self.driver.find_element_by_id('id_fornecedor').text

  def test_detalhes(self):
    self.driver.get('http://127.0.0.1:8081/produtos/listar_produtos/')
    time.sleep(2)

    detalhes_button = self.driver.find_element_by_id('id_button_1').value_of_css_property('background-color')
    assert "rgba(25, 135, 84, 1)" == detalhes_button