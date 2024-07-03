from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from config import *

class Signup:
    
    signup_icon = (By.XPATH,"//a[text()='Sign up']")
    username_input_field_on_signup_page = (By.XPATH,"//input[@id='sign-username']")
    password_input_field_on_signup_page = (By.XPATH,"//input[@id='sign-password']")
    signup_button = (By.XPATH,"//button[text()='Sign up']")
    close_button = (By.XPATH,"//button[text()='Sign up']/preceding-sibling::button")
    
    def __init__(self, driver):
        
        self.driver = driver
        
    
        