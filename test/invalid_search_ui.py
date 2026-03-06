from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
import allure
from Configuration import UI_url


class MainPageInvalidName:
    def __init__(self, driver):
        """
        Конструктор класса MainPageInvalidName
        :param driver: WebDriver — объект драйвера Selenium
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.title("Открытие страницы интернет-магазина")
    @allure.story("Открывает главную страницу "
                  "интернет-магазина книг Читай-город")
    def open(self):
        """
        Открывает главную страницу интернет-магазина
        """
        self.driver.get(UI_url)

    @allure.title("Поиск книг по невалидному названию")
    @allure.story("Вводит поисковой невалидный запрос: {invalid_term} в"
                  " строку поиска и нажимает кнопку поиска")
    def search(self, invalid_term):
        """
        Выполняет поиск книг.
        :param invalid_term: искомое невалидное название
        """
        self.wait.until(EC.presence_of_element_located(
            (By.ID, "app-search"))).send_keys(invalid_term)

        self.wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "button[type=submit]"))).click()

    @allure.title("Проверка результатов поиска")
    @allure.story("Проверяет, что поиск не дал результатов")
    def no_results(self) -> bool:
        """
        Проверяет, что поиск не дал результатов,
        по наличию сообщения «Похоже, у нас такого нет».
        :return: True, если сообщение видно (результатов нет);
        False — если сообщение отсутствует
        """
        try:
            self.wait.until(EC.text_to_be_present_in_element(
                (By.CLASS_NAME, 'catalog-stub__title'),
                'Похоже, у нас такого нет'))
            return True
        except (TimeoutException, StaleElementReferenceException):
            return False
