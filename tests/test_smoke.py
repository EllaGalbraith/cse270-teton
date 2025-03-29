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
from selenium.webdriver.chrome.options import Options

class TestDefaultSuite():
  # def setup_method(self, method):
  #   self.driver = webdriver.Firefox()
  #   self.vars = {}
  def setup_method(self, method):
    options = Options()
    options.add_argument("--headless=new")
    self.driver = webdriver.Chrome(options=options)
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_1aSiteLogo(self):
    self.driver.get("http://127.0.0.1:5500/cse270-teton/teton/1.6/index.html")
    elements = self.driver.find_elements(By.XPATH, "/html/body/div/header/div[1]/div[1]/a/img")
    assert len(elements) > 0
  
  def test_1bbrowsertabtitle(self):
    self.driver.get("http://127.0.0.1:5500/cse270-teton/teton/1.6/index.html")
    assert self.driver.title == "Teton Idaho CoC"
  
  def test_1cwebsiteheading(self):
    self.driver.get("http://127.0.0.1:5500/cse270-teton/teton/1.6/index.html")
    assert self.driver.find_element(By.XPATH, "/html/body/div/header/div[1]/div[2]/h1").text == "Teton Idaho"
    assert self.driver.find_element(By.XPATH, "/html/body/div/header/div[1]/div[2]/h2").text == "Chamber of Commerce"
  
  def test_2ascreensize(self):
    self.driver.get("http://127.0.0.1:5500/cse270-teton/teton/1.6/index.html")
    self.driver.set_window_size(1920, 1080)
  
  def test_2btwospotlights(self):
    self.driver.get("http://127.0.0.1:5500/cse270-teton/teton/1.6/index.html")
    elements = self.driver.find_elements(By.XPATH, "/html/body/div/main/section[5]/div[1]")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.XPATH, "/html/body/div/main/section[5]/div[2]")
    assert len(elements) > 0
  
  def test_2cJoinUslink(self):
    self.driver.get("http://127.0.0.1:5500/cse270-teton/teton/1.6/index.html")
    elements = self.driver.find_elements(By.XPATH, "/html/body/div/header/nav/ul/li[2]/a")
    assert len(elements) > 0
  
  def test_2dJoinUslink(self):
    self.driver.get("http://127.0.0.1:5500/cse270-teton/teton/1.6/index.html")
    self.driver.find_element(By.LINK_TEXT, "Join").click()
    self.vars["pageUrl"] = self.driver.execute_script("return window.location.href")
    assert(self.vars["pageUrl"] == "http://127.0.0.1:5500/cse270-teton/teton/1.6/join.html")
  
  def test_3aGrid(self):
    self.driver.get("http://127.0.0.1:5500/cse270-teton/teton/1.6/directory.html")
    self.driver.find_element(By.XPATH, "//*[@id=\"directory-grid\"]").click()
  
  def test_3bTetonTurfandTree(self):
    self.driver.get("http://127.0.0.1:5500/cse270-teton/teton/1.6/directory.html")
    self.driver.find_element(By.XPATH, "//*[@id=\"directory-grid\"]").click()
    assert self.driver.find_element(By.XPATH, "/html/body/div/main/div[2]/section[9]/p[1]").text == "Teton Turf and Tree"
  
  def test_3cListbutton(self):
    self.driver.get("http://127.0.0.1:5500/cse270-teton/teton/1.6/directory.html")
    self.driver.find_element(By.XPATH, "//*[@id=\"directory-list\"]").click()
  
  def test_3dTetonTurfandTreeList(self):
    self.driver.get("http://127.0.0.1:5500/cse270-teton/teton/1.6/directory.html")
    self.driver.find_element(By.XPATH, "//*[@id=\"directory-list\"]").click()
    assert self.driver.find_element(By.XPATH, "/html/body/div/main/div[2]/section[9]/p[1]").text == "Teton Turf and Tree"
  
  def test_4aFirstName(self):
    self.driver.get("http://127.0.0.1:5500/cse270-teton/teton/1.6/join.html")
    elements = self.driver.find_elements(By.XPATH, "/html/body/div/main/section/form/fieldset/label[1]/input")
    assert len(elements) > 0
  
  def test_4bcdFillinSubmitCheckEmail(self):
    self.driver.get("http://127.0.0.1:5500/cse270-teton/teton/1.6/join.html")
    self.driver.find_element(By.XPATH, "/html/body/div/main/section/form/fieldset/label[1]/input").send_keys("Ella")
    self.driver.find_element(By.XPATH, "/html/body/div/main/section/form/fieldset/label[2]/input").send_keys("Galbraith")
    self.driver.find_element(By.NAME, "bizname").send_keys("Business Name")
    self.driver.find_element(By.NAME, "biztitle").send_keys("Biz Title lol")
    self.driver.find_element(By.NAME, "submit").click()
    elements = self.driver.find_elements(By.NAME, "email")
    assert len(elements) > 0
  
  def test_5IncorrectLogin(self):
    self.driver.get("http://127.0.0.1:5500/cse270-teton/teton/1.6/admin.html")
    elements = self.driver.find_elements(By.NAME, "username")
    assert len(elements) > 0
    self.driver.find_element(By.NAME, "username").send_keys("incorrect")
    self.driver.find_element(By.NAME, "password").send_keys("password")
    self.driver.find_element(By.XPATH, "/html/body/div/main/section[1]/form/fieldset/input").click()
    elements = self.driver.find_elements(By.XPATH, "/html/body/div/main/section[1]/form/div/span")
    assert len(elements) > 0
  
