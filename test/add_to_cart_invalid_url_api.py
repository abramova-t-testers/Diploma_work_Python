import requests
import allure
from Configuration import API_3_url, token, key


class AddToCartInvalidUrlApi:
    url = API_3_url

    def __init__(self, url: str, headers: dict) -> None:
        """
        Конструктор создаёт новый экземпляр класса,
        предназначенный для работы с API,
        инициализируя его базовыми настройками.
        :param url: URL-адрес
        :type url: str
        :param headers: словарь HTTP-заголовков,
        применяемых по умолчанию для всех запросов.
        Пример: {'Authorization': 'Bearer token123',
        'Content-Type': 'application/json'}
        :type headers: dict
        """
        self.url = url
        self.headers = {
            "Cookie": token,
            "Authorization": key,
            "Content-Type": headers.get("Content-Type", "application/json"),
        }

    @allure.title("Добавление товара в корзину с ошибкой в URL при запросе")
    @allure.story("Ошибка в URL при запросе на добавление товара в корзину "
                  "(отсутствует последняя буква) и возврат статус-код ответа")
    def add_to_cart_invalid_url(self, product_id: int) -> int:
        """
        Добавление товара в корзину с ошибкой в URL.
        :param product_id: ID товара
        :type product_id: int
        :return: ответ сервера
        """
        body = {
            'id': product_id
        }
        resp = requests.post(self.url, json=body, headers=self.headers)
        return resp.status_code
