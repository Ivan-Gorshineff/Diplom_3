from selenium.webdriver.common.by import By


class ProfilePageLocators:

    SAVE_BUTTON = (By.XPATH, ".//button[text()='Сохранить']")  # Кнопка "Сохранить"
    ORDER_HISTORY_LINK = (By.XPATH, ".//a[@href='/account/order-history']")  # Ссылка История заказов
    ORDER_HISTORY_IS_ACTIVE = 'Account_link_active'  # История заказов активна
    EXIT_BUTTON = (By.XPATH, ".//button[text()='Выход']")  # Кнопка "Выход"
    ORDER_HISTORY_ORDER_NUMBER = (By.XPATH, './/li[contains(@class,"OrderHistory_listItem")]/a/div/p[contains(@class,"digits")]')