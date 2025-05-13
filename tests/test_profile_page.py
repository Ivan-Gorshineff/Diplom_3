from allure import step, title

from data import Urls
from locators.login_page_locators import LoginPageLocators
from pages.constructor_page import ConstructorPage
from pages.profile_page import ProfilePage
from conftest import create_new_user_by_api, login_new_user, get_browser


class TestProfilePage:

    @step('Открываем Личный кабинет по ссылке на Главной странице')
    def __open_profile_page(self, driver):
        constructor_page = ConstructorPage(driver)
        constructor_page.click_and_open_profile_by_link()

    @title('Проверяем переход по клику на «Личный кабинет»')
    def test_profile_link(self, get_browser, create_new_user_by_api, login_new_user):
        driver = login_new_user
        profile_page = ProfilePage(driver)
        profile_page.open_profile_page()
        # Проверяем что текущий url это url Личного кабинета
        assert  driver.current_url == Urls.PROFILE_PAGE_URL

    @title('Проверяем переход в раздел «История заказов»')
    def test_order_history_link(self, get_browser, create_new_user_by_api, login_new_user):
        driver = login_new_user
        profile_page = ProfilePage(driver)
        profile_page.open_profile_page()
        profile_page.click_order_history_link()
        # Проверяем что раздел Истории заказов стал активным и текущий url это url Истории заказов
        assert profile_page.order_history_is_active()
        assert profile_page.get_current_url() == Urls.ORDER_HISTORY_URL

    @title('Проверяем выход из аккаунта')
    def test_exir_button(self, get_browser, create_new_user_by_api, login_new_user):
        driver = login_new_user
        profile_page = ProfilePage(driver)
        profile_page.open_profile_page()
        profile_page.click_exit_button()
        profile_page.wait_for_load_element(LoginPageLocators.LOGIN_BUTTON)
        # Проверяем что текущий url это url страницы авторизации
        assert profile_page.get_current_url() == Urls.LOGIN_PAGE_URL

