from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from Configuration import UI_url


class MainPage:
    def __init__(self, driver):
        """
        Конструктор класса MainPage
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

    @allure.title("Поиск книг по названию")
    @allure.story("Вводит поисковой запрос: {term} в"
                  " строку поиска и нажимает кнопку поиска")
    def search(self, term):
        """
        Выполняет поиск книг.
        :param term: искомое название
        """
        self.wait.until(EC.presence_of_element_located(
            (By.ID, "app-search"))).send_keys(term)

        self.wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "button[type=submit]"))).click()

    @allure.title("Проверка результатов поиска")
    @allure.story("Проверяет, что в результатах поиска есть книги: {term}")
    def verify_search_results(self, term) -> bool:
        """
        Проверяет, что в результатах поиска присутствуют
         книги, содержащие искомое название.
        :param term: искомое название
        :return: True, если найдены релевантные результаты; False — иначе
        """
        results = self.wait.until(EC.visibility_of_all_elements_located(
            (By.CLASS_NAME, 'app-products-list__grid')))

        for result in results:
            if term.lower() in result.text.lower():
                return True

        return False
