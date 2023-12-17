import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class OrderPage:
    def __init__(self, driver: webdriver.Chrome, output_folder):
        self.driver = driver
        self.output_folder = output_folder
    
    def check_modal(self):
       modal = self.driver.find_element(By.CLASS_NAME, 'modal')
       if modal.is_displayed():
          self.driver.find_element(By.CLASS_NAME, 'btn-danger').click()
        
    def select_head_parameter(self, option_number):
        drop_down_element = self.driver.find_element(By.ID, 'head')
        select = Select(drop_down_element)
        select.select_by_value(option_number)

    def select_body_parameter(self, option_number):
        self.driver.find_element(By.CSS_SELECTOR, f'#id-body-{option_number}').click()

    def enter_legs_quantity(self, quantity):
        legs_input = self.driver.find_element(By.CSS_SELECTOR, ".form-control[type='number']")
        legs_input.send_keys(quantity)

    def enter_address(self, address):
        address_input = self.driver.find_element(By.ID, 'address')
        address_input.send_keys(address)
    
    def click_preview_button(self):
        self.driver.execute_script("window.scrollBy(0, 200)")
        time.sleep(4)
        button = self.driver.find_element(By.ID, 'preview')
        button.click()

    def click_order_button(self):
        button = self.driver.find_element(By.ID, 'order')
        while True:
            button.click()
            try:
                self.driver.find_element(By.CLASS_NAME, 'alert-danger')
            except Exception:
                break

    def save_robot_image(self):
        image = self.driver.find_element(By.ID, 'robot-preview-image')
        self.driver.execute_script("window.scrollBy(0, 1000)")
        time.sleep(4)
        screenshot = image.screenshot_as_png

        with open('output/temp.png', 'wb') as f:
            f.write(screenshot)

    def get_order_id(self):
        return self.driver.find_element(By.CLASS_NAME, 'badge-success').text

    def order_another(self):
        button = self.driver.find_element(By.ID, 'order-another')
        button.click()
        self.check_modal()
