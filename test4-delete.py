import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


class adnew(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_blog(self):
        user = "instructor"
        pwd = "instructor1a"
        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000/admin")
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        assert "Logged In"
        time.sleep(1)
        elem = driver.find_element_by_xpath("//*/div[2]/table/tbody/tr/td[2]/a").click()
        time.sleep(1)
        elem = driver.find_element_by_xpath("//*/tbody/tr[1]/td/input").click()
        delete = Select(driver.find_element_by_name("action"))
        delete.select_by_visible_text('Delete selected posts')
        elem = driver.find_element_by_xpath("// * / div[1] / button").click()

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
