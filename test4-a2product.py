import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


class FoodService_test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_customer(self):
        user = "instructor"
        pwd = "instructor1a"
        pro = "test"
        desc = "test"
        quan = 1
        char = 100
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
        elem = driver.find_element_by_xpath("//*/div/div/div/div[2]/div/div/div/div/div[3]/div/div/p[2]/a").click()
        elem = driver.find_element_by_xpath("//*/div/div/div/div[3]/div/a/span").click()
        name = Select(driver.find_element_by_id("id_cust_name"))
        name.select_by_visible_text('Barbara York')
        elem = driver.find_element_by_id("id_product")
        elem.send_keys(pro)
        elem = driver.find_element_by_id("id_p_description")
        elem.send_keys(desc)
        elem = driver.find_element_by_id("id_quantity")
        elem.send_keys(quan)
        elem = driver.find_element_by_id("id_charge")
        elem.send_keys(char)
        elem = driver.find_element_by_xpath("//*/div/div/div/form/button").click()
        time.sleep(2)

    def tearDown(self):
        self.driver.close()

    if __name__ == "__main__":
        unittest.main()