import allure
from data import Site
from pages.main_page import MainPage

class TestLogo:
    @allure.title('Переход на страницу ДЗЕН по лого Яндекса')
    @allure.description('тест на проверку перехода по логотипу яндекса')
    def test_logo_yandex(self, browser):
        main_page = MainPage(browser)
        main_page.click_button_cookie()
        main_page.click_button_yandex()
        main_page.switch_to_window()
        main_page.wait_for_site(Site.dzen)
        assert main_page.current_get_url() == Site.dzen

    @allure.title('Переход по клику на лого Самокат')
    @allure.description('тест на проверку перехода по логотипу Самокат')
    def test_logo_scooter(self, browser):
        main_page = MainPage(browser)
        main_page.click_button_cookie()
        main_page.click_button_order_top()
        main_page.click_button_scooter()
        main_page.wait_for_site(Site.scooter)
        assert main_page.current_get_url() == Site.scooter
