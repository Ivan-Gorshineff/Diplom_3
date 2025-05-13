from allure import title

from data import Urls
from locators.main_page_locators import MainPageLocators
from pages.constructor_page import ConstructorPage
from pages.feed_page import FeedPage
from conftest import get_browser, login_new_user, create_new_user_by_api


class TestConstructorPage:

    @title('Проверяем переход по клику на «Конструктор»')
    def test_open_constructor_by_link(self, get_browser):
        driver = get_browser
        feed_page = FeedPage(driver)
        feed_page.open_feed_page()
        feed_page.click_constructor_link()
        constructor_page = ConstructorPage(driver)
        constructor_page.wait_for_load_element(MainPageLocators.LOGIN_BUTTON)
        # Проверяем что текущий url это url Главной страницы
        assert constructor_page.wait_for_constructor_is_active()
        assert constructor_page.get_current_url() == f'{Urls.MAIN_PAGE_URL}/'

    @title('Проверяем переход по клику на «Лента заказов»')
    def test_open_feed_by_link(self, get_browser):
        driver = get_browser
        constructor_page = ConstructorPage(driver)
        constructor_page.open_constructor_page()
        constructor_page.click_feed_link()
        feed_page = FeedPage(driver)
        feed_page.wait_for_load_element(MainPageLocators.TOTAL_TODAY)
        # Проверяем что текущий url это url Ленты заказов
        assert feed_page.feed_is_active()
        assert feed_page.get_current_url() == Urls.FEED_PAGE_URL

    @title('Проверяем, что если кликнуть на ингредиент, появится всплывающее окно с деталями')
    def test_click_ingredient(self, get_browser):
        driver = get_browser
        constructor_page = ConstructorPage(driver)
        constructor_page.open_constructor_page()
        constructor_page.click_ingredient_link()
        constructor_page.ingredient_details_is_opened()
        # Проверяем что появился заголовок Детали ингредиента
        assert constructor_page.details_title_is_visible()

    @title('Проверяем, что всплывающее окно закрывается кликом по крестику')
    def test_close_ingredient_details(self, get_browser):
        driver = get_browser
        constructor_page = ConstructorPage(driver)
        constructor_page.open_constructor_page()
        constructor_page.click_ingredient_link()
        element = constructor_page.ingredient_details_is_opened()
        constructor_page.click_details_close_link()
        constructor_page.ingredient_details_is_closed()
        # проверяем что модальное окно с деталями заказа закрылось
        assert element.get_attribute('class') == MainPageLocators.DETAILS_LINK_CLASS

    @title(
        'Проверяем, что при добавлении ингредиента в заказ счётчик этого ингридиента увеличивается')
    def test_append_ingredient_in_order(self, get_browser):
        driver = get_browser
        constructor_page = ConstructorPage(driver)
        constructor_page.open_constructor_page()
        counter_before = constructor_page.get_buns_counter()
        constructor_page.drag_and_drop_bun()
        counter_after = constructor_page.get_buns_counter()
        # Проверяем, что счетчик ингредиента увеличивается
        assert counter_after > counter_before

    @title('Проверяем, что залогиненный пользователь может оформить заказ')
    def test_checkout_order_by_user(self, get_browser, create_new_user_by_api,login_new_user):
        driver = login_new_user
        constructor_page = ConstructorPage(driver)
        constructor_page._create_order()
        # проверяем, что появилось модальное окно с деталями заказа
        assert constructor_page.order_details_is_visible()