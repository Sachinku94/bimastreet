

# from Pages import homepagejio
# from Smoke_tests.utilities.base_class import BaseClass
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from tests.test_data import test_newdata 
# from tests.test_data import test_alldata
# import time
# import random
# import logging
# from Smoke_tests.object.Selenium_helper import SeleniumHelper

# class QuotePage(BaseClass):

#     def __init__(self, driver):
#         self.driver = driver
#         self.wait = WebDriverWait(self.driver, 20)
#         self.ac = ActionChains(self.driver)
#         self.log = self.getLogger()

#     def healthpre(self):
#         try:
#             products = self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".product-section li")))

#             for product in products:
#                 if product.get_attribute("id") == "health":
#                     product.click()

#                     checkboxes = self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "input.PrivateSwitchBase-input.css-1m9pwf3")))
#                     selected_checkbox = random.choice(checkboxes)
#                     value = selected_checkbox.get_attribute("id").strip()
#                     self.log.info(value)

#                     selected_checkbox.click()
#                     time.sleep(5)  # Delay to prevent stale element
#                     self._fill_health_form(value)
#                     break

#             self.log.info("Health prequote passed")

#         except Exception as e:
#             self.log.error(f"Health quote failed: {e}")
#             self.log.info(f"Current URL: {self.driver.current_url}")

#     def _fill_health_form(self, value):
#         def select_date():
#             self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".MuiButtonBase-root.MuiIconButton-root.MuiIconButton-sizeSmall.MuiPickersCalendarHeader-switchViewButton.css-1wjkg3"))).click()
#             random.choice(self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".MuiPickersYear-root.css-1p8hrm8")))).click()
#             try:
#                 for _ in range(3):
#                     random.choice(self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.MuiPickersArrowSwitcher-root.css-k008qs button")))).click()
#                     time.sleep(3)  # Delay to prevent stale element
#             except Exception:
#                 pass
#             random.choice(self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".css-a78wou")))).click()

#         def select_gender():

#             gender=self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".css-qiwgdb.css-qiwgdb.css-qiwgdb")))
#             for gen in gender:
#                 gen.click()

#                 random.choice(self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".MuiButtonBase-root.MuiMenuItem-root.MuiMenuItem-gutters.MuiMenuItem-root.MuiMenuItem-gutters.css-1km1ehz")))).click()

#         relations = self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "button.MuiButtonBase-root.MuiIconButton-root.MuiIconButton-edgeEnd.MuiIconButton-sizeMedium.css-slyssw")))

#         for rel in relations:
#             rel.click()
#             time.sleep(3)  # Delay to prevent stale element
#             select_date()

#         time.sleep(2)  # Delay to prevent stale element
#         select_gender()

#         self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".MuiButton-root"))).click()
#         personal_detail=By.CSS_SELECTOR,".evInputField .MuiInputBase-root .MuiInputBase-input"
#         per_det=self.wait.until(EC.presence_of_all_elements_located(personal_detail))
#         field_order = ["mobile", "pincode"]  # Ensure this matches how fields appear in the DOM
#         Personal_Details=test_alldata.Personal_Details
# # Loop through the fields and send a random value
#         for i, key in enumerate(field_order):
#             element = per_det[i]
#             value_to_send = random.choice(Personal_Details[key])
#             element.clear()
#             element.send_keys(value_to_send)
#         self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".MuiButton-root"))).click() 
#         time.sleep(10)
#         qotepageurl=self.driver.current_url
        
#         Save_file=SeleniumHelper.save_to_test_data
#         Save_file(qotepageurl)
#         assert "quote_no"   in  qotepageurl
#         self.log.info(qotepageurl)

#         time.sleep(10)

#     def healthpost(self):
#         helthqoteurl=test_newdata.Health_post
#         for hel in helthqoteurl:
#          self.driver.get(hel)
#         time.sleep(10)
#         del_record=SeleniumHelper.del_to_tests_data
#         del_record()





from Smoke_tests.utilities.base_class import BaseClass
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.test_data import test_newdata 
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

            gender=self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".css-qiwgdb.css-qiwgdb.css-qiwgdb")))
            for gen in gender:
                gen.click()

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
        
        try:
            helthqoteurl=test_newdata.Health_post
            for hel in helthqoteurl:
                logolist=[]
                premlist=[]
                self.driver.get(hel)
                time.sleep(10)
                insurer_logo=By.CSS_SELECTOR,"img.insurerLogo"
                srcinsurer_log=self.wait.until(EC.presence_of_all_elements_located(insurer_logo))
                for insurer in srcinsurer_log:
                    logo=insurer.get_attribute("src")
                    logolist.append(logo)
                    self.log.info('done')
                prem=By.CSS_SELECTOR,"p.premium span"
                prem_all=self.wait.until(EC.presence_of_all_elements_located(prem))
                for premi in prem_all:
                   premitext= premi.text
                   premlist.append(premitext)

                buy_policy=By.CSS_SELECTOR,"button#buy_policy"
                policy=self.wait.until(EC.presence_of_all_elements_located(buy_policy))
                policy_choice=random.choice(policy)
                policy_choice.click()
                indexvalue=policy.index(policy_choice)
                
                time.sleep(10)
                insurer_logoekyc=By.CSS_SELECTOR,"img.insurerLogo"
                srcinsurer_log=self.wait.until(EC.presence_of_element_located(insurer_logoekyc))
                srcinsurer_logekyc=srcinsurer_log.get_attribute("src")
                self.log.info('donekyc')
                premkyc=By.CSS_SELECTOR,"h5.premium"
                premkycfinal=self.wait.until(EC.presence_of_element_located(premkyc)).text


                
                assert logolist[indexvalue] == srcinsurer_logekyc
                assert premlist[indexvalue] == premkycfinal
                    
                del_record=SeleniumHelper.del_to_tests_data
                del_record()
        except Exception as e:
            self.log.error(f"Health post quote failed: {e}")
            self.log.info(f"Current URL: {self.driver.current_url}")


