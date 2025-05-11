# UI Stellar burgers

## Структура проекта:
`tests/` - папка с файлами тестов

- `tests/test_forgot_password_page` - тесты функциональности Восстановление пароля
- `tests/test_profile_page` - тесты функциональности Личный кабинет
- `tests/test_constructor_page` - тесты основного функционала (Главная страница)
- `tests/test_feed_page` - тесты раздела «Лента заказов»

`pages/` - папка page object (классы страниц РОМ):

- `pages/base_page` - класс базового класса для классов страниц, общие методы
- `pages/main_page` - класс Главной страницы
- `pages/login_page` - класс страницы авторизации
- `pages/forgot_password_page` - класс страницы восстановления пароля
- `pages/reset_password_page` - класс страницы сброса пароля
- `pages/profile_page` - класс страницы Личного кабинета
- `pages/constructor_page` - класс раздела Конструктор на Главной страницы
- `pages/feed_page` - класс раздела Лента заказов на Главной странице

`helpers/` - папка вспомогательных функций:

`conftest` - функции-фикстуры

`locators/` папка с локаторами:
- `constructor_page_locators` - локаторы раздела Конструктор на Главной страницы
- `feed_page_locators` - локаторы раздела Лента заказов на Главной странице
- `forgot_password_locators` - локаторы страницы восстановления пароля
- `login_page_locators` - локаторы страницы авторизации
- `main_page_locators` - локаторы Главной страницы
- `profile_page_locators` - локаторы страницы Личного кабинета
- `reset_password_page_locators` - локаторы страницы сброса пароля

`data.py` - константы, URL-адреса и данные для тестов

`requirements.txt` - файл внешних зависимостей

