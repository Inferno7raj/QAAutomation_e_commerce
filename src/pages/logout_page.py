from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


class LogoutPage:

    log_out_icon = (By.XPATH,"//a[text()='Log out']")
    
    
    def __init__(self, driver):
	    self.driver = driver
