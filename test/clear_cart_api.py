import requests
import allure
from Configuration import API_1_url, token, key


class ClearCartApi:
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

    @allure.title("Очистка корзины")
    @allure.story("Удаляет все содержимое из корзины "
                  "и возвращает статус-код ответа")
    def clear_cart(self, item_id: int) -> int:
        """
        Очищает корзину от содержимого.
        """
        url = f"{self.url}/{item_id}"
        resp = requests.delete(url, headers=self.headers)
        return resp.status_code
