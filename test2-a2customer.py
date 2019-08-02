import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class FoodService_test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_customer(self):
        user = "instructor"
        pwd = "instructor1a"
        driver = self.driver
        driver.maximize_window()
        driver.get("http://peightal.pythonanywhere.com/admin")
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        driver.get("http://peightal.pythonanywhere.com/")
        assert "Logged In"
        elem = driver.find_element_by_xpath("//*/ul[1]/li[2]/a").click()
        elem = driver.find_element_by_xpath("//*/div/div/div/div[3]/table/tbody/tr[1]/td[12]/a").click()
        elem = driver.find_element_by_xpath("/html/body/form/button").click()
        elem = driver.find_element_by_xpath("//*/div/div/div/div[3]/table/tbody/tr[1]/td[14]/a").click()
        time.sleep(1)

    def tearDown(self):
        self.driver.close()

    if __name__ == "__main__":
        unittest.main()
