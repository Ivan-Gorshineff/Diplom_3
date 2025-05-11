from allure import step
import requests


class ApiData:

    SERVER_URL = 'https://stellarburgers.nomoreparties.site'
    # Эндпойнты запросов к API
    API_CREATE_USER = '/api/auth/register'
    API_DELETE_USER = '/api/auth/user'

class ApiRequests:

    @staticmethod
    @step('Отправляем API-запрос на создание пользователя')
    def request_on_create_user(payload):
        request_url = f'{ApiData.SERVER_URL}{ApiData.API_CREATE_USER}'
        response = requests.post(f'{request_url}', json=payload, timeout=(60, 60))
        return response

    @staticmethod
    @step('Отправляем API-запрос на удаление пользователя')
    def request_on_delete_user(headers):
        request_url = f'{ApiData.SERVER_URL}{ApiData.API_DELETE_USER}'
        response = requests.delete(f'{request_url}', headers=headers, timeout=(60, 60))
        return response
