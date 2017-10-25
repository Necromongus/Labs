import requests

class BaseClient:

    # URL vk api
    BASE_URL = "https://api.vk.com/method/"
    # метод vk api
    method = None
    # GET, POST, ...

    http_method = None

    # Получение GET параметров запроса
    def get_params(self):
        return None

    # Получение данных POST запроса
    def get_json(self):
        return None

    # Получение HTTP заголовков
    def get_headers(self):
        return None

    # Склейка url
    def generate_url(self, method):
        return '{0}{1}'.format(self.BASE_URL, method)

    # Отправка запроса к VK API
    def _get_data(self, method, http_method):

        # todo выполнить запрос
        response = requests.get(self.BASE_URL + self.method + "." + self.http_method, params = self.get_params())

        return self.response_handler(response)

    # Обработка ответа от VK API
    def response_handler(self, response):
        return response

    # Запуск клиента
    def execute(self):
        return self._get_data(
            self.method,
            http_method=self.http_method
        )



from datetime import datetime
debug = True

class ClientGetID(BaseClient):
    username = None
    # метод vk api
    method = "users"
    # GET, POST, ...
    http_method = "get"

    json_data = None

    def __init__(self, username):              #Создание экземпляра
        self.username = username

    # Получение GET параметров запроса
    def get_params(self):
        return {
        "user_ids": self.username
        }

    # Обработка ответа от VK API
    def response_handler(self, response):
        self.json_data = response.json()
        return self.json_data["response"][0]["uid"]

    # Получение данных POST запроса
    def get_json(self):
        return self.json_data


class ClientGetFriendsAges(BaseClient):
    # метод vk api
    method = "friends"
    # id пользователя
    user_id = None
    # GET, POST, ...
    http_method = "get"

    json_data = None

    def __init__(self, user_id):
        self.user_id = user_id

    def get_params(self):
        return {
        "user_id": self.user_id,
        "fields": "bdate"
        }

    def calculate_age(self, born, today):
        if today == None:
            today = datetime.utcnow()
        return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

    def response_handler(self, response):
        self.json_data = response.json()
        ages = list()
        today = datetime.utcnow()
        date_tmp = None
        for friend in self.json_data["response"]:
            date_tmp = friend.get("bdate")
            if date_tmp == None or len(date_tmp) < 6:
                continue
            ages.append( self.calculate_age( datetime.strptime( date_tmp, "%d.%m.%Y"), today))
        return ages

    def get_json(self):
        return self.json_data




class Gist ():
    # данные гистаграммы
    _data = None
    _data_sorting = dict()

    def __init__(self, date):
        self._data = date
        for number in date:
            self._data_sorting.update({number: self._data_sorting.get(number, 0) + 1})

    def get_data(self):
        return self._data

    def printHist(self):
        str_out = ""
        for age, stat in self._data_sorting.items():
            str_out += str(age).ljust(4) + str().ljust(stat, '#') + '\n'
        print( str_out)






debug = True
username = "id65287085"

get_id = ClientGetID(username).execute()
friends_ages = ClientGetFriendsAges(get_id).execute()

if debug:
    print("ID: ", get_id)
    print("Ages: ", friends_ages)

mygist = Gist(friends_ages)
mygist.printHist()

