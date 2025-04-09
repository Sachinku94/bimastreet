from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time, random, logging, inspect
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
from concurrent.futures import ThreadPoolExecutor
import threading
from selenium.webdriver.common.keys import Keys
    
                                             

class KYc_function:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)
        self.log = KYc_function.getLogger(self)

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler("logfile.log")
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        if not logger.handlers:
            logger.addHandler(fileHandler)
        logger.setLevel(logging.DEBUG)
        return logger

    def clear_and_fill_field(self, field, value):
        field.clear()
        field.send_keys(value)
        self.log.info(f"Filled field with value: {value}")

    def select_from_autocomplete(self, field, value, selector):
        KYc_function.clear_and_fill_field(self, field, value)
        select_val = self.wait.until(EC.presence_of_element_located(selector))
        select_val.click()
        self.log.info(f"Selected from autocomplete: {value}")

    def select_gender(self, kyc, selected_value):
        self.log.info("Selecting gender...")
        kyc.click()
        gender_options = self.wait.until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, ".MuiMenu-paper .MuiMenu-list .MuiMenuItem-root")
            )
        )
        for option in gender_options:
            if option.text.strip() == selected_value:
                option.click()
                self.log.info(f"Gender selected: {selected_value}")
                break


                            

    def Kycfunction(self):
        Kyc_Details = test_alldata.Kyc_Details
        stored_index = None

        Kyc_fields = (By.CSS_SELECTOR, ".evInputField .MuiInputBase-root .MuiInputBase-input")
        try:
            Kyc_formsubmission = self.wait.until(EC.presence_of_all_elements_located(Kyc_fields))
        except TimeoutException:
            self.log.error("Timeout while waiting for KYC form fields.")
            return

        for kyc in Kyc_formsubmission:
            try:
                idkyc = kyc.get_attribute('id')
                self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", kyc)
                self.wait.until(EC.element_to_be_clickable(kyc))

                if idkyc in ["H.No. / Building", "Pincode", "Document ID", "Proposer Full Name"]:
                    if idkyc in Kyc_Details:
                        value = random.choice(Kyc_Details[idkyc]) if stored_index is None else Kyc_Details[idkyc][stored_index]
                        stored_index = Kyc_Details[idkyc].index(value)
                        kyc.click()
                        kyc.clear()
                        kyc.send_keys(value)
                        kyc.send_keys(Keys.TAB)
                        self.log.info(f"{idkyc} filled with {value}")

                elif idkyc in [
                    "document_for_verification-autocomplete",
                    "income_source-autocomplete",
                    "occupation-autocomplete",
                    "city-autocomplete",
                    "area_/_town_/_locality-autocomplete"
                ]:
                    if idkyc in Kyc_Details:
                        value = Kyc_Details[idkyc][stored_index]
                        kyc.click()
                        kyc.clear()
                        kyc.send_keys(value)
                        self.wait.until(
                            EC.visibility_of_element_located((By.CSS_SELECTOR, ".MuiAutocomplete-popper .MuiAutocomplete-option"))
                        ).click()
                        self.log.info(f"{idkyc} selected: {value}")

                elif idkyc == "gender":
                    if idkyc in Kyc_Details:
                        value = Kyc_Details[idkyc][stored_index]
                        KYc_function.select_gender(self,kyc, value)

                elif idkyc == "ckycproposerdob":
                    if idkyc in Kyc_Details:
                        value = Kyc_Details[idkyc][stored_index]
                        SeleniumHelper.calander_picker(self, dob=value)
                        self.log.info(f"DOB set to: {value}")

            except (StaleElementReferenceException, NoSuchElementException, TimeoutException) as e:
                self.log.warning(f"Retrying field {idkyc} due to exception: {str(e)}")
                continue

        self.log.info("KYC form filling completed.")

                                  

                        
                        
                                  