import allure
from selenium import webdriver
import pytest
from search_by_name_ui import MainPage
from invalid_search_ui import MainPageInvalidName


@pytest.fixture
def driver():
    """
    Фикстура для инициализации и завершения работы драйвера
    """
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.mark.ui
@allure.title("Тестирование UI интернет-магазина")
@allure.story("Поиск книг по названию: текст в верхнем и нижнем регистре"
              " одновременно (positive)")
def test_search_by_name_register(driver):
    """
    Тест проверяет корректность поиска по
    названию, где текст в верхнем и нижнем регистре одновременно
    :param driver: WebDriver — объект драйвера, переданный фикстурой
    """
    main_page = MainPage(driver)
    with allure.step("Открытие страницы интернет-магазина"):
        main_page.open()
    with allure.step("Ввод названия книги в двух регистрах и поиск"):
        term = "Гарри Поттер и Орден Феникса"
        main_page.search(term)
    with allure.step(f"Проверка результатов поиска по запросу '{term}'"):
        assert main_page.verify_search_results(term), \
            f"Не найдены результаты, содержащие '{term}'"


@pytest.mark.ui
@allure.title("Тестирование UI интернет-магазина")
@allure.story("Поиск книг по названию: иероглифы (negative)")
def test_search_by_invalid_name_hieroglyph(driver):
    """
    Тест проверяет невозможность поиска по невалидному
    названию - иероглифу в интернет-магазине Читай-город
    :param driver: WebDriver — объект драйвера, переданный фикстурой
    """
    main_page_invalid_name = MainPageInvalidName(driver)
    with allure.step("Открытие страницы интернет-магазина"):
        main_page_invalid_name.open()
    with allure.step("Ввод невалидного названия книги (иероглиф) и поиск"):
        invalid_term = "测"
        main_page_invalid_name.search(invalid_term)
    with allure.step("Проверка отсутствия результатов"):
        assert main_page_invalid_name.no_results(), "Похоже, у нас такого нет"


@pytest.mark.ui
@allure.title("Тестирование UI интернет-магазина")
@allure.story("Поиск книг по названию: латиница (positive)")
def test_search_by_name_latin(driver):
    """
    Тест проверяет корректность поиска по
    названию на латинице
    :param driver: WebDriver — объект драйвера, переданный фикстурой
    """
    main_page = MainPage(driver)
    with allure.step("Открытие страницы интернет-магазина"):
        main_page.open()
    with allure.step("Ввод названия книги на латинице и поиск"):
        term = "Harry Potter"
        main_page.search(term)
    with allure.step(f"Проверка результатов поиска по запросу '{term}'"):
        assert main_page.verify_search_results(term), \
            f"Не найдены результаты, содержащие '{term}'"


@pytest.mark.ui
@allure.title("Тестирование UI интернет-магазина")
@allure.story("Поиск книг по названию: специальные символы (negative)")
def test_search_by_invalid_name_symbols(driver):
    """
    Тест проверяет невозможность поиска по невалидному
    названию - специальным символам в интернет-магазине Читай-город
    :param driver: WebDriver — объект драйвера, переданный фикстурой
    """
    main_page_invalid_name = MainPageInvalidName(driver)
    with allure.step("Открытие страницы интернет-магазина"):
        main_page_invalid_name.open()
    with allure.step("Ввод невалидного названия книги"
                     " специальными символамими поиск"):
        invalid_term = "№^"
        main_page_invalid_name.search(invalid_term)
    with allure.step("Проверка отсутствия результатов"):
        assert main_page_invalid_name.no_results(), "Похоже, у нас такого нет"


@pytest.mark.ui
@allure.title("Тестирование UI интернет-магазина")
@allure.story("Поиск книг по названию: цифры (positive)")
def test_search_by_name_numbers(driver):
    """
    Тест проверяет корректность поиска по
    названию, состоящему из цифр
    :param driver: WebDriver — объект драйвера, переданный фикстурой
    """
    main_page = MainPage(driver)
    with allure.step("Открытие страницы интернет-магазина"):
        main_page.open()
    with allure.step("Ввод названия книги цифрами и поиск"):
        term = "1984"
        main_page.search(term)
    with allure.step(f"Проверка результатов поиска по запросу '{term}'"):
        assert main_page.verify_search_results(term), \
            f"Не найдены результаты, содержащие '{term}'"
