from selenium import webdriver
from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def open_order_page(self):
        self.driver.find_element(By.CSS_SELECTOR, 'a[href="#/robot-order"]').click()