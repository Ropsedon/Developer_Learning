# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_untitled_test_case(self):
        driver = self.driver
        driver.get("http://kyiv-win-inf01:8500/ui/#/dev-dc1/services")
        driver.find_element_by_id("ember477").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='+'])[1]/following::div[5]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='+'])[1]/following::div[5]").click()
        driver.find_element_by_id("ember734").click()
        driver.find_element_by_id("ember734").click()
        # ERROR: Caught exception [ERROR: Unsupported command [doubleClick | id=ember734 | ]]
        driver.find_element_by_id("ember734").clear()
        driver.find_element_by_id("ember734").send_keys("{\n    \"Id\": \"SBTech.Microservices.Test.Microservice.Mongo\",\n    \"Service\": \"1c57\",\n    \"Active\": false,\n    \"Version\": \"2.4.5-RC-4245\",\n    \"TargetClusters\": [\n        \"kyiv-win-inf01\"\n    ],\n    \"Environment\": \"DEV\",\n    \"SelfHostVersion\": \"2.4.5-RC-4269\", \n    \"Count\": 3,\n    \"Properties\": {\n        \"dotnet-runtime\": \"net462\"\n    },\n    \"ConfigPath\": \"SBTech.Microservices.Test.Microservice.Mongo.2.4.5-RC-4245/lib/config.json\"\n}")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Cancel'])[1]/preceding::button[1]").click()
        driver.find_element_by_id("ember734").click()
        driver.find_element_by_id("ember734").click()
        # ERROR: Caught exception [ERROR: Unsupported command [doubleClick | id=ember734 | ]]
        driver.find_element_by_id("ember734").clear()
        driver.find_element_by_id("ember734").send_keys("{\n    \"Id\": \"SBTech.Microservices.Test.Microservice.Mongo\",\n    \"Service\": \"1c57\",\n    \"Active\": true,\n    \"Version\": \"2.4.5-RC-4245\",\n    \"TargetClusters\": [\n        \"kyiv-win-inf01\"\n    ],\n    \"Environment\": \"DEV\",\n    \"SelfHostVersion\": \"2.4.5-RC-4269\", \n    \"Count\": 3,\n    \"Properties\": {\n        \"dotnet-runtime\": \"net462\"\n    },\n    \"ConfigPath\": \"SBTech.Microservices.Test.Microservice.Mongo.2.4.5-RC-4245/lib/config.json\"\n}")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Cancel'])[1]/preceding::button[1]").click()
    
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
