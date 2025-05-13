from allure import step

from data import Urls
from locators.forgot_password_locators import ForgotPasswordPageLocators
from locators.reset_password_page_locators import ResetPasswordPageLocators
from pages.base_page import BasePage


class ForgotPage(BasePage):

    @step('Открываем страницу восстановления пароля')
    def open_forgot_page(self):
        self.open_page(Urls.FORGOT_PASSWORD_PAGE_URL)

    @step('Ждем загрузку и кликаем ссылку "Восстановить пароль"')
    def scroll_to_click_email_field(self):
        self.wait_for_load_element(ForgotPasswordPageLocators.EMAIL_FIELD)
        self.scroll_to_element_by_locator(ForgotPasswordPageLocators.RECOVER_BUTTON)
        self.click_element_by_locator_when_clickable(ForgotPasswordPageLocators.EMAIL_FIELD)

    @step('Открываем страницу восстановления пароля, вводим почту и кликаем кнопку "Восстановить"')
    def open_and_enter_forgot_password(self, email):
        self.open_forgot_page()
        self.wait_for_load_element(ForgotPasswordPageLocators.RECOVER_BUTTON)
        self.scroll_to_click_email_field()
        self.set_value(ForgotPasswordPageLocators.EMAIL_FIELD, email)
        self.click_element_by_locator_when_clickable(ForgotPasswordPageLocators.RECOVER_BUTTON)
        self.wait_for_load_element(ResetPasswordPageLocators.SAVE_BUTTON)