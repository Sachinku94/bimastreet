from utilities.base_class import BaseClass

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import time
import pytest
from tests.Pages.quotepagebimastreet import QuotePage
from object.Selenium_helper import SeleniumHelper
import asyncio


class Testone(BaseClass):

    
    def test_healthleadprequote(self):
        healthlead=QuotePage(self.driver)
        healthlead.healthpre()
    def test_healthleadpostquote(self):
        healthleadpost=QuotePage(self.driver)
        healthleadpost.healthpost()
    def test_healthleadkyc(self):
        healthleadkyc=QuotePage(self.driver)
        healthleadkyc.healthkyc()
    def test_healthckyc(self):
        healthckyc=QuotePage(self.driver)
        healthckyc.healthckyc()






        