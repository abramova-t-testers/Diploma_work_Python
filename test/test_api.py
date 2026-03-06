import allure
import pytest
import json
from add_to_cart_api import AddToCartApi
from increment_cart_item_quantity_api import IncrementCartItemQuantityApi
from wrong_method_add_to_cart_api import WrongMethodAddToCartApi
from add_to_cart_invalid_url_api import AddToCartInvalidUrlApi
from clear_cart_api import ClearCartApi
from Configuration import API_1_url
from Configuration import API_2_url
from Configuration import API_3_url


@pytest.mark.api
@allure.title("Тестирование API интернет-магазина")
@allure.story("Добавление товара в корзину")
@pytest.mark.parametrize("product_id, expected_status", [(2850454, 200)])
def test_add_product_to_cart(product_id: int, expected_status: int) -> None:
    """
    Тест для метода добавления товара в корзину.
    Проверяет успешность запроса на добавление товара в корзину.
    :param product_id: id добавляемого товара
    :type product_id: int
    :param expected_status: ожидаемый статус
    :type expected_status: int
    """
    with allure.step("Добавить товар в корзину"):
        headers = {"Content-Type": "application/json"}
        add_to_cart_api = AddToCartApi(API_1_url, headers)
        s_code = add_to_cart_api.add_to_cart(product_id)

    with allure.step("Проверить статус запроса"):
        assert s_code == expected_status


@pytest.mark.api
@allure.title("Тестирование API интернет-магазина")
@allure.story("Увеличение количества выбранного"
              " товара в корзине на одну единицу")
@pytest.mark.parametrize("product_id, item_id, initial_qty,"
                         " expected_qty, expected_status",
                         [(2850454, 250666129, 1, 2, 200)])
def test_increment_cart_item_quantity(product_id: int, item_id: int,
                                      initial_qty: int, expected_qty: int,
                                      expected_status: int) -> None:
    """
    Тест для метода увеличения товара в корзине на одну единицу.
    Проверяет успешность запроса на изменение количества товара в корзине.
    :param product_id: id добавляемого товара
    :type product_id: int
    :param item_id: id добавленного в корзину товара
    :type item_id: int
    :param initial_qty: первоначальное количество товара в корзине
    :type initial_qty: int
    :param expected_qty: ожидаемое количество товара в корзине
    :type expected_qty: int
    :param expected_status: ожидаемый статус
    :type expected_status: int
    """
    headers = {"Content-Type": "application/json"}
    with allure.step("Добавить товар в корзину"):
        add_to_cart_api = AddToCartApi(API_1_url, headers)
        add_response = add_to_cart_api.add_to_cart(product_id)

    with allure.step("Проверить статус запроса"):
        assert add_response == expected_status

    with allure.step("Увеличить количество товара на 1"):
        increment_cart_item_quantity_api = IncrementCartItemQuantityApi(API_2_url, headers)
        status_code, raw_response = increment_cart_item_quantity_api.increment_cart_item_quantity({
            'id': item_id,
            'quantity': initial_qty + 1
        })
        try:
            data = json.loads(raw_response)
        except json.JSONDecodeError:
            pytest.fail(f"Невалидный JSON в ответе: {raw_response}")

    with allure.step("Проверить статус запроса"):
        assert status_code == expected_status

    with allure.step("Проверяем содержимое корзины после изменения"):
        assert data["products"][0]["quantity"] == expected_qty, (
            f"Количество {data['products'][0]['quantity']}, "
            f"ожидалось {expected_qty}"
        )


@pytest.mark.api
@allure.title("Тестирование API интернет-магазина")
@allure.story("Очистка корзины")
@pytest.mark.parametrize("product_id, item_id, expected_status, "
                         "expected_status_after_clear",
                         [(2850454, 250666129, 200, 204)])
def test_clear_cart(product_id: int, item_id: int,
                    expected_status: int,
                    expected_status_after_clear: int) -> None:
    """
    Тест для метода очистки корзины.
    Проверяет успешность запроса на уудаление товара из корзины.
    :param product_id: id добавляемого товара
    :type product_id: int
    :param item_id: id добавленного в корзину товара
    :type item_id: int
    :param expected_status: ожидаемый статус
    :type expected_status: int
    """
    headers = {"Content-Type": "application/json"}
    with allure.step("Добавить товар в корзину"):
        add_to_cart_api = AddToCartApi(API_1_url, headers)
        add_response = add_to_cart_api.add_to_cart(product_id)

    with allure.step("Проверить статус запроса"):
        assert add_response == expected_status

    with allure.step("Очистка корзины"):
        clear_cart_api = ClearCartApi(API_1_url, headers)
        status_code = clear_cart_api.clear_cart(item_id)

    with allure.step("Проверить статус запроса"):
        assert status_code == expected_status_after_clear


@pytest.mark.api
@allure.title("Тестирование API интернет-магазина")
@allure.story("Добавление товара в корзину с неверным"
              " методом (PUT вместо POST)")
@pytest.mark.parametrize("product_id, expected_status", [(2850454, 405)])
def test_wrong_method_add_to_cart(product_id: int,
                                  expected_status: int) -> None:
    """
    Тест для неверного метода добавления товара в корзину.
    Проверяет успешность неверного запроса на добавление товара в корзину.
    :param product_id: id добавляемого товара
    :type product_id: int
    :param expected_status: ожидаемый статус
    :type expected_status: int
    """
    with allure.step("Добавить товар в корзину неверным методом"):
        headers = {"Content-Type": "application/json"}
        wrong_method_add_to_cart_api = WrongMethodAddToCartApi(API_1_url, headers)
        s_code = wrong_method_add_to_cart_api.wrong_method_add_to_cart(product_id)

    with allure.step("Проверить статус запроса"):
        assert s_code == expected_status


@pytest.mark.api
@allure.title("Тестирование API интернет-магазина")
@allure.story("Добавление товара в корзину с ошибкой в URL"
              " при запросе (отсутствует последняя буква)")
@pytest.mark.parametrize("product_id, expected_status", [(2850454, 404)])
def test_add_to_cart_invalid_url(product_id: int,
                                 expected_status: int) -> None:
    """
    Тест для добавления товара в корзину с неверным URL.
    Проверяет успешность неверного запроса на добавление товара в корзину.
    :param product_id: id добавляемого товара
    :type product_id: int
    :param expected_status: ожидаемый статус
    :type expected_status: int
    """
    with allure.step("Добавить товар в корзину с неверным URL"):
        headers = {"Content-Type": "application/json"}
        add_to_cart_invalid_url_api = AddToCartInvalidUrlApi(API_3_url, headers)
        s_code = add_to_cart_invalid_url_api.add_to_cart_invalid_url(product_id)

    with allure.step("Проверить статус запроса"):
        assert s_code == expected_status
