import random
from helpers import *
import allure
from locators.locators_order_page import LocatorsOrderPage
from pages.base_page import BasePage

class OrderPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    @allure.step('Заполняю форму оформления заказа персональные данные.')
    def fill_form_one(self):
        self.find(LocatorsOrderPage.metro).click()
        self.find(LocatorsOrderPage.contaner_metro)
        input_metro_option = self.find_elements(LocatorsOrderPage.meto_text)
        input_metro_random = random.choice(input_metro_option)
        selected_option_text = input_metro_random.text
        input_metro_random.click()

        input_name = self.find(LocatorsOrderPage.name)
        input_name.click()
        input_name.send_keys(name())

        input_second_name = self.find(LocatorsOrderPage.second_name)
        input_second_name.click()
        input_second_name.send_keys(second_name())

        input_address = self.find(LocatorsOrderPage.address)
        input_address.click()
        input_address.send_keys(address())

        input_phone = self.find(LocatorsOrderPage.phone_number)
        input_phone.click()
        input_phone.send_keys(phone_number())

    @allure.step('Заполняю форму c подробностями аренды')
    def fill_form_two(self):
        date = self.find(LocatorsOrderPage.date)
        date.click()
        input_date = self.find(LocatorsOrderPage.date_input)
        input_date.click()

        period = self.find(LocatorsOrderPage.period)
        period.click()

        period_choice = self.find(LocatorsOrderPage.period_input)
        period_choice.click()

        color = self.find(LocatorsOrderPage.color_grey)
        color.click

        commments = self.find(LocatorsOrderPage.comment_for_delivery)
        commments.click()
        commments.send_keys('Осторожно злая собака')

        self.click_button(LocatorsOrderPage.button_order)
        self.click_button(LocatorsOrderPage.button_yep_order)
