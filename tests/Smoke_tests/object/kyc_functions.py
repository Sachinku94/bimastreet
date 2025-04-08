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

class KYc_function:
    def __init__(self, driver):
        self.driver = driver

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
                        
                            # self.log.info(print(f"Sent '{selected_value if stored_index is not None else random_value}' to field '{idkyc}'"))


                        
                        
                                  