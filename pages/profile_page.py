from allure import step

from locators.proflle_page_locators import ProfilePageLocators
from pages.base_page import BasePage
from pages.constructor_page import ConstructorPage


class ProfilePage(BasePage):

    step('Открываем Личный кабинет по ссылке на Главной странице')
    def open_profile_page(self):
        constructor_page = ConstructorPage(self.driver)
        constructor_page.click_and_open_profile_by_link()

    @step('кликаем ссылку "История заказов"')
    def click_order_history_link(self):
        self.click_element_by_locator(ProfilePageLocators.ORDER_HISTORY_LINK)

    @step('Проверяем, что раздел История заказов становится активным')
    def order_history_is_active(self):
        return self.wait_for_text_in_class_name(ProfilePageLocators.ORDER_HISTORY_LINK,
                                                ProfilePageLocators.ORDER_HISTORY_IS_ACTIVE)

    @step('кликаем кнопку "Выход"')
    def click_exit_button(self):
        self.click_element_by_locator_when_clickable(ProfilePageLocators.EXIT_BUTTON)

    # вспомогательные функции для других тестов
    @step('Получаем список элементов страницы с номерами заказов')
    def __get_order_history_elements(self):
        return self.wait_for_load_all_elements(ProfilePageLocators.ORDER_HISTORY_ORDER_NUMBER)

    @step('Получаем элемент страницы с номером заказа')
    def __get_order_history_element(self):
        return self.wait_for_load_element(ProfilePageLocators.ORDER_HISTORY_ORDER_NUMBER)

    @step('Получаем список номеров заказов пользователя')
    def get_order_history_link(self):
        self.open_profile_page()
        self.click_order_history_link()
        elements = self.__get_order_history_elements()
        order_list = [item.text for item in elements]
        return order_list

    @step('Получаем номер последнего заказа пользователя')
    def get_number_from_order_history(self):
        self.open_profile_page()
        self.click_order_history_link()
        element = self.__get_order_history_element()
        number = element.text
        return number
