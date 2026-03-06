import requests
import allure
from Configuration import API_1_url, token, key


class AddToCartApi:
    url = API_1_url

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

    @allure.title("Добавление товара в корзину")
    @allure.story("Добавляет товар в корзину и возвращает статус-код ответа")
    def add_to_cart(self, product_id: int) -> int:
        """
        Добавляет товар в корзину.
        :param product_id: ID товара
        :type product_id: int
        :return: ответ сервера
        """
        body = {
            'id': product_id
        }
        resp = requests.post(self.url, json=body, headers=self.headers)
        return resp.status_code
