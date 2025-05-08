from allure import step

from data import Urls
from locators.reset_password_page_locators import ResetPasswordPageLocators
from pages.base_page import BasePage


class ResetPasswordPage(BasePage):

    @step('Открываем страницу сброса пароля')
    def open_reset_password_page(self):
        return self.open_page(Urls.RESET_PASSWORD_PAGE_URL)

    @step('Кликаем по значку глаза - показать/скрыть пароль')
    def click_eye_icon(self):
        return self.click_element_by_locator(ResetPasswordPageLocators.EYE_ICON)

    @step('Проверяем, что поле "пароль" становится активным')
    def check_password_field_focused(self):
        self.wait_for_text_in_class_name(ResetPasswordPageLocators.FOCUSED_FIELD, ResetPasswordPageLocators.FOCUSED_TEXT)