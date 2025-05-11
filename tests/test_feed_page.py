from allure import title

from pages.constructor_page import ConstructorPage
from pages.feed_page import FeedPage
from pages.profile_page import ProfilePage
from conftest import (create_new_user_by_api,
                      create_order, login_new_user, get_browser)


class TestFeedPage:

    @title('Проверяем что если кликнуть на заказ, откроется всплывающее окно с деталями')
    def test_click_order(self,get_browser, create_order, login_new_user, create_new_user_by_api):
        driver = get_browser
        feed_page = FeedPage(driver)
        feed_page.open_feed_page()
        feed_page.click_order_link()
        # ждем что открылось модальное окно деталей заказа
        assert feed_page.order_details_is_opened()

    @title('Проверяем что заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    def test_user_orders_are_in_feed(self, create_order, create_new_user_by_api, login_new_user, get_browser):
        driver = get_browser
        profile_page = ProfilePage(driver)
        order = profile_page.get_number_from_order_history()
        feed_page = FeedPage(driver)
        feed_order_list = feed_page.get_order_number_list()
        # проверяем, что заказ в ленте
        assert order in feed_order_list, f'Ошибка проверки Ленты заказов: заказ пользователя: {order} отсутствует в Ленте'

    @title('Проверяем что после оформления заказа его номер появляется в разделе В работе')
    def test_user_order_is_in_work(self, create_order, create_new_user_by_api, get_browser, login_new_user):
        driver = get_browser
        new_order = create_order
        constructor_page = ConstructorPage(driver)
        constructor_page.click_feed_link()
        feed_page = FeedPage(driver)
        orders_list_in_work = feed_page.get_order_list_in_work()
        # проверяем что новый заказ есть в списке
        assert new_order in orders_list_in_work

    @title('Проверяем что создании нового заказа счётчик "Выполнено за всё время" увеличивается')
    def test_orders_total_number(self, get_browser, create_order, create_new_user_by_api, login_new_user):
        driver = get_browser
        feed_page = FeedPage(driver)
        feed_page.open_feed_page()
        orders_before = feed_page.get_orders_total()
        constructor_page = ConstructorPage(driver)
        constructor_page.create_order()
        feed_page.open_feed_page()
        orders_after = feed_page.get_orders_total()
        # проверяем что счетчик увеличился
        assert orders_after > orders_before

    @title('Проверяем что при создании нового заказа счётчик "Выполнено за сегодня" увеличивается')
    def test_orders_today_counter(self, get_browser, create_order, create_new_user_by_api, login_new_user):
        driver = get_browser
        feed_page = FeedPage(driver)
        feed_page.open_feed_page()
        orders_before = feed_page.get_orders_today()
        constructor_page = ConstructorPage(driver)
        constructor_page.create_order()
        feed_page.open_feed_page()
        orders_after = feed_page.get_orders_today()
        # проверяем что счетчик увеличился
        assert orders_after > orders_before