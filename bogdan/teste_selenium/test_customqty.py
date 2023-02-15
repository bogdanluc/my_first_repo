# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestCustomqty():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_customqty(self):
    # Test name: custom_qty
    # Step # | name | target | value
    # 1 | open | /en/ | 
    self.driver.get("https://prestashop-ta26.multibit.ro/en/")
    # 2 | setWindowSize | 1168x644 | 
    self.driver.set_window_size(1168, 644)
    # 3 | click | css=.js-product:nth-child(5) img | 
    self.driver.find_element(By.CSS_SELECTOR, ".js-product:nth-child(5) img").click()
    # 4 | click | css=.touchspin-up | 
    self.driver.find_element(By.CSS_SELECTOR, ".touchspin-up").click()
    # 5 | click | css=.touchspin-up | 
    self.driver.find_element(By.CSS_SELECTOR, ".touchspin-up").click()
    # 6 | click | css=.add-to-cart | 
    self.driver.find_element(By.CSS_SELECTOR, ".add-to-cart").click()
    # 7 | click | css=.cart-content-btn > .btn-primary |
    item_ordered = WebDriverWait(self.driver, 10).until(lambda driver:driver.find_element(By.CSS_SELECTOR, ".cart-content-btn > .btn-primary"))
    item_ordered.click()
    # 8 | click | name=product-quantity-spin |
    self.driver.find_element(By.NAME, "product-quantity-spin").click()
    # 9 | assertValue | name=product-quantity-spin | 3
    value = self.driver.find_element(By.NAME, "product-quantity-spin").get_attribute("value")
    assert value == "3"
    time.sleep(3)