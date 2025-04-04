from Pages import homepagejio
from Smoke_tests.utilities.base_class import BaseClass
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.test_data import test_data
import requests
import random
from Smoke_tests.object.Selenium_helper import SeleniumHelper
class QuotePage(BaseClass):

    def __init__(self, driver):
        self.driver = driver
    
    def motor(self):
        log=self.getLogger()
        Ac = ActionChains(self.driver)
        wait = WebDriverWait(self.driver, 20)
        quote=homepagejio.HomePage
        quote.leads(self)
        prod=By.CSS_SELECTOR,"div.css-12hd50 p"
        product=wait.until(EC.presence_of_all_elements_located(prod))
        
        
        for podu in product:
                    pod=podu.text
                    if pod=="Car":
                    

                        vehino="Enter car registration number"
                        vehin=self.driver.find_element(By.ID,vehino)
                        vehin.send_keys("MH01WG7452")
                        mobino="Enter mobile number"
                        mobin=self.driver.find_element(By.ID,mobino)
                        mobin.send_keys("7894566623")
                        button="button#Get\ free\ quotes"
                        buttonquo=self.driver.find_element(By.CSS_SELECTOR,button)
                        buttonquo.click()
                        time.sleep(5)

                        br=By.ID,"#make"
                        brands=wait.until(EC.visibility_of_all_elements_located(br))
                        
                        
                        if brands:
                            time.sleep(4)
                        
                            ra_br=random.choice(brands)
                            ra_br.click()
                        time.sleep(5)
                        
                        
                            
                        vars=By.ID,"#model"
                        varints=wait.until(EC.visibility_of_all_elements_located(vars)) 
                        
                        if varints:
                                ra_vr=random.choice(varints)
                                ra_vr.click()
                                time.sleep(9)
                                log.info("trupass")
    def healthpre(self):
        time.sleep(5)
        log=self.getLogger()
        Ac = ActionChains(self.driver)
        wait = WebDriverWait(self.driver, 20)
        
        prod=By.CSS_SELECTOR,".product-section li"
        product=wait.until(EC.presence_of_all_elements_located(prod))
        
        
        for podu in product:
                    pod=podu.get_attribute("id")
                    if pod=="health": 
                          
                        podu.click()  

                        time.sleep(5)           
                        
                        checkbox=By.CSS_SELECTOR,".PrivateSwitchBase-input css-1m9pwf3"
                        selectcheck=wait.until(EC.presence_of_all_elements_located(checkbox))
                        ra_slcheck=random.choice(selectcheck)
                        value=ra_slcheck.get_attribute("id")
                        
                        if value=="One Adult":
                            
                                
                                
                                
                                rel=By.CSS_SELECTOR,"css-slyssw"
                                relation=wait.until(EC.visibility_of_element_located(rel))
                                
                                relation.click()
                                calander =By.CSS_SELECTOR,".css-1wjkg3"
                                alclander=wait.until(EC.visibility_of_element_located(calander))
                                alclander.click()
                                year_slec=By.CSS_SELECTOR,"css-1p8hrm8"
                                allYear_slec=wait.until(EC.presence_of_all_elements_located(year_slec))
                                sel=random.choice(allYear_slec)
                                sel.click()
                                month_slec=By.CSS_SELECTOR,"css-1cw4hi4"
                                all_monthslec=wait.until(EC.presence_of_all_elements_located(month_slec))
                                mont=random.choice(all_monthslec)
                                for _ in range(3):
                                    mont.click()
                                date_slec=By.CSS_SELECTOR,".css-a78wou"
                                alldate_slec=wait.until(EC.presence_of_all_elements_located(date_slec))
                                date=random.choice(alldate_slec)
                                date.click()
                                gender=By.CSS_SELECTOR,".css-qiwgdb.css-qiwgdb.css-qiwgdb"
                                gendersel=wait.until(EC.presence_of_element_located(gender))
                                gendersel.click()
                                se=By.CSS_SELECTOR,"css-1km1ehz"
                                se_sel=wait.until(EC.presence_of_all_elements_located(se))
                                sel_se=random.choice(se_sel)
                                sel_se.click()
                                continue_btn=By.CSS_SELECTOR,".MuiButton-root"
                                continue_but=wait.until(EC.presence_of_element_located(continue_btn))
                                continue_but.click()

                                 
                                # qutbut=self.driver.find_element(By.CSS_SELECTOR,".primaryBtns .MuiButton-root")
                                # qutbut.click()
                                
                                
                            
                                
                                
                                
                        elif value=="Two Adults" :
                                ra_slcheck.click()
                                time.sleep(5)
                                rel=By.CSS_SELECTOR,"css-slyssw"
                                relation=wait.until(EC.visibility_of_all_elements_located(rel))
                                for rela in relation:
                                      rela.click()
                                      
                                      calander =By.CSS_SELECTOR,".css-1wjkg3"
                                      alclander=wait.until(EC.visibility_of_element_located(calander))
                                      alclander.click()
                                      year_slec=By.CSS_SELECTOR,"css-1p8hrm8"
                                      allYear_slec=wait.until(EC.presence_of_all_elements_located(year_slec))
                                      sel=random.choice(allYear_slec)
                                      sel.click()
                                      month_slec=By.CSS_SELECTOR,"css-1cw4hi4"
                                      all_monthslec=wait.until(EC.presence_of_all_elements_located(month_slec))
                                      mont=random.choice(all_monthslec)
                                      for _ in range(3):
                                        mont.click()
                                      date_slec=By.CSS_SELECTOR,".css-a78wou"
                                      alldate_slec=wait.until(EC.presence_of_all_elements_located(date_slec))
                                      date=random.choice(alldate_slec)
                                      date.click()
                                gender=By.CSS_SELECTOR,".css-qiwgdb.css-qiwgdb.css-qiwgdb"
                                gendersel=wait.until(EC.presence_of_all_elements_located(gender))
                                for gen in gendersel:
                                            gen.click()
                                            se=By.CSS_SELECTOR,"css-1km1ehz"
                                            se_sel=wait.until(EC.presence_of_all_elements_located(se))
                                            sel_se=random.choice(se_sel)
                                            sel_se.click()      
                                continue_btn=By.CSS_SELECTOR,".MuiButton-root"
                                continue_but=wait.until(EC.presence_of_element_located(continue_btn))
                                continue_but.click()        
                                      
                                

                                    
                                            
                        elif value == "Daughter " or value == "Son ":
                                ra_slcheck.click()
                                time.sleep(5)
                                rel=By.CSS_SELECTOR,"css-slyssw"
                                relation=wait.until(EC.visibility_of_all_elements_located(rel))
                                for rela in relation:
                                      rela.click()
                                      
                                      calander =By.CSS_SELECTOR,".css-1wjkg3"
                                      alclander=wait.until(EC.visibility_of_element_located(calander))
                                      alclander.click()
                                      year_slec=By.CSS_SELECTOR,"css-1p8hrm8"
                                      allYear_slec=wait.until(EC.presence_of_all_elements_located(year_slec))
                                      sel=random.choice(allYear_slec)
                                      sel.click()
                                      month_slec=By.CSS_SELECTOR,"css-1cw4hi4"
                                      all_monthslec=wait.until(EC.presence_of_all_elements_located(month_slec))
                                      mont=random.choice(all_monthslec)
                                      for _ in range(3):
                                        mont.click()
                                      date_slec=By.CSS_SELECTOR,".css-a78wou"
                                      alldate_slec=wait.until(EC.presence_of_all_elements_located(date_slec))
                                      date=random.choice(alldate_slec)
                                      date.click()
                                gender=By.CSS_SELECTOR,".css-qiwgdb.css-qiwgdb.css-qiwgdb"
                                gendersel=wait.until(EC.presence_of_element_located(gender))
                                gendersel.click()      
                                continue_btn=By.CSS_SELECTOR,".MuiButton-root"
                                continue_but=wait.until(EC.presence_of_element_located(continue_btn))
                                continue_but.click()
                                 
                            
                            
                        break            
                    else:
                          continue
                        
                           
                    
                                       
                    
                
        log.info("prequote pass")

