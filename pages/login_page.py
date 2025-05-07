from allure import step

from data import Urls
from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):

    @step('Открываем страницу авторизации')
    def open_login_page(self):
        self.open_page(Urls.LOGIN_PAGE_URL)
        self.wait_for_load_element(LoginPageLocators.LOGIN_BUTTON)

    @step('Ждем загрузку страницы авторизации')
    def wait_open_login_page(self):
        self.wait_for_load_element(LoginPageLocators.LOGIN_BUTTON)

    @step('Вводим email и пароль')
    def enter_user_data(self, email, password):
        self.wait_for_load_element(LoginPageLocators.EMAIL_FIELD)
        self.click_element_by_locator_when_clickable(LoginPageLocators.EMAIL_FIELD)
        self.set_value(LoginPageLocators.EMAIL_FIELD, email)
        self.click_element_by_locator_when_clickable(LoginPageLocators.PASSWORD_FIELD)
        self.set_value(LoginPageLocators.PASSWORD_FIELD, password)

    @step('кликаем кнопку "Войти"')
    def click_login_button(self):
        self.click_element_by_locator_when_clickable(LoginPageLocators.LOGIN_BUTTON)

    @step('Прокручиваем страницу и кликаем ссылку "Восстановить пароль"')
    def scroll_to_click_forgot_password_link(self):
        self.scroll_to_element_by_locator(LoginPageLocators.LOGIN_BUTTON)
        self.click_element_by_locator(LoginPageLocators.FORGOT_PAGE_LINK)