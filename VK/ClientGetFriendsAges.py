from datetime import datetime
from BaseClient import BaseClient

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
        if today is None:
            today = datetime.utcnow()
        return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

    def response_handler(self, response):
        self.json_data = response.json()
        ages = list()
        today = datetime.utcnow()
        date_tmp = None
        for friend in self.json_data["response"]:
            date_tmp = friend.get("bdate")
            if date_tmp is None or len(date_tmp) < 6:
                continue
            ages.append(self.calculate_age(datetime.strptime(date_tmp, "%d.%m.%Y"),
                                           today))
        return ages

    def get_json(self):
        return self.json_data
