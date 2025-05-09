from allure import step

from data import Urls
from locators.constructor_page_locators import ConstructorPageLocators
from pages.base_page import BasePage


class ConstructorPage(BasePage):

    @step('Открываем Главную страницу по url')
    def open_constructor_page(self):
        self.open_page(Urls.MAIN_PAGE_URL)
        self.wait_for_load_element(ConstructorPageLocators.ANY_BUTTON)

    @step('Кликаем ссылку "Лента заказов"')
    def click_feed_link(self):
        self.click_element_by_locator(ConstructorPageLocators.FEED_LINK)

    @step('Ждем, что раздел Конструктор становится активным')
    def wait_for_constructor_is_active(self):
        return self.wait_for_text_in_class_name(ConstructorPageLocators.CONSTRUCTOR_LINK,
                                                ConstructorPageLocators.ACTIVE_TEXT)

    @step('Кликаем ссылку "Личный кабинет"')
    def click_profile_link(self):
        self.click_element_by_locator(ConstructorPageLocators.PROFILE_LINK)

    @step('Открываем Личный кабинет по ссылке на Главной странице')
    def click_and_open_profile_by_link(self):
        self.open_constructor_page()
        self.wait_for_load_element(ConstructorPageLocators.ORDER_BUTTON)
        # кликаем Личный кабинет в хедере
        self.click_profile_link()
        # ждем перехода в Личный кабинет и появления кнопки "Сохранить"
        self.wait_for_load_element(ConstructorPageLocators.SAVE_BUTTON)

    @step('Кликаем на 1-й ингредиент')
    def click_ingredient_link(self):
        self.click_element_by_locator(ConstructorPageLocators.INGREDIENT_LINK)

    @step('Проверяем, что открывается карточка деталей')
    def ingredient_details_is_opened(self):
        return self.wait_for_load_element(ConstructorPageLocators.DETAILS_OPENED_LINK)

    @step('Проверяем, что появился заголовок Детали ингредиента')
    def details_title_is_visible(self):
        return self.wait_for_load_element(ConstructorPageLocators.DETAILS_TITLE_LINK)

    @step('Кликаем на крестик')
    def click_details_close_link(self):
        self.click_element_by_locator(ConstructorPageLocators.DETAILS_CLOSE_LINK)

    @step('Проверяем что заголовок Детали ингредиента скрыт')
    def ingredient_details_is_closed(self):
        self.wait_for_invisibility_of_element(ConstructorPageLocators.DETAILS_TITLE_LINK)

    @step('Добавляем булку в заказ')
    def drag_and_drop_bun(self):
        source = self.wait_for_load_element(ConstructorPageLocators.INGREDIENT_LINK)
        target = self.wait_for_load_element(ConstructorPageLocators.DRAGNDROP_BUN_TARGET)
        self.drag_and_drop(source, target)

    @step('Получаем счетчик булок')
    def get_buns_counter(self):
        counter = self.get_text(ConstructorPageLocators.INGREDIENT_COUNTER_LINK)
        counter = int(counter)
        return counter

    @step('Прокручиваем страницу к соусу')
    def scroll_to_sauce(self):
        sauce_element = self.scroll_to_element_by_locator(ConstructorPageLocators.INGREDIENT_3_LINK)
        return sauce_element

    @step('Прокручиваем страницу к начинке')
    def scroll_to_filling(self):
        filling_element = self.scroll_to_element_by_locator(ConstructorPageLocators.INGREDIENT_7_LINK)
        return filling_element

    @step('Добавляем соус в заказ')
    def drag_and_drop_sauce(self):
        self.scroll_to_sauce()
        source = self.wait_for_load_element(ConstructorPageLocators.INGREDIENT_3_LINK)
        target = self.wait_for_load_element(ConstructorPageLocators.DRAGNDROP_BURGER_TARGET)
        self.drag_and_drop(source, target)

    @step('Добавляем начинку в заказ')
    def drag_and_drop_filling(self):
        self.scroll_to_filling()
        source = self.wait_for_load_element(ConstructorPageLocators.INGREDIENT_7_LINK)
        target = self.wait_for_load_element(ConstructorPageLocators.DRAGNDROP_BURGER_TARGET)
        self.drag_and_drop(source, target)

    @step('Кликаем кнопку Оформить заказ')
    def click_order_button(self):
        self.click_element_by_locator_when_clickable(ConstructorPageLocators.ORDER_BUTTON)

    @step('Ждем, что появилось окно с деталями заказа')
    def order_details_is_visible(self):
        return self.wait_for_load_element(ConstructorPageLocators.ORDER_MODAL_ORDER_NUMBER)

    @step('Получаем номер заказа')
    def get_number_order(self):
        return self.wait_for_load_element(ConstructorPageLocators.ORDER_MODAL_ORDER_NUMBER).text

    @step('Формируем заказ и кликаем кнопку "Оформить заказ"')
    def _create_order(self):
        self.open_constructor_page()
        self.drag_and_drop_bun()
        self.drag_and_drop_sauce()
        self.drag_and_drop_filling()
        self.click_order_button()

    # вспомогательная функция для других тестов
    @step('Создаем заказ и получаем его номер')
    def create_order(self):
        self._create_order()
        self.order_details_is_visible()
        number = self.get_number_order()
        self.click_element_by_locator(ConstructorPageLocators.ORDER_CLOSE_BUTTON)
        return str(number)