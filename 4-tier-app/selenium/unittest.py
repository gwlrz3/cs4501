# import unittest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time

time.sleep(10)

driver = webdriver.Remote(
    command_executor='http://selenium-chrome:4444/wd/hub',
    desired_capabilities=DesiredCapabilities().CHROME)

driver.get("http://web:8000")
assert "Office" in driver.title

driver.close()

