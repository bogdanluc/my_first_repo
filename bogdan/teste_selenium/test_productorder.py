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

class TestProductorder():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_productorder(self):
    # Test name: product_order
    # Step # | name | target | value
    # 1 | open | /en/ | 
    self.driver.get("https://prestashop-ta26.multibit.ro/en/")
    # 2 | setWindowSize | 1168x643 | 
    self.driver.set_window_size(1168, 643)
    # 3 | click | css=a > .hidden-sm-down | 
    self.driver.find_element(By.CSS_SELECTOR, "a > .hidden-sm-down").click()
    # 4 | click | id=content | 
    self.driver.find_element(By.ID, "content").click()
    # 5 | click | id=field-email | 
    self.driver.find_element(By.ID, "field-email").click()
    # 6 | type | id=field-password | paroladetest
    self.driver.find_element(By.ID, "field-password").send_keys("paroladetest")
    # 7 | type | id=field-email | lucaciubogdansorin@gmail.com
    self.driver.find_element(By.ID, "field-email").send_keys("lucaciubogdansorin@gmail.com")
    # 8 | click | id=submit-login | 
    self.driver.find_element(By.ID, "submit-login").click()
    # 9 | click | css=.logo | 
    self.driver.find_element(By.CSS_SELECTOR, ".logo").click()
    # 10 | click | css=.js-product:nth-child(4) img | 
    self.driver.find_element(By.CSS_SELECTOR, ".js-product:nth-child(4) img").click()
    # 11 | click | css=.touchspin-up | 
    self.driver.find_element(By.CSS_SELECTOR, ".touchspin-up").click()
    # 12 | click | css=.add-to-cart | 
    self.driver.find_element(By.CSS_SELECTOR, ".add-to-cart").click()
    # 13 | click | css=.cart-content-btn > .btn-primary |
    cart_content = WebDriverWait(self.driver, 10).until(lambda driver:driver.find_element(By.CSS_SELECTOR, ".cart-content-btn > .btn-primary"))
    cart_content.click()
    # 14 | click | css=.text-sm-center > .btn | 
    self.driver.find_element(By.CSS_SELECTOR, ".text-sm-center > .btn").click()
    # 15 | click | name=confirm-addresses | 
    self.driver.find_element(By.NAME, "confirm-addresses").click()
    # 16 | click | name=confirmDeliveryOption | 
    self.driver.find_element(By.NAME, "confirmDeliveryOption").click()
    # 17 | click | id=payment-option-3 | 
    self.driver.find_element(By.ID, "payment-option-3").click()
    # 18 | click | id=conditions_to_approve[terms-and-conditions] | 
    self.driver.find_element(By.ID, "conditions_to_approve[terms-and-conditions]").click()
    # 19 | click | css=.ps-shown-by-js > .btn |
    self.driver.find_element(By.CSS_SELECTOR, ".ps-shown-by-js > .btn").click()
    # 1 | open | https://prestashop-ta26.multibit.ro/admin619cii23r/index.php?controller=AdminLogin&token=b65a48f22412c454be6d5d41575880a5 |
    self.driver.get(
      "https://prestashop-ta26.multibit.ro/admin619cii23r/index.php?controller=AdminLogin&token=b65a48f22412c454be6d5d41575880a5")
    # 2 | setWindowSize | 1168x643 |
    self.driver.set_window_size(1168, 643)
    # 3 | type | id=passwd | TestatareAutomata26
    self.driver.find_element(By.ID, "passwd").send_keys("TestatareAutomata26")
    # 4 | type | id=email | ta26@multibit.ro
    self.driver.find_element(By.ID, "email").send_keys("ta26@multibit.ro")
    # 5 | click | id=submit_login |
    self.driver.find_element(By.ID, "submit_login").click()
    # 6 | mouseOver | id=submit_login |
    self.driver.implicitly_wait(10)
    element = self.driver.find_element(By.ID, "submit_login")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 7 | mouseOut | id=submit_login |
    self.driver.implicitly_wait(10)
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    # actions.move_to_element(element).perform()
    # 8 | mouseOver | css=#subtab-AdminParentCustomer > .link |
    element = self.driver.find_element(By.CSS_SELECTOR, "#subtab-AdminParentCustomer > .link")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 9 | mouseOut | css=#subtab-AdminParentCustomer > .link |
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    # actions.move_to_element(element, 0, 0).perform()
    # 10 | mouseOver | css=#subtab-AdminCatalog > .link |
    element = self.driver.find_element(By.CSS_SELECTOR, "#subtab-AdminCatalog > .link")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 11 | mouseOut | css=#subtab-AdminCatalog > .link |
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    # actions.move_to_element(element, 0, 0).perform()
    # 12 | mouseOver | css=#subtab-AdminParentOrders > .link |
    element = self.driver.find_element(By.CSS_SELECTOR, "#subtab-AdminParentOrders > .link")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 13 | mouseOut | css=#subtab-AdminParentOrders > .link |
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    # actions.move_to_element(element, 0, 0).perform()
    # 14 | click | css=#subtab-AdminParentOrders span |
    self.driver.find_element(By.CSS_SELECTOR, "#subtab-AdminParentOrders span").click()
    # 15 | click | linkText=Orders |
    self.driver.find_element(By.LINK_TEXT, "Orders").click()
    # 16 | mouseOver | linkText=Orders |
    element = self.driver.find_element(By.LINK_TEXT, "Orders")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 17 | click | css=tr:nth-child(1) > .column-reference |
    self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(1) > .column-reference").click()
    # 18 | assertText | linkText=lucaciubogdansorin@gmail.com | lucaciubogdansorin@gmail.com
    assert self.driver.find_element(By.LINK_TEXT, "lucaciubogdansorin@gmail.com").text == "lucaciubogdansorin@gmail.com"
    