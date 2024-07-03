from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
from config import *
import time

class CartCheckout:   
    
    cart_icon = (By.XPATH,"//a[text()='Cart']")
    
    def __init__(self,driver):
        self.driver = driver
    
    def checkout_process(self, product_name):
        
        wait = WebDriverWait(self.driver, 30)
    
        wait.until(expected_conditions.visibility_of_element_located(self.cart_icon))
        self.driver.find_element(*self.cart_icon).click()
          
       
        
        

