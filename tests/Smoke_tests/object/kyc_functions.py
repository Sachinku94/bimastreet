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
        formatter = logging.Formatter(
            "%(asctime)s :%(levelname)s : %(name)s :%(message)s"
        )
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object

        logger.setLevel(logging.DEBUG)
        return logger
    def Kycfunction(self):
    
        stored_index = None
        
        
        Kyc_fields = (By.CSS_SELECTOR, ".evInputField .MuiInputBase-root .MuiInputBase-input")
        
        
        Kyc_formsubmission = self.wait.until(EC.presence_of_all_elements_located(Kyc_fields))
        
        
        for kyc in Kyc_formsubmission:

            
            idkyc = kyc.get_attribute('id')
            
            if idkyc== "H.No. / Building"  or idkyc=="Pincode" or idkyc=="Document ID" or idkyc=="Proposer Full Name" :
                
                
                kyes = test_alldata.Kyc_Details.keys()
                
                for ky in kyes:
                    
                    if ky == idkyc:
                        
                        if stored_index is None:
                            
                            random_value = random.choice(test_alldata.Kyc_Details[ky])  
                            stored_index = test_alldata.Kyc_Details[ky].index(random_value)  
                            
                            
                            kyc.clear()  
                            kyc.send_keys(random_value)  
                        else:
                            
                            selected_value = test_alldata.Kyc_Details[ky][stored_index]  
                           
                            kyc.clear()  
                            kyc.send_keys(selected_value)  
                            
                        time.sleep(5)

            elif idkyc =="document_for_verification-autocomplete" or idkyc=="income_source-autocomplete" or idkyc=="occupation-autocomplete" or idkyc=="city-autocomplete" or idkyc=="area_/_town_/_locality-autocomplete":

                     kyes = test_alldata.Kyc_Details.keys()
                
                     for ky in kyes:
                    
                        if ky == idkyc:
                        
                        
                            
                        
                            
                            selected_value = test_alldata.Kyc_Details[ky][stored_index]  
                           
                            kyc.clear()  
                            kyc.send_keys(selected_value) 
                            selec_value=By.CSS_SELECTOR,".css-ue1yok .MuiAutocomplete-option" 
                            select_val=self.wait.until(EC.presence_of_element_located(selec_value))
                            select_val.click()
            elif idkyc=="gender" :
                     self.log.info("done cl")
                     kyes = test_alldata.Kyc_Details.keys()
                
                     for ky in kyes:
                    
                        if ky == idkyc:
                             selected_value = test_alldata.Kyc_Details[ky][stored_index] 
                             self.log.info("done cli")
                             
                             self.log.info("done clear")
                             kyc.click()
                             self.log.info("done click gender")
                             selec_value=By.CSS_SELECTOR,".MuiMenu-paper .MuiMenu-list .MuiMenuItem-root" 
                             select_val=self.wait.until(EC.presence_of_all_elements_located(selec_value))
                             for sel in select_val:
                                  text_val=sel.text.strip()
                                  if text_val==selected_value:
                                       sel.click()
                                  break
            elif idkyc=="ckycproposerdob":
                     kyes = test_alldata.Kyc_Details.keys()
                
                     for ky in kyes:
                    
                        if ky == idkyc:
                             selected_value = test_alldata.Kyc_Details[ky][stored_index]
                             yearsel=SeleniumHelper.calander_picker(self,dob=selected_value)
                             yearsel
                     
                             
                        
                        
                            
                        
                            
                                  

                        
                        
                                  