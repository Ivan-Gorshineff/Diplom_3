_browser = 'Chrome'


# тестовые данные для функции восстановления пароля
class UserData:
    USER_EMAIL = 'IvanGorshinev019@ya.ru'
    USER_PASSWORD = 'ivan_ivanov'


class Urls:
    MAIN_PAGE_URL = 'https://stellarburgers.nomoreparties.site'  # URL для Главной страницы
    FORGOT_PASSWORD_PAGE_URL = f'{MAIN_PAGE_URL}/forgot-password'  # URL страницы восстановления пароля
    LOGIN_PAGE_URL = f'{MAIN_PAGE_URL}/login'  # URL для страницы авторизации
    RESET_PASSWORD_PAGE_URL = f'{MAIN_PAGE_URL}/reset-password'  # URL страницы восстановления пароля
    PROFILE_PAGE_URL = f'{MAIN_PAGE_URL}/account/profile'  # URL для страницы Личный кабинет
    ORDER_HISTORY_URL = f'{MAIN_PAGE_URL}/account/order-history'  # URL для страницы Личный кабинет
    FEED_PAGE_URL = f'{MAIN_PAGE_URL}/feed'  # URL для Главной страницы


class ResponseKeys:
    # поля в ответе API
    ACCESS_TOKEN    = 'accessToken'
    REFRESH_TOKEN   = 'refreshToken'

    # поля для отправки запроса к API
    AUTH_TOKEN_KEY  = 'Authorization'
    TOKEN_KEY       = 'token'
