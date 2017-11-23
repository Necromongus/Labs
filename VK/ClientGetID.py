from BaseClient import BaseClient


class ClientGetID(BaseClient):
    # метод vk api
    method = "users"
    # GET, POST, ...
    http_method = "get"

    json_data = None

    #Создание экземпляра
    def __init__(self, username):
        self.username = username

    # Получение GET параметров запроса
    def get_params(self):
        return {
            "user_ids": self.username
        }

    # Обработка ответа от VK API
    def response_handler(self, response):
        self.json_data = response.json()
        ids = list()
        try:
            ids.append(self.json_data["response"][0]["uid"])
        except Exception:
            print('Id не найден')
            return None

        return ids

    # Получение данных POST запроса
    def get_json(self):
        return self.json_data
