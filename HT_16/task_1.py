# Автоматизувати процес замовлення робота за допомогою Selenium
# 1. Отримайте та прочитайте дані з "https://robotsparebinindustries.com/orders.csv". Увага! Файл має бути прочитаний з сервера кожного разу при запускі скрипта, не зберігайте файл локально.
# 2. Зайдіть на сайт "https://robotsparebinindustries.com/"
# 3. Перейдіть у вкладку "Order your robot"
# 4. Для кожного замовлення з файлу реалізуйте наступне:
#     - закрийте pop-up, якщо він з'явився. Підказка: не кожна кнопка його закриває.
#     - оберіть/заповніть відповідні поля для замовлення
#     - натисніть кнопку Preview та збережіть зображення отриманого робота. Увага! Зберігати треба тільки зображення робота, а не всієї сторінки сайту.
#     - натисніть кнопку Order та збережіть номер чеку. Увага! Інколи сервер тупить і видає помилку, але повторне натискання кнопки частіше всього вирішує проблему. Дослідіть цей кейс.
#     - переіменуйте отримане зображення у формат <номер чеку>_robot (напр. 123456_robot.jpg). Покладіть зображення в директорію output (яка має створюватися/очищатися під час запуску скрипта).
#     - замовте наступного робота (шляхом натискання відповідної кнопки)
# ** Додаткове завдання (необов'язково)
#     - окрім збереження номеру чеку отримайте також HTML-код всього чеку
#     - збережіть отриманий код в PDF файл
#     - додайте до цього файлу отримане зображення робота (бажано на одній сторінці, але не принципово)
#     - збережіть отриманий PDF файл у форматі <номер чеку>_robot в директорію output. Окремо зображення робота зберігати не потрібно. Тобто замість зображень у вас будуть pdf файли які містять зображення з чеком.
import os
import shutil
import time

from csv import DictReader
from io import StringIO

import requests
from selenium import webdriver

from pages.home_page import HomePage
from pages.order_page import OrderPage


class OrderAutomation:
    orders_details_url = "https://robotsparebinindustries.com/orders.csv"
    site_url = "https://robotsparebinindustries.com/"
    output_folder = 'output'

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.home_page = HomePage(self.driver)
        self.order_page = OrderPage(self.driver, self.output_folder)

    def prepare_output_folder(self):
        if os.path.exists(self.output_folder):
            shutil.rmtree(self.output_folder)
        os.mkdir(self.output_folder)

    def rename_image(self, id):
        os.rename(f'{self.output_folder}/temp.png', f'{self.output_folder}/{id}_robot.png')

    def get_orders_info_reader(self):
        r = requests.get(self.orders_details_url)
        csv_file = StringIO(r.text)
        headers = ["order_number", "head", "body", "legs", "address"]
        reader = DictReader(f=csv_file, fieldnames=headers)
        return reader

    def open_order_page(self):
        self.driver.get('https://robotsparebinindustries.com/')
        self.home_page.open_order_page()
        self.order_page.check_modal()

    def create_orders(self):
        try:
            self.open_order_page()
            orders_info = self.get_orders_info_reader()
            next(orders_info)
            self.prepare_output_folder()

            for order in orders_info:
                self.order_page.select_head_parameter(order['head'])
                self.order_page.select_body_parameter(order['body'])
                self.order_page.enter_legs_quantity(order['legs'])
                self.order_page.enter_address(order['address'])
                self.order_page.click_preview_button()
                self.order_page.save_robot_image()
                self.order_page.click_order_button()
                order_id = self.order_page.get_order_id()
                self.rename_image(order_id)
                self.order_page.order_another()
                time.sleep(5)
        except Exception:
            self.driver.close()
            
        self.driver.close()


automation_script = OrderAutomation()
automation_script.create_orders()
