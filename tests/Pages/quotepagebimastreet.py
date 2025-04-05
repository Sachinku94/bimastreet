# from Pages import homepagejio
# from Smoke_tests.utilities.base_class import BaseClass
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
# import time
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from tests.test_data import test_data
# import requests
# import random
# from Smoke_tests.object.Selenium_helper import SeleniumHelper
# class QuotePage(BaseClass):

#     def __init__(self, driver):
#         self.driver = driver
    
#     def motor(self):
#         log=self.getLogger()
#         Ac = ActionChains(self.driver)
#         wait = WebDriverWait(self.driver, 20)
#         quote=homepagejio.HomePage
#         quote.leads(self)
#         prod=By.CSS_SELECTOR,"div.css-12hd50 p"
#         product=wait.until(EC.presence_of_all_elements_located(prod))
        
        
#         for podu in product:
#                     pod=podu.text
#                     if pod=="Car":
                    

#                         vehino="Enter car registration number"
#                         vehin=self.driver.find_element(By.ID,vehino)
#                         vehin.send_keys("MH01WG7452")
#                         mobino="Enter mobile number"
#                         mobin=self.driver.find_element(By.ID,mobino)
#                         mobin.send_keys("7894566623")
#                         button="button#Get\ free\ quotes"
#                         buttonquo=self.driver.find_element(By.CSS_SELECTOR,button)
#                         buttonquo.click()
#                         time.sleep(5)

#                         br=By.ID,"#make"
#                         brands=wait.until(EC.visibility_of_all_elements_located(br))
                        
                        
#                         if brands:
#                             time.sleep(4)
                        
#                             ra_br=random.choice(brands)
#                             ra_br.click()
#                         time.sleep(5)
                        
                        
                            
#                         vars=By.ID,"#model"
#                         varints=wait.until(EC.visibility_of_all_elements_located(vars)) 
                        
#                         if varints:
#                                 ra_vr=random.choice(varints)
#                                 ra_vr.click()
#                                 time.sleep(9)
#                                 log.info("trupass")
#     def healthpre(self):
#         time.sleep(5)
#         log=self.getLogger()
#         Ac = ActionChains(self.driver)
#         wait = WebDriverWait(self.driver, 20)
        
#         prod=By.CSS_SELECTOR,".product-section li"
#         product=wait.until(EC.presence_of_all_elements_located(prod))
        
        
#         for podu in product:
#                     pod=podu.get_attribute("id")
#                     if pod=="health": 
                          
#                         podu.click()  

#                         time.sleep(5)           
                        
#                         checkbox=By.CSS_SELECTOR,"input.PrivateSwitchBase-input.css-1m9pwf3"
#                         selectcheck=wait.until(EC.presence_of_all_elements_located(checkbox))
#                         ra_slcheck=random.choice(selectcheck)
#                         value=ra_slcheck.get_attribute("id")
#                         log.info(value)
                        
#                         if value=="One Adult":
                            
                                
                                
                                
#                                 rel=By.CSS_SELECTOR,"button.MuiButtonBase-root.MuiIconButton-root.MuiIconButton-edgeEnd.MuiIconButton-sizeMedium.css-slyssw"
#                                 relation=wait.until(EC.visibility_of_element_located(rel))
                                
#                                 relation.click()
#                                 calander =By.CSS_SELECTOR,".MuiButtonBase-root.MuiIconButton-root.MuiIconButton-sizeSmall.MuiPickersCalendarHeader-switchViewButton.css-1wjkg3"
#                                 alclander=wait.until(EC.visibility_of_element_located(calander))
#                                 alclander.click()
#                                 year_slec=By.CSS_SELECTOR,".MuiPickersYear-root.css-1p8hrm8"
#                                 allYear_slec=wait.until(EC.presence_of_all_elements_located(year_slec))
#                                 sel=random.choice(allYear_slec)
#                                 sel.click()
#                                 try:
#                                     month_slec=By.CSS_SELECTOR,"div.MuiPickersArrowSwitcher-root.css-k008qs button"
#                                     all_monthslec=wait.until(EC.presence_of_all_elements_located(month_slec))
#                                     mont=random.choice(all_monthslec)
#                                     for _ in range(3):
                                        
#                                             mont.click()
#                                             time.sleep(3)
#                                 except Exception:
#                                       ()
                                    
#                                 date_slec=By.CSS_SELECTOR,".css-a78wou"
#                                 alldate_slec=wait.until(EC.visibility_of_any_elements_located(date_slec))
#                                 date=random.choice(alldate_slec)
#                                 date.click()
#                                 gender=By.CSS_SELECTOR,".css-qiwgdb.css-qiwgdb.css-qiwgdb"
#                                 gendersel=wait.until(EC.presence_of_element_located(gender))
#                                 gendersel.click()
#                                 se=By.CSS_SELECTOR,".MuiButtonBase-root.MuiMenuItem-root.MuiMenuItem-gutters.MuiMenuItem-root.MuiMenuItem-gutters.css-1km1ehz"
#                                 se_sel=wait.until(EC.presence_of_all_elements_located(se))
#                                 sel_se=random.choice(se_sel)
#                                 sel_se.click()
#                                 continue_btn=By.CSS_SELECTOR,".MuiButton-root"
#                                 continue_but=wait.until(EC.presence_of_element_located(continue_btn))
#                                 continue_but.click()

                                 
#                                 # qutbut=self.driver.find_element(By.CSS_SELECTOR,".primaryBtns .MuiButton-root")
#                                 # qutbut.click()
                                
                                
                            
                                
                                
                                
#                         elif value=="Two Adults" :
#                                 ra_slcheck.click()
#                                 time.sleep(5)
#                                 rel=By.CSS_SELECTOR,"button.MuiButtonBase-root.MuiIconButton-root.MuiIconButton-edgeEnd.MuiIconButton-sizeMedium.css-slyssw"
#                                 relation=wait.until(EC.visibility_of_all_elements_located(rel))
#                                 for rela in relation:
#                                       rela.click()
                                      
#                                       calander =By.CSS_SELECTOR,".MuiButtonBase-root.MuiIconButton-root.MuiIconButton-sizeSmall.MuiPickersCalendarHeader-switchViewButton.css-1wjkg3"
#                                       alclander=wait.until(EC.visibility_of_element_located(calander))
#                                       alclander.click()
#                                       time.sleep(3)
#                                       year_slec=By.CSS_SELECTOR,".MuiPickersYear-root.css-1p8hrm8"
#                                       allYear_slec=wait.until(EC.presence_of_all_elements_located(year_slec))
#                                       sel=random.choice(allYear_slec)
#                                       sel.click()
#                                       try:
#                                         month_slec=By.CSS_SELECTOR,"div.MuiPickersArrowSwitcher-root.css-k008qs button"
#                                         all_monthslec=wait.until(EC.presence_of_all_elements_located(month_slec))
#                                         mont=random.choice(all_monthslec)
#                                         for _ in range(3):
                                        
#                                                 mont.click()
#                                                 time.sleep(3)
#                                       except Exception:
#                                             ()
                                        
#                                       date_slec=By.CSS_SELECTOR,".css-a78wou"
#                                       alldate_slec=wait.until(EC.visibility_of_any_elements_located(date_slec))
#                                       date=random.choice(alldate_slec)
#                                       date.click()
#                                       time.sleep(3)
#                                 gender=By.CSS_SELECTOR,".css-qiwgdb.css-qiwgdb.css-qiwgdb"
#                                 gendersel=wait.until(EC.presence_of_all_elements_located(gender))
#                                 for gen in gendersel:
                                            
#                                             gen.click()
#                                             se=By.CSS_SELECTOR,".MuiButtonBase-root.MuiMenuItem-root.MuiMenuItem-gutters.MuiMenuItem-root.MuiMenuItem-gutters.css-1km1ehz"
#                                             se_sel=wait.until(EC.presence_of_all_elements_located(se))
#                                             sel_se=random.choice(se_sel)
#                                             sel_se.click() 
#                                             time.sleep(3) 
#                                 time.sleep(2)    
#                                 continue_btn=By.CSS_SELECTOR,".MuiButton-root"
#                                 continue_but=wait.until(EC.presence_of_element_located(continue_btn))
#                                 continue_but.click()        
                                      
                                

                                    
                                            
#                         elif value == "Daughter " or value == "Son ":
#                                 ra_slcheck.click()
#                                 time.sleep(5)
#                                 rel=By.CSS_SELECTOR,"button.MuiButtonBase-root.MuiIconButton-root.MuiIconButton-edgeEnd.MuiIconButton-sizeMedium.css-slyssw"
#                                 relation=wait.until(EC.visibility_of_all_elements_located(rel))
#                                 for rela in relation:
#                                       rela.click()
                                      
#                                       calander =By.CSS_SELECTOR,".MuiButtonBase-root.MuiIconButton-root.MuiIconButton-sizeSmall.MuiPickersCalendarHeader-switchViewButton.css-1wjkg3"
#                                       alclander=wait.until(EC.visibility_of_element_located(calander))
#                                       alclander.click()
#                                       time.sleep(2)
#                                       year_slec=By.CSS_SELECTOR,".MuiPickersYear-root.css-1p8hrm8"
#                                       allYear_slec=wait.until(EC.presence_of_all_elements_located(year_slec))
#                                       sel=random.choice(allYear_slec)
#                                       sel.click()
#                                       try:
#                                         month_slec=By.CSS_SELECTOR,"div.MuiPickersArrowSwitcher-root.css-k008qs button"
#                                         all_monthslec=wait.until(EC.presence_of_all_elements_located(month_slec))
#                                         mont=random.choice(all_monthslec)
#                                         for _ in range(3):
                                            
#                                                 mont.click()
#                                                 time.sleep(3)
#                                       except Exception:
#                                             ()
                                        
#                                       date_slec=By.CSS_SELECTOR,".css-a78wou"
#                                       alldate_slec=wait.until(EC.visibility_of_any_elements_located(date_slec))
#                                       date=random.choice(alldate_slec)
#                                       date.click()
#                                       time.sleep(3)
#                                 time.sleep(2)
#                                 gender=By.CSS_SELECTOR,".css-qiwgdb.css-qiwgdb.css-qiwgdb"
#                                 gendersel=wait.until(EC.presence_of_element_located(gender))
#                                 gendersel.click()
#                                 se=By.CSS_SELECTOR,".MuiButtonBase-root.MuiMenuItem-root.MuiMenuItem-gutters.MuiMenuItem-root.MuiMenuItem-gutters.css-1km1ehz"
#                                 se_sel=wait.until(EC.presence_of_all_elements_located(se))
#                                 sel_se=random.choice(se_sel)
#                                 sel_se.click()     
#                                 continue_btn=By.CSS_SELECTOR,".MuiButton-root"
#                                 continue_but=wait.until(EC.presence_of_element_located(continue_btn))
#                                 continue_but.click()
                                 
                            
                            
#                         break            
#                     else:
#                           continue
                        
                           
                    
                                       
                    
                
#         log.info("prequote pass")

from Pages import homepagejio
from Smoke_tests.utilities.base_class import BaseClass
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.test_data import test_alldata
import time
import random
import logging
from Smoke_tests.object.Selenium_helper import SeleniumHelper

class QuotePage(BaseClass):

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)
        self.ac = ActionChains(self.driver)
        self.log = self.getLogger()

    def motor(self):
        try:
            homepagejio.HomePage.leads(self)
            products = self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.css-12hd50 p")))

            for product in products:
                if product.text == "Car":
                    self.driver.find_element(By.ID, "Enter car registration number").send_keys("MH01WG7452")
                    self.driver.find_element(By.ID, "Enter mobile number").send_keys("7894566623")
                    self.driver.find_element(By.CSS_SELECTOR, "button#Get\\ free\\ quotes").click()

                    time.sleep(4)  # Delay to prevent stale element
                    brands = self.wait.until(EC.visibility_of_all_elements_located((By.ID, "make")))
                    random.choice(brands).click()

                    time.sleep(5)  # Delay to prevent stale element
                    variants = self.wait.until(EC.visibility_of_all_elements_located((By.ID, "model")))
                    random.choice(variants).click()
                    self.log.info("Motor quote completed successfully")
                    break
        except Exception as e:
            self.log.error(f"Motor quote failed: {e}")
            self.log.info(f"Current URL: {self.driver.current_url}")

    def healthpre(self):
        try:
            products = self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".product-section li")))

            for product in products:
                if product.get_attribute("id") == "health":
                    product.click()

                    checkboxes = self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "input.PrivateSwitchBase-input.css-1m9pwf3")))
                    selected_checkbox = random.choice(checkboxes)
                    value = selected_checkbox.get_attribute("id").strip()
                    self.log.info(value)

                    selected_checkbox.click()
                    time.sleep(5)  # Delay to prevent stale element
                    self._fill_health_form(value)
                    break

            self.log.info("Health prequote passed")

        except Exception as e:
            self.log.error(f"Health quote failed: {e}")
            self.log.info(f"Current URL: {self.driver.current_url}")

    def _fill_health_form(self, value):
        def select_date():
            self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".MuiButtonBase-root.MuiIconButton-root.MuiIconButton-sizeSmall.MuiPickersCalendarHeader-switchViewButton.css-1wjkg3"))).click()
            random.choice(self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".MuiPickersYear-root.css-1p8hrm8")))).click()
            try:
                for _ in range(3):
                    random.choice(self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.MuiPickersArrowSwitcher-root.css-k008qs button")))).click()
                    time.sleep(3)  # Delay to prevent stale element
            except Exception:
                pass
            random.choice(self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".css-a78wou")))).click()

        def select_gender():
            self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".css-qiwgdb.css-qiwgdb.css-qiwgdb"))).click()
            random.choice(self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".MuiButtonBase-root.MuiMenuItem-root.MuiMenuItem-gutters.MuiMenuItem-root.MuiMenuItem-gutters.css-1km1ehz")))).click()

        relations = self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "button.MuiButtonBase-root.MuiIconButton-root.MuiIconButton-edgeEnd.MuiIconButton-sizeMedium.css-slyssw")))

        for rel in relations:
            rel.click()
            time.sleep(3)  # Delay to prevent stale element
            select_date()

        time.sleep(2)  # Delay to prevent stale element
        select_gender()

        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".MuiButton-root"))).click()
        personal_detail=By.CSS_SELECTOR,".evInputField .MuiInputBase-root .MuiInputBase-input"
        per_det=self.wait.until(EC.presence_of_all_elements_located(personal_detail))
        field_order = ["mobile", "pincode"]  # Ensure this matches how fields appear in the DOM
        Personal_Details=test_alldata.Personal_Details
# Loop through the fields and send a random value
        for i, key in enumerate(field_order):
            element = per_det[i]
            value_to_send = random.choice(Personal_Details[key])
            element.clear()
            element.send_keys(value_to_send)
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".MuiButton-root"))).click() 
        time.sleep(10)
        qotepageurl=self.driver.current_url
        
        Save_file=SeleniumHelper.save_to_test_data
        Save_file(qotepageurl)
        assert "quote_no"   in  qotepageurl
        self.log.info(qotepageurl)

        time.sleep(10)

    def healthpost(self):
        helthqoteurl=test_alldata.Health_post
        self.driver.get(helthqoteurl)


