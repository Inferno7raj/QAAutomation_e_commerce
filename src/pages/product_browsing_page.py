from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
from config import *
import time

class ProductBrowsing:   
    
    next_button_on_home_page = (By.XPATH,"//button[text()='Next']")    
    previous_button_on_home_page = (By.XPATH,"//button[text()='Previous']")
    apple_monitor = (By.XPATH,"//a[text()='Apple monitor 24']")
    home_page_button = (By.XPATH,"//a[text()='Home ']")
    
    switch_to_phone_categories = (By.XPATH,"//a[text()='Phones']")
    switch_to_laptop_categories = (By.XPATH,"//a[text()='Laptops']")
    switch_to_monitors_categories = (By.XPATH,"//a[text()='Monitors']")
    
    select_categories = (By.XPATH,"//a[text()='CATEGORIES']")
    macbook_pro = (By.XPATH,"//a[text()='MacBook Pro']")
    add_to_cart = (By.XPATH,"//a[text()='Add to cart']")
    last_product_on_home_page = (By.XPATH,"//form[@id='frm']/preceding::div[@class='card h-100']//a[@href='prod.html?idp_=9']/ancestor::div[@class='card h-100']")       
    
    product_name_added_to_cart = (By.XPATH,"//div[@id='tbodyid']//descendant::h2")
    
    
    
    def __init__(self, driver):
        self.driver = driver
        
    def product_browsing(self):
        
        wait = WebDriverWait(self.driver, 30)
               
        scroll_down_element = self.driver.find_element(By.XPATH," //a[text()='Monitors']")
        self.driver.execute_script("arguments[0].scrollIntoView(true)", scroll_down_element)    
        actions = ActionChains(self.driver) 
        actions.move_to_element(scroll_down_element).perform()
        
        wait.until(expected_conditions.visibility_of_element_located(self.next_button_on_home_page))
        self.driver.find_element(*self.next_button_on_home_page).click()
        
        wait.until(expected_conditions.visibility_of_element_located(self.previous_button_on_home_page))
        self.driver.find_element(*self.previous_button_on_home_page).click()
        time.sleep(2)
        
        wait.until(expected_conditions.visibility_of_element_located(self.apple_monitor))
        self.driver.find_element(*self.apple_monitor).click()
        time.sleep(2)
              
        wait.until(expected_conditions.visibility_of_element_located(self.home_page_button))
        self.driver.find_element(*self.home_page_button).click()                
        
        wait.until(expected_conditions.visibility_of_element_located(self.switch_to_phone_categories))
        self.driver.find_element(*self.switch_to_phone_categories).click()
        
        wait.until(expected_conditions.visibility_of_element_located(self.switch_to_laptop_categories))
        self.driver.find_element(*self.switch_to_laptop_categories).click()
        
        wait.until(expected_conditions.visibility_of_element_located(self.switch_to_monitors_categories))
        self.driver.find_element(*self.switch_to_monitors_categories).click()
        time.sleep(2)
        
    def adding_products_to_cart(self):
        
        wait = WebDriverWait(self.driver, 30)        
        
        wait.until(expected_conditions.visibility_of_element_located(self.select_categories))
        self.driver.find_element(*self.select_categories).click()
        
        wait.until(expected_conditions.visibility_of_element_located(self.next_button_on_home_page))
        self.driver.find_element(*self.next_button_on_home_page).click() 
        time.sleep(2)       
        
        wait.until(expected_conditions.visibility_of_element_located(self.last_product_on_home_page))
        self.driver.find_element(*self.last_product_on_home_page).click()
        
        wait.until(expected_conditions.visibility_of_element_located(self.add_to_cart))
        self.driver.find_element(*self.add_to_cart).click()
        time.sleep(3)
        
        alert = self.driver.switch_to.alert
        alert_text = alert.text
        alert.accept()                                              
        
        wait.until(expected_conditions.visibility_of_element_located(self.product_name_added_to_cart))
        product_name = self.driver.find_element(*self.product_name_added_to_cart).text
        
        if(alert_text == 'Product added.'):
            logging.info(f"Selected product - {product_name} is successfully added to the cart")
        
        else:
            logging.info(f"Selected product - {product_name} is not added to the cart")   
        
        return product_name
        
        
        