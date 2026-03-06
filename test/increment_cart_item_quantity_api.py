import requests
import allure
from Configuration import API_1_url, API_2_url, token, key


class IncrementCartItemQuantityApi:
    url = API_1_url
    url_2 = API_2_url

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

    @allure.title("Увеличение количества выбранного товара "
                  "в корзине на одну единицу")
    @allure.story("Увеличивает количество выбранного товара в корзине "
                  "на одну единицу и возвращает статус-код ответа")
    def increment_cart_item_quantity(self, items: dict):
        """
        Увеличивает количество выбранного товара в корзине на одну единицу.
        :param items: словарь с товарами для добавления в корзину
        Пример:
        {
            "items": {"id": 123456, "quantity": 5}
        }
        """
        resp = requests.put(self.url_2, json=items, headers=self.headers)
        return resp.status_code, resp.text
