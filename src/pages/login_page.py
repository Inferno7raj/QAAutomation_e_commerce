from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


class LoginPage:

    login_icon = (By.XPATH,"//a[text() = 'Log in']")
    username_input_field = (By.XPATH,"//input[@id='loginusername']")
    password_input_field = (By.XPATH,"//input[@id='loginpassword']")
    login_button = (By.XPATH,"//button[text()='Log in']")
    validate_username = (By.XPATH,"//a[@id='nameofuser']")
    
    def __init__(self, driver):
	    self.driver = driver
