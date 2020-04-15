import unittest 
from selenium import webdriver 

from selenium.webdriver.chrome.options import Options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')

class FooBarTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(chrome_options=chrome_options)

@classmethod
def tearDownClass(cls):
    cls.driver.quit()

def setUP(self):
    self.driver.get("http://travel.agileway.net")

def tearDown(self):
    self.driver.find.element_by_link_text("Sign off").click()

def test_first_case(self):
    self.assertEqual("Agile Travels", self.driver.title)
    self.driver.find_element_by_name("usernarne").send_keys("agileway")

def test_second_case(self):
        self.driver.find_element_by_id("register_link").click()
        self.assertIn("Register",self.driver.find_element_by_tag_name("body").text)