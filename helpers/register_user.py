import random
import string

from helpers.api_requests import ApiRequests as ar
from allure import step


# Вспомогательные функции для регистрации/удаления пользователя с помощью API
# генерируем логин, пароль и имя пользователя
class GenerateUser:

    @staticmethod
    @step('Генерируем данные нового пользователя: email, password, name')
    def generate_random_user_data():
        email = GenerateUser.generate_random_string(10) + '@mail.ru'
        password = GenerateUser.generate_random_string(10)
        name = GenerateUser.generate_random_string(10)
        user_data = {
            'email': email,
            'password': password,
            'name': name
        }
        # возвращаем словарь
        return user_data

    @staticmethod
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for _ in range(length))
        return random_string

    @staticmethod
    @step('Отправляем запрос на создание нового пользователя')
    def try_to_create_user(user_data):
        response = ar.request_on_create_user(user_data)
        return response

    @staticmethod
    @step('Удаляем пользователя')
    def try_to_delete_user(auth_token):
        headers = {'Authorization': auth_token}
        response = ar.request_on_delete_user(headers)
        return response
