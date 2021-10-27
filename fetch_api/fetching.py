from functools import lru_cache

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

    def fetch_posts_by_user_id(self, user_id: int):
        data = self.session.get(f'{self.url}/posts?userId={user_id}').json()
        return data

    def fetch_all_todos(self):
        data = self.session.get(f'{self.url}/todos').json()
        return data

    def fetch_todo(self, todo_id: int):
        data = self.session.get(f'{self.url}/todos/{todo_id}').json()
        return data

    def fetch_todo_by_user_id(self, user_id: int):
        data = self.session.get(f'{self.url}/todos?userId={user_id}').json()
        return data
