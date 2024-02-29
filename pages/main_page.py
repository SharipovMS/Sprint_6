import allure

from locators.locators_main_page import LocatorsMainPage
from pages.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    @allure.step('Нажать кнопку принять куки')
    def click_button_cookie(self):
        self.click_button(LocatorsMainPage.cookie_button)

    @allure.step('Нажать на кнопку Самокаты')
    def click_button_scooter(self):
        self.click_button(LocatorsMainPage.logo_link_scooter)

    @allure.step('Нажать на кнопку Яндекс')
    def click_button_yandex(self):
        self.click_button(LocatorsMainPage.logo_link_yandex)

    @allure.step('Нажать на кнопку заказать верхняя')
    def click_button_order_top(self):
        self.click_button(LocatorsMainPage.order_button_main)

    @allure.step('Нажать на кнопку заказать нижняя')
    def click_button_order_low(self):
        self.click_button(LocatorsMainPage.order_button_low)

    @allure.step('Прокручиваем страницу до вопросов')
    def scrolling_method(self):
        self.scroll_to_element(LocatorsMainPage.QUESTION_8)
