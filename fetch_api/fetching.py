import requests


class JsonPlaceHolderAPI:
    def __init__(self):
        self.session = requests.Session()
        self.url = 'https://jsonplaceholder.typicode.com'

    def fetch_all_users(self):
        data = self.session.get(f'{self.url}/users').json()
        return data

    def fetch_user(self, user_id: int):
        data = self.session.get(f'{self.url}/users/{user_id}').json()
        return data

    def fetch_all_posts(self):
        data = self.session.get(f'{self.url}/posts').json()
        return data

    def fetch_post(self, post_id: int):
        data = self.session.get(f'{self.url}/posts/{post_id}').json()
        return data

    def fetch_posts_by_user_id(self):
        pass
