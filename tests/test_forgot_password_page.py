from allure import title

from data import Urls, UserData
from locators.forgot_password_locators import ForgotPasswordPageLocators
from pages.login_page import LoginPage
from pages.forgot_password_page import ForgotPage
from pages.reset_password_page import ResetPasswordPage
from conftest import get_browser


class TestForgotPage:

    @title('Проверяем переход на страницу восстановления пароля по ссылке «Восстановить пароль»')
    def test_forgot_password_button(self, get_browser):
        driver = get_browser
        login_page = LoginPage(driver)
        login_page.open_login_page()
        login_page.scroll_to_click_forgot_password_link()
        login_page.wait_for_load_element(ForgotPasswordPageLocators.RECOVER_BUTTON)
        # Проверяем что текущий url это url страницы восстановления пароля
        assert login_page.get_current_url() == Urls.FORGOT_PASSWORD_PAGE_URL

    @title('Проверяeм ввод почты и клик по кнопке «Восстановить»')
    def test_recover_password_button(self, get_browser):
        driver = get_browser
        forgot_password_page = ForgotPage(driver)
        forgot_password_page.open_and_enter_forgot_password(UserData.USER_EMAIL)
        # Проверяем что текущий url это url страницы сброса пароля
        assert forgot_password_page.get_current_url() == Urls.RESET_PASSWORD_PAGE_URL

    @title('Проверяем что клик по кнопке показать/скрыть пароль делает поле активным')
    def test_click_eye_button(self, get_browser):
        driver = get_browser
        forgot_password_page = ForgotPage(driver)
        forgot_password_page.open_and_enter_forgot_password(UserData.USER_EMAIL)
        reset_password_page = ResetPasswordPage(driver)
        reset_password_page.click_eye_icon()
        # Проверяем, что поле "email" становится активным
        assert reset_password_page.check_password_field_focused()