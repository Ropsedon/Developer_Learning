# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
import os


class DeployMS(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        # self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_deploy_m_s(self):
        driver = self.driver
        self.open_consul_home_page(driver, link="http://ua1-2317-pc:8500/ui/dc1/services")
        self.open_key_value_consul(driver)
        self.create_consul_ms(driver)
        self.deploy_mongo_net462(driver, way_ms="Applications/SBTech.Microservices.Mongo.net462")
        self.create_consul_ms(driver)
        self.deploy_callother_net462(driver, way_ms="Applications/SBTech.Microservices.Test.CallOtherMicroservice.net462")
        driver.find_element_by_link_text("Applications").click()
        driver.find_element_by_link_text("Services").click()

    def deploy_callother_net462(self, driver, way_ms):
        driver.find_element_by_name("additional").click()
        driver.find_element_by_name("additional").clear()
        driver.find_element_by_name("additional").send_keys(way_ms)
        driver.find_element_by_name("value").click()
        # Open directory which contain config files
        files_directory = "\\Config_MSs\\CallOther_net462.txt"
        path = os.getcwd() + files_directory
        configs_ms = open(path, 'r+')
        data_json = configs_ms.read()
        driver.find_element_by_name("value").send_keys(data_json)
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Value'])[1]/following::button[1]").click()
        configs_ms.close()

    def deploy_mongo_net462(self, driver, way_ms):
        driver.find_element_by_name("additional").click()
        driver.find_element_by_name("additional").clear()
        driver.find_element_by_name("additional").send_keys(way_ms)
        driver.find_element_by_name("value").click()
        driver.find_element_by_name("value").clear()
        # Open directory which contain config files
        files_directory = "\\Config_MSs\\mongo_net462.txt"
        path = os.getcwd() + files_directory
        configs_ms = open(path, 'r+')
        data_json = configs_ms.read()
        driver.find_element_by_name("value").send_keys(data_json)
        driver.find_element_by_xpath(
           "(.//*[normalize-space(text()) and normalize-space(.)='Value'])[1]/following::button[1]").click()
        configs_ms.close()

    def create_consul_ms(self, driver):
        driver.find_element_by_link_text("Create").click()

    def open_key_value_consul(self, driver):
        driver.find_element_by_link_text("Key/Value").click()

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
