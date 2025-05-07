from selenium.webdriver.common.by import By


class FeedPageLocators:

    ORDER_LINK = (By.XPATH, '//*[contains(@href,"/feed/")]')
    ORDER_DETAILS_OPENED = (By.XPATH, './/section[contains(@class,"Modal_modal_opened")]')
    ORDER_LIST_ITEM = (By.XPATH, './/li[contains(@class,"OrderHistory_listItem")]')
    ORDER_LIST_ORDER_NUMBER = (By.XPATH, './/p[@class="text text_type_digits-default"]')
    ORDER_STATUS_BOX = (By.XPATH, './/div[contains(@class,"OrderFeed_orderStatusBox")]')
    ORDER_STATUS_BOX_LIST = (By.XPATH, './/ul[contains(@class,"OrderFeed_orderList")]')
    ORDER_STATUS_BOX_LIST1 = (By.XPATH, '(.//ul[contains(@class,"OrderFeed_orderList")])[1]')
    ORDER_STATUS_BOX_LIST2 = (By.XPATH, '(.//ul[contains(@class,"OrderFeed_orderList")])[2]')
    ORDER_STATUS_BOX_LIST1_ITEM = (By.XPATH, '(.//ul[contains(@class,"OrderFeed_orderList")])[1]/li')
    ORDER_STATUS_BOX_LIST2_ITEM = (By.XPATH, '(.//ul[contains(@class,"OrderFeed_orderList")])[2]/li')
    ORDER_STATUS_BOX_LIST2_ITEM_DIGIT = (By.XPATH, '(.//ul[contains(@class,"OrderFeed_orderList")])[2]/li[contains(@class,"digits")]')
    ORDER_FEED_NUMBER = (By.XPATH, './/p[contains(@class,"OrderFeed_number")]')
