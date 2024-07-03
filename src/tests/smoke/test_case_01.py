from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from config import *
from pages.login_page import LoginPage
from pages.product_browsing_page import ProductBrowsing
from pages.product_cart import CartCheckout
from pages.sign_up_page import Signup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import allure
from allure_commons.types import AttachmentType
import pytest
import json

class Test_case_01:

    @pytest.mark.usefixtures("setup_teardown")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_case_01(self):

        extend_testing = (By.XPATH,"")

        # reading the data here, from test_case_01.json
        with open(TEST_DATA_DIR + '/test_case_01.json', 'r') as json_file:
            test_data = json.load(json_file)
            customer_unit = test_data['customer_unit']
            
        wait = WebDriverWait(self.driver, 30)
     
        product_browse  = ProductBrowsing(self.driver) 
        product_cart_validate = CartCheckout(self.driver)      
        
        product_browse.product_browsing()
        
        product_name = product_browse.adding_products_to_cart()
        
        product_cart_validate.checkout_process(product_name)


