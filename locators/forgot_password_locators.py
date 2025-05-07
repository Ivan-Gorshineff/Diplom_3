from selenium.webdriver.common.by import By


class ForgotPasswordPageLocators:

    RECOVER_TITLE = (By.XPATH, ".//h2[text()='Восстановление пароля']")  # Заголовок
    RECOVER_BUTTON = (By.XPATH, ".//button[text()='Восстановить']")  # Кнопка "Восстановить"
    EMAIL_FIELD = (By.XPATH, ".//input[@type='text']")  # поле ввода "email"