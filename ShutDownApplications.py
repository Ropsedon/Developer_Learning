# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
import os


class ShutDownApplications(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        # self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_down_applications(self):
        driver = self.driver
        self.open_consul_home_page(driver, link="http://ua1-2317-pc:8500/ui/dc1/services")
        driver.find_element_by_link_text("Key/Value").click()
        driver.find_element_by_link_text("Applications").click()
        self.down_mongo_ms(driver)
        self.down_callother_ms(driver)
        driver.close()

    def down_mongo_ms(self, driver):
        driver.find_element_by_link_text("SBTech.Microservices.Mongo.net462").click()
        driver.find_element_by_name("value").click()
        driver.find_element_by_name("value").clear()
        # Open directory which contain config files
        files_directory = "\\Config_MSs\\mongo_net462.txt"
        path = os.getcwd() + files_directory
        configs_ms = open(path, 'r+')
        data_json = configs_ms.read()
        # Change status
        data_json = data_json.replace('true', 'false')
        driver.find_element_by_name("value").send_keys(data_json)
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Value'])[1]/following::button[1]").click()
        configs_ms.close()

    def down_callother_ms(self, driver):
        driver.find_element_by_link_text("SBTech.Microservices.Test.CallOtherMicroservice.net462").click()
        driver.find_element_by_name("value").click()
        driver.find_element_by_name("value").clear()
        # Open directory which contain config files
        files_directory = "\\Config_MSs\\CallOther_net462.txt"
        path = os.getcwd() + files_directory
        configs_ms = open(path, 'r+')
        data_json = configs_ms.read()
        # Change status
        data_json = data_json.replace('true', 'false')
        driver.find_element_by_name("value").send_keys(data_json)
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Value'])[1]/following::button[1]").click()
        configs_ms.close()

    def open_consul_home_page(self, driver, link):
        driver.get(link)

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True

    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
