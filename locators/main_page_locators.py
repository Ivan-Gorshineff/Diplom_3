from selenium.webdriver.common.by import By


class MainPageLocators:

    ORDER_BUTTON = (By.XPATH, ".//button[text()='Оформить заказ']")  # Кнопка "Оформить заказ" на Главной странице
    LOGIN_BUTTON = (By.XPATH, ".//button[text()='Войти в аккаунт']")  # Кнопка "Войти в аккаунт" на Главной странице
    PROFILE_LINK = (By.XPATH, ".//a[@href='/account']")  # Ссылка Личный кабинет
    CONSTRUCTOR_LINK = (By.XPATH, ".//a[@href='/']")  # ссылка на Конструктор
    FEED_LINK = (By.XPATH, ".//a[@href='/feed']")  # ссылка на Ленту заказов
    ACTIVE_TEXT = 'link_active'  # текст в классе активной вкладки
    TOTAL_TODAY = (By.XPATH, ".//p[text()='Выполнено за сегодня:']")  # Последний элемент нв странице Лента заказов
    ANY_BUTTON = (By.XPATH, ".//button")  # Кнопка "Оформить заказ"/"Войти в аккаунт" на Главной странице

    # Вкладка Конструктор:
    INGREDIENT_LINK = (By.XPATH, '//*[contains(@href,"/ingredient/")]')  # 1й ингредиент из 15 (булка)
    DETAILS_OPENED_LINK = (By.XPATH, './/section[contains(@class,"Modal_modal_opened")]')
    DETAILS_TITLE_LINK = (By.XPATH, ".//h2[text()='Детали ингредиента']")
    DETAILS_CLOSE_LINK = (By.XPATH, './/section[contains(@class,"Modal_modal_opened")]//button')
    DETAILS_LINK_CLASS = 'Modal_modal__P3_V5'
    DRAGANDROP_BUN_TARGET = (By.XPATH, './/span[text()="Перетяните булочку сюда (верх)"]')
    INGREDIENT_COUNTER_LINK = (By.XPATH,'//*[contains(@href,"/ingredient/")]//p[contains(@class,"counter_counter__num")]')  # счетчик ингредиента
    INGREDIENT_3_LINK = (By.XPATH, '(//*[contains(@href,"/ingredient/")])[3]')  # 3й ингредиент из 15 (соус)
    INGREDIENT_7_LINK = (By.XPATH, '(//*[contains(@href,"/ingredient/")])[7]')  # 7й ингредиент из 15 (начинка)
    DRAGNDROP_BURGER_TARGET = (By.XPATH, '//*[contains(@class,"BurgerConstructor_basket__list")]')

    # Модальное окно - заказ оформлен
    ORDER_ID_LINK = (By.XPATH, './/p[text()="Ваш заказ начали готовить"]')
    ORDER_MODAL_LINK = (By.XPATH, './/section[contains(@class,"Modal_modal_")]')  # common/hidden
    ORDER_MODAL_OPENED_LINK = (By.XPATH, './/section[contains(@class,"Modal_modal_opened__3ISw4")]')  # visible
    ORDER_CLOSE_BUTTON = (By.XPATH, './/button[contains(@class,"Modal_modal__close")]')  # visible
    ORDER_MODAL_ORDER_NUMBER = (By.XPATH, './/h2[contains(@class,"Modal_modal__title_shadow")]')  # номер нового заказа