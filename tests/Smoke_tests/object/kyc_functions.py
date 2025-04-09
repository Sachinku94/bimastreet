from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import NoSuchElementException
from concurrent.futures import ThreadPoolExecutor
from selenium.common.exceptions import TimeoutException
import inspect
import logging
import requests
import asyncio
import aiohttp
import time
import inspect
import test_data.test_alldata
import test_data.test_alldata
import random
from test_data import test_alldata
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from object.Selenium_helper import SeleniumHelper

    
                        
class KYc_function:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)
        self.log = self.getLogger()

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler("logfile.log")
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)  # filehandler object
        logger.setLevel(logging.DEBUG)
        return logger

    def clear_and_fill_field(self, field, value):
        """Helper function to clear and fill the input field."""
        field.clear()
        field.send_keys(value)
        self.log.info(f"Filled field with value: {value}")

    def select_from_autocomplete(self, field, value, selector):
        """Helper function to fill autocomplete fields and select a value."""
        KYc_function.clear_and_fill_field(self,field, value)
        select_val = self.wait.until(EC.presence_of_element_located(selector))
        select_val.click()
        self.log.info(f"Selected from autocomplete: {value}")

    def select_gender(self, kyc, selected_value):
        """Helper function to select the gender."""
        self.log.info("Selecting gender...")
        kyc.click()
        gender_options = self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".MuiMenu-paper .MuiMenu-list .MuiMenuItem-root")))
        for option in gender_options:
            if option.text.strip() == selected_value:
                option.click()
                self.log.info(f"Gender selected: {selected_value}")
                break

    def Kycfunction(self):
        stored_index = None
        Kyc_fields = (By.CSS_SELECTOR, ".evInputField .MuiInputBase-root .MuiInputBase-input")
        Kyc_formsubmission = self.wait.until(EC.presence_of_all_elements_located(Kyc_fields))

        # Loop through all KYC fields
        for kyc in Kyc_formsubmission:
            idkyc = kyc.get_attribute('id')

            if idkyc in ["H.No. / Building", "Pincode", "Document ID", "Proposer Full Name"]:
                kyes = test_alldata.Kyc_Details.keys()
                for ky in kyes:
                    if ky == idkyc:
                        # Select a random value if no stored index, otherwise reuse the stored value
                        value_to_enter = random.choice(test_alldata.Kyc_Details[ky]) if stored_index is None else test_alldata.Kyc_Details[ky][stored_index]
                        stored_index = test_alldata.Kyc_Details[ky].index(value_to_enter)
                        KYc_function.clear_and_fill_field(self,kyc, value_to_enter)
                        time.sleep(5)

            elif idkyc in ["document_for_verification-autocomplete", "income_source-autocomplete", "occupation-autocomplete", "city-autocomplete", "area_/_town_/_locality-autocomplete"]:
                kyes = test_alldata.Kyc_Details.keys()
                for ky in kyes:
                    if ky == idkyc:
                        value_to_enter = test_alldata.Kyc_Details[ky][stored_index]
                        # Select value from the autocomplete dropdown
                        KYc_function.select_from_autocomplete(self,kyc, value_to_enter, (By.CSS_SELECTOR, ".css-ue1yok .MuiAutocomplete-option"))
                        time.sleep(5)

            elif idkyc == "gender":
                kyes = test_alldata.Kyc_Details.keys()
                for ky in kyes:
                    if ky == idkyc:
                        selected_value = test_alldata.Kyc_Details[ky][stored_index]
                        KYc_function.select_gender(self,kyc, selected_value)
                        time.sleep(5)

            elif idkyc == "ckycproposerdob":
                kyes = test_alldata.Kyc_Details.keys()
                for ky in kyes:
                    if ky == idkyc:
                        selected_value = test_alldata.Kyc_Details[ky][stored_index]
                        # Assuming the `calander_picker` function is available and works fine
                        SeleniumHelper.calander_picker(self, dob=selected_value)
                        break
                time.sleep(3)                       
                            
                        
                            
                                  

                        
                        
                                  