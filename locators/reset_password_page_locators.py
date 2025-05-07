from selenium.webdriver.common.by import By


class ResetPasswordPageLocators:

    SAVE_BUTTON = (By.XPATH, ".//button[text()='Сохранить']")  # Кнопка "Сохранить"
    EYE_ICON = (By.XPATH, '//*[contains(@class,"input__icon")]')
    PASSWORD_PLACEHOLDER = (By.XPATH, ".//label[text()='Пароль']")  # Плейсхолдер поля "Пароль"
    FOCUSED_FIELD = (By.XPATH, '//*[contains(@class,"input__placeholder")]')  # Класс поля "Пароль"
    FOCUSED_TEXT = 'input__placeholder-focused'