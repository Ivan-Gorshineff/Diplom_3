from allure import step
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.url = None

    @step('Открываем страницу по URL')
    def open_page(self, url):
        return self.driver.get(url)

    @step('Ждем загрузку элемента по локатору')
    def wait_for_load_element(self, locator):
        return WebDriverWait(self.driver, 60).until(
            EC.visibility_of_element_located(locator))

    @step('Ждем открытие страницы при переходе по ссылке URL')
    def wait_for_open_page(self, url):
        return WebDriverWait(self.driver, 60).until(EC.url_to_be(url))

    @step('Ждем загрузку всех элементов HTML по локатору')
    def wait_for_load_all_elements(self, locator):
        return WebDriverWait(self.driver, 60).until(
            EC.visibility_of_all_elements_located(locator))

    @step('Ждем появление в DOM элемента HTML по локатору')
    def wait_for_presence_of_element(self, locator):
        return WebDriverWait(self.driver, 60).until(EC.presence_of_element_located(locator))

    @step('Получаем текущий URL')
    def get_current_url(self):
        return self.driver.current_url

    @step('Ищем элемент HTML по локатору')
    def find_element(self, locator):
        return self.driver.find_element(*locator)

    @step('Ищем все элементы HTML по локатору')
    def find_all_elements(self, locator):
        return self.driver.find_elements(*locator)

    @step('Ждем кликабельности элемента по локатору')
    def wait_for_clickable_element(self, locator):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable(locator))

    @step('Вводим текст в поле по локатору')
    def set_value(self, locator, value):
        return self.wait_for_load_element(locator).send_keys(value)

    @step('Получаем значение поля по локатору')
    def get_value(self, locator):
        return self.wait_for_load_element(locator).get_attribute('value')

    @step('Получаем текст в поле по локатору')
    def get_text(self, locator):
        return self.wait_for_load_element(locator).text

    @step('Прокручиваем страницу до элемента по локатору')
    def scroll_to_element_by_locator(self, locator):
        element = WebDriverWait(self.driver, 60).until(
            EC.visibility_of_element_located(locator))
        self.driver.execute_script('arguments[0].scrollIntoView();', element)
        return element

    @step('Ждем видимости элемента по локатору и кликаем')
    def click_element_by_locator(self, locator):
        WebDriverWait(self.driver, 60).until(
            EC.visibility_of_element_located(locator)).click()

    @step('Ждем кликабельности элемента по локатору и кликаем')
    def click_element_by_locator_when_clickable(self, locator):
        element = WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable(locator))
        element.click()

    @step('Кликаем элемент')
    def click_element(self, element):
        element.click()

    @step('Перемещаем элемент')
    def drag_and_drop(self, source, target):
        action = ActionChains(self.driver)
        action.drag_and_drop(source, target).perform()

    @step('Проверяем, что в имени класса появляется текст')
    def wait_for_text_in_class_name(self, locator, text):
        return WebDriverWait(self.driver, 60).until(
            EC.text_to_be_present_in_element_attribute(locator, 'class', text))

    @step('Проверяем что элемент становится невидимым')
    def wait_for_invisibility_of_element(self, locator):
        return WebDriverWait(self.driver, 30).until(EC.invisibility_of_element_located(locator))