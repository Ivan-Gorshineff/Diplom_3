from selenium.webdriver.common.by import By


class LoginPageLocators:

    FORGOT_PAGE_LINK = (By.XPATH, ".//a[text()='Восстановить пароль']")  # Ссылка "Восстановить пароль" на странице авторизации
    LOGIN_BUTTON = (By.XPATH, ".//button[text()='Войти']")  # Кнопка "Войти"
    EMAIL_FIELD = (By.XPATH, ".//input[@type='text']")  # Поле "email"
    PASSWORD_FIELD = (By.XPATH, ".//input[@type='password']")  # Поле "Пароль"
